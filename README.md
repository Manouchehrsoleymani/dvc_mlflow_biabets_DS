# dvc_mlflow_biabets_DS
This is an Practical Repository for learning Mlops and machine learning alogorithms such as dvc,mlflow,Diabets dataset, Macheine learning, Random Forest.
if i want to descibe the tools that i used in this project includes:

# DVC: (Data Version Control): 
> As the name calls, this is a tools to control Data-set versioning in our project , it's simple to work with it , and the command as the same as Git. 

> ## To Install DVC:

``` pip install dvc ```

> ## To initilize DVC:

``` dvc init ```
> #### it create a dvc temp folder next to your project and tries to keep your data-set versions in your local storage. 

> ## To Determin Data file
``` dvc add [DATA=SET FILE NAME] ```
> #### it creates a files next to you data-set file with dvc extention. and the content of the file is hash of data-set content, size, path, ...
> when you change your dataset , this file will change too, and the versions of data-sets file (the history) keep in dvc folder that you create with __dvc init__ command
# Dagshub
> Dagshub servs a service as the same as Git specially for AI project and keeps your Code,Data and your Experiments data(mlflow experiments such as metrics, parameters,logs, tags,...)
you have to create a repository like Git in dasgshub and it helps you the next step, and what commands you need to continue.

# Mlflow 
To manage the workflow of training Model in machine learning algorithms. it Store params, metrics, model registration, Model Artifacts, comparing Model metris with different params, to evaluate Models.

- Installing MLflow.

- Starting a local MLflow Tracking Server.

- Logging and registering a model with MLflow.

- Loading a logged model for inference using MLflo

- Viewing the experiment results in the MLflow UI.

# Diabets Data-Set

Data-Set includes some Columns such as __Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome__

# To Run the scripts:
``` 
- python -m venv .venv
- source .venv/bin/activate
- pip install -U pip
- pip install -r requirements.txt
- python src/preprocessing.py
- python src/train.py
- pythin src/evaluate.py
```
