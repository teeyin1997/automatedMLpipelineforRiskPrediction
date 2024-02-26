# Automatic ML Pipeline Automation

## Method 1: Using Virtual Environment

1. **Create a Virtual Environment:**
`python -m venv env`
2. **Activate the Virtual Environment:**
`.\env\Scripts\activate`
3. **Install Requirements:**
`pip install -r requirements.txt `
4. **Run the Project:**
`python run_project.py`


5. **Access the Deployment UI:**
Open and run `deployment/run_deployment.ipynb`.

6. **Monitor the Application:**
Open and run `monitor/run_monitor_ui.ipynb`.

7. **Automatic Retraining Pipeline Activation:**
Run the following notebooks:
- `pipeline/stage1_alert.ipynb`
- `pipeline/stage2_trigger_pipeline.ipynb`
- `pipeline/stage3_validation.ipynb`

## Method 2: Run with your own Jupyter Environment

1. **Manually open and run the following Jupyter notebooks at your notebook environment:**
- `deployment/run_deployment.ipynb`
- `experiment/experiment.ipynb` (Do not run until you want to trigger retraining criteria)
- `pipeline/stage1_alert.ipynb`
- `pipeline/stage2_trigger_pipeline.ipynb`
- `pipeline/stage3_validation.ipynb`
- `monitor/run_monitor_ui.ipynb`

## Project Description

This project aims to automate various aspects of a machine learning pipeline, including model deployment, monitoring, retraining, and performance evaluation.

## File and Folder Structure

1. **database:**
Stores datasets (`loan.csv`, `production_df.csv`, and `sampled_df.csv`).

2. **deployment:**
Contains code for running the deployment UI, production model, and performance summaries.

3. **experiment:**
Contains scripts to trigger the retraining criteria.

4. **metabase:**
Stores trained models, performance logs, and model training notebooks (with data selection, feature engineering, EDA, etc.).

5. **monitor:**
Contains code to run the monitoring UI.

6. **pipeline:**
Stores notebooks for concurrent pipelines.


