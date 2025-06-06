import mlflow
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
import yaml

# Load parameters from params.yaml
params = yaml.safe_load(open("params.yaml"))["train"]

def evaluate(data_path,model_path):
    data=pd.read_csv(data_path)
    X = data.drop(columns=["Outcome"])
    y = data["Outcome"]

    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    ## load the model from the disk
    model=pickle.load(open(model_path,'rb'))

    # prediction of model
    y_pred=model.predict(X)
    accuracy=accuracy_score(y,y_pred)
    
    ## log metrics to MLFLOW
    mlflow.log_metric("accuracy",accuracy)
    print(f"Model accuracy:{accuracy}")

if __name__=="__main__":
    evaluate(params["data"],params["model"])
