# Copyright 2024 DataRobot, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv # type: ignore
import pulumi # type: ignore
import pulumi_datarobot as datarobot # type: ignore
import yaml # type: ignore

def key_exists(env_file, key):
    try:
        if not os.path.exists(env_file):
            raise FileNotFoundError(f"{env_file} not found")
        load_dotenv(env_file)
        if key in os.environ:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

print("Checking for .env file...")
train_and_predict=key_exists('.env','TRAIN_AND_PREDICT')
train_only=key_exists('.env','TRAIN_ONLY')
predict_only=key_exists('.env','PREDICT_ONLY')
print("done!")

from infra import (
    settings_app,
    settings_main,
)
from infra.common.papermill import run_notebook
from infra.settings_deployment import (
    deployment_args,
)
from infra.settings_main import model_training_nb_path, model_training_output_path, model_scoring_nb_path
from starter.i18n import LocaleSettings
from starter.resources import (
    app_env_name,
    app_locale,
    deployment_env_name,
    scoring_dataset_env_name,
)
from starter.schema import AppSettings

LocaleSettings().setup_locale()

# if not model_training_output_path.exists():    
if train_and_predict:
    pulumi.info("Executing model training notebook...")
    run_notebook(model_training_nb_path)
    pulumi.info("Executing model scoring notebook...")
    run_notebook(model_scoring_nb_path)
elif train_only:
    pulumi.info("Executing model training notebook...")
    run_notebook(model_training_nb_path)
elif predict_only:
    pulumi.info("Executing model scoring notebook...")
    run_notebook(model_scoring_nb_path)
else:
    pulumi.info(
        f"Using existing model training outputs in '{model_training_output_path}'"
    )
with open(model_training_output_path) as f:
    model_training_output = AppSettings(**yaml.safe_load(f))

prediction_environment = datarobot.PredictionEnvironment(
    **settings_main.prediction_environment_args,
)

deployment = datarobot.Deployment(
    prediction_environment_id=prediction_environment.id,
    registered_model_version_id=model_training_output.registered_model_version_id,
    **deployment_args.model_dump(),
    use_case_ids=[model_training_output.use_case_id],
)

app_runtime_parameters = [
    datarobot.ApplicationSourceRuntimeParameterValueArgs(
        key=deployment_env_name,
        type="deployment",
        value=deployment.id,
    ),
    datarobot.ApplicationSourceRuntimeParameterValueArgs(
        key=scoring_dataset_env_name,
        type="string",
        value=model_training_output.training_dataset_id,
    ),
    datarobot.ApplicationSourceRuntimeParameterValueArgs(
        key=app_locale, type="string", value=LocaleSettings().app_locale
    ),
]

application_source = datarobot.ApplicationSource(
    files=settings_app.get_app_files(app_runtime_parameters),
    runtime_parameter_values=app_runtime_parameters,
    **settings_app.app_source_args,
)

app = datarobot.CustomApplication(
    resource_name=settings_app.app_resource_name,
    source_version_id=application_source.version_id,
    use_case_ids=[model_training_output.use_case_id],
)

app.id.apply(settings_app.ensure_app_settings)


pulumi.export(scoring_dataset_env_name, model_training_output.training_dataset_id)
pulumi.export(deployment_env_name, deployment.id)
pulumi.export(app_env_name, app.id)
pulumi.export(settings_app.app_resource_name, app.application_url)
