# SAP Extended Planning and Analytics (xP&A) Late Payments Business Application Template

This business application template outlines a basic late payments predictive model development and prediction workflow in DataRobot. It leverages the data stored in SAP Datasphere, acquired from SAP Cloud ERP, to develop a predictive model. It is a good starter for making a new recipe. DataRobot recommends modifying this README to include information about the template you are creating.

> [!WARNING]
> Application templates are intended to be starting points that provide guidance on how to develop, serve, and maintain Buisness AI applications.
> They require a developer or data scientist to adapt and modify them to meet business requirements before being put into production.

## Table of Contents
1. [Setup](#setup)
2. [Architecture overview](#architecture-overview)
3. [Why build AI Apps with DataRobot app templates?](#why-build-ai-apps-with-datarobot-app-templates)
4. [Make changes](#make-changes)
   - [Change the data and how the model is trained](#change-the-data-and-how-the-model-is-trained)
   - [Change the front-end](#change-the-front-end)
   - [Change the language in the front-end](#change-the-language-in-the-front-end)
5. [Share results](#share-results)
6. [Delete all resources](#delete-all-provisioned-resources)
7. [Setup for advanced users](#setup-for-advanced-users)
8. [Data privacy](#data-privacy)

## Setup

> [!IMPORTANT]  
> If you are running this template in a DataRobot codespace, `pulumi` is already configured and the repository is automatically cloned;
> skip to **Step 3**.

1. If `pulumi` is not already installed, install the CLI following instructions [here](https://www.pulumi.com/docs/iac/download-install/).
   After installing `pulumi` for the first time, restart your terminal and run:

   ```sh
   pulumi login --local  # omit --local to use Pulumi Cloud (requires separate account)
   ```

2. Clone the template repository.

   ```sh
   git clone https://github.com/datarobot-community/sap_xpa_biz_app_lpm
   cd sap_xpa_biz_app_lpm
   ```

3. Rename the file `.env.template` to `.env` in the root directory of the repo and populate your DataRobot and SAP Datasphere credentials alongwith respective data views residing in SAP Datasphere.

```sh
DATAROBOT_API_TOKEN=
DATAROBOT_ENDPOINT=
OPENAI_API_KEY=
OPENAI_API_VERSION=
OPENAI_API_BASE=
OPENAI_API_DEPLOYMENT_ID=
PULUMI_CONFIG_PASSPHRASE=
# SAP DSP

SAP_DSP_HOST_NAME=
SAP_DSP_PORT=
SAP_DSP_DATA_STORE_CANONICAL_NAME=
SAP_DSP_ALTERNATE_DATA_STORE_CANONICAL_NAME=
SAP_DSP_DATA_SOURCE=
#
SAP_DSP_USER=
SAP_DSP_USER_PASSWD=
SAP_DSP_CONNECTION=
SAP_DSP_CREDENTIALS=
#
SAP_DSP_LATE_PAYMENTS_TRAINING_DATA_QUERY=
SAP_DSP_LATE_PAYMENTS_TRAINING_DATA_SET=
SAP_DSP_LATE_PAYMENTS_PRIMARY_SCORING_DATA_QUERY=
SAP_DSP_LATE_PAYMENTS_SECONDARY_SCORING_DATA_QUERY=
SAP_DSP_LATE_PAYMENTS_HOLDOUT_PRIMARY_DATA_SET=
SAP_DSP_LATE_PAYMENTS_HOLDOUT_SECONDARY_DATA_SET=
```
Use the following resources to locate the required credentials:
   - **DataRobot API Token**: Refer to the *Create a DataRobot API Key* section of the [DataRobot API Quickstart docs](https://docs.datarobot.com/en/docs/api/api-quickstart/index.html#create-a-datarobot-api-key).
   - **DataRobot Endpoint**: Refer to the *Retrieve the API Endpoint* section of the [DataRobot API Quickstart docs](https://docs.datarobot.com/en/docs/api/api-quickstart/index.html#retrieve-the-api-endpoint).

4. In a terminal, run the following command:

   ```sh
   python quickstart.py YOUR_PROJECT_NAME --train-and-predict --train-only --predict_only # Windows users may have to use `py` instead of `python`
   ```

Options are mutually exclusive and at least one is required. The options are describes in the following
1. `train-and-predict` trains a new predictive model from the provided dataset and generates desired predictions from the supplied prediction dataset
2. `train-only` option trains a desired predictive model but does not execute a batch prediction job for the provided data set
3. `predict-only` option executes a batch prediction job against an already deployed predictive model.


Advanced users who want to control virtual environment creation, dependency installation, environment variable setup
and `pulumi` invocation, see [the advanced setup instructions](#setup-for-advanced-users).

## Architecture overview

![Guarded RAG architecture](https://s3.us-east-1.amazonaws.com/datarobot_public/drx/recipe_gifs/sap_xpa_biz_app_architecture.drawio.svg)

App Templates contain three families of complementary logic. For this template, you can [opt-in](#make-changes) to fully 
custom AI logic and a fully custom front-end or utilize DataRobot's off-the-shelf offerings:

- **AI logic**: Necessary to service AI requests, generate predictions, and manage predictive models.

  ```
  notebooks/  # Model training logic
  ```
- **App logic**: Necessary for user consumption, whether via a hosted front-end or integrating into an external consumption layer.
  ```
  frontend/  # Streamlit frontend
  ```
- **Operational logic**: Necessary to turn on all DataRobot assets.
  ```
  __main__.py  # Pulumi program for configuring DataRobot to serve and monitor AI & App logic
  infra/  # Settings for resources and assets created in DataRobot
  ```

## Why build AI Apps with DataRobot app templates?

App templates transform your AI projects from notebooks to production-ready applications. Too often, getting models into production means rewriting code, juggling credentials, and coordinating with multiple tools and teams just to make simple changes. DataRobot's composable AI apps framework eliminates these bottlenecks, letting you spend more time experimenting with your ML and app logic and less time wrestling with plumbing and deployment.

- Start building in minutes: Deploy complete AI applications instantly, then customize AI logic or front-end independently - no architectural rewrites needed.
- Keep working your way: Data scientists keep working in notebooks, developers in IDEs, and configs stay isolated - update any piece without breaking others.
- Iterate with confidence: Make changes locally and deploy with confidence - spend less time writing and troubleshooting plumbing, more time improving your app.

Each template provides an end-to-end AI architecture, from raw inputs to deployed application, while remaining highly customizable for specific business requirements.

## Make changes

### Change the data and how the model is trained

1. Edit the following notebook:
   - `notebooks/train_model.ipynb`: Handles training data ingest and preparation and model training settings.

   The last cell of the notebook is required, as it writes outputs needed for the rest of the pipeline.
2. Run the revised notebook.
3. Run `pulumi up` to update your stack with these changes.

   ```sh
   source set_env.sh  # On windows use `set_env.bat`
   pulumi up
   ```

### Change the front-end

1. Ensure you have already run `pulumi up` at least once (to provision the time series deployment).
2. Streamlit assets are in `frontend/` and can be edited. After provisioning the stack
   at least once, you can also test the front-end locally using `streamlit run app.py` from the
   `frontend/` directory (don't forget to initialize your environment using `source set_env.sh`).
3. Run `pulumi up` again to update your stack with the changes.

   ```sh
   source set_env.sh  # On windows use `set_env.bat`
   pulumi up
   ```

#### Change the language in the front-end

Optionally, you can set the application locale in `meta_template/i18n.py`, e.g. `APP_LOCALE = LanguageCode.JA`. Supported locales are Japanese and English, with English set as the default.

## Share results

1. Log into the DataRobot application.
2. Navigate to **Registry > Applications**.
3. Navigate to the application you want to share, open the actions menu, and select **Share** from the dropdown.

## Delete all provisioned resources

```sh
pulumi down
```

Then run the jupyter notebook `notebooks/delete_non_pulumi_assets.ipynb`.

## Setup for advanced users

For manual control over the setup process, adapt the following steps for MacOS/Linux to your environent:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
source set_env.sh
pulumi stack init YOUR_PROJECT_NAME
pulumi up 
```

e.g., for Windows/conda/cmd.exe the previous example would change to the following:

```sh
conda create --prefix .venv pip
conda activate .\.venv
pip install -r requirements.txt
set_env.bat
pulumi stack init YOUR_PROJECT_NAME
pulumi up 
```

For projects that will be maintained, DataRobot recommends forking the repo so upstream fixes and improvements can be merged in the future.

## Data privacy

Your data privacy is important to DataRobot. Data handling is governed by the DataRobot [Privacy Policy](https://www.datarobot.com/privacy/). Review the policy before using your own data with DataRobot.

