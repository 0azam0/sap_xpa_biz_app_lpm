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


from pathlib import Path
import datetime as datetime

from infra.common.globals import GlobalPredictionEnvironmentPlatforms

from .common.schema import (
    PredictionEnvironmentArgs,
    UseCaseArgs,
)
from .common.stack import get_stack

project_name = get_stack()


prediction_environment_args = PredictionEnvironmentArgs(
    resource_name=f"Recipe Template Prediction Environment [{project_name}]",
    platform=GlobalPredictionEnvironmentPlatforms.DATAROBOT_SERVERLESS,
).model_dump(mode="json", exclude_none=True)


use_case_args = UseCaseArgs(
    resource_name=f"Recipe Template Use Case [{project_name}]",
    description="Use Case for Recipe Template application",
)

application_path_str = "frontend/"
runtime_parameters_spec_template = "metadata.yaml.jinja"
runtime_parameters_spec = "metadata.yaml"

model_training_nb_name = "train_model.ipynb"
model_scoring_nb_name = "batch_predict.ipynb"
model_training_nb_path = Path(f"notebooks/{model_training_nb_name}")
model_scoring_nb_path = Path(f"notebooks/{model_scoring_nb_name}")
model_training_nb_output_name = "train_model_output.yaml"
model_training_output_name = f"train_model_output.{project_name}.yaml"
model_training_output_path_str = f"{application_path_str}{model_training_output_name}"
model_training_output_path = Path(model_training_output_path_str)
