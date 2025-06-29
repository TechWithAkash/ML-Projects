# # src/utils.py
import os
import sys
import pandas as pd
import numpy as np
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    """
    Saves an object to a file using joblib.
    
    Parameters:
    - file_path (str): The path where the object will be saved.
    - obj: The object to be saved.
    
    Raises:
    - CustomException: If there is an error during saving the object.
    """
    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        
        logging.info(f"Saving object at {file_path}")

        # Using dill to serialize the object
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Object saved successfully at {file_path}")

     
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        logging.info("Evaluating models...")
        # Initialize a dictionary to hold the evaluation reports
        reports = {}
        for i in range (len(list(models))):

            logging.info(f"Evaluating model: {list(models.keys())[i]}")
            model = list(models.values())[i]

            logging.info(f"Setting parameters for model: {list(models.keys())[i]}")
            # Setting the parameters for the model
            para = params[list(models.keys())[i]]

            gs = GridSearchCV(
                model,para,
                cv=3,
                n_jobs=-1,
                verbose=2,
                refit=True,
                scoring='r2'
            )

            logging.info(f"Fitting model with GridSearchCV: {list(models.keys())[i]}")
            # Fitting the model with GridSearchCV
            model = gs.fit(X_train,y_train)


            logging.info(f"Fitting model: {list(models.keys())[i]}")
            model.fit(X_train,y_train)

            logging.info(f"Predicting with model: {list(models.keys())[i]}")
            # Predicting on training and testing data
            y_train_pred = model.predict(X_train)


            logging.info(f"Predicting with model on test data: {list(models.keys())[i]}")
            # Predicting on test data
            y_test_pred = model.predict(X_test)


            logging.info(f"Calculating scores for model: {list(models.keys())[i]}")
            # Calculating the score for training and testing data
            train_model_score = r2_score(y_train,y_train_pred)

            logging.info(f"Calculating test score for model: {list(models.keys())[i]}")
            test_model_score = r2_score(y_test,y_test_pred)

            # Logging the scores
            logging.info(f"Model: {list(models.keys())[i]}, Train Score: {train_model_score}, Test Score: {test_model_score}")

            # Storing the scores in the reports dictionary
            reports[list(models.keys())[i]] = test_model_score
            # reports[list(models.keys())[i]] = {
            #     "train_score": train_model_score,
            #     "test_score": test_model_score
            # }
        logging.info(f"Model evaluation reports: {reports}")
        return reports
    



    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):

    try:
        """
        Loads an object from a file using dill.
        Parameters:
        - file_path (str): The path from which the object will be loaded.
        Returns:
        - obj: The loaded object.
        """
        logging.info(f"Loading object from {file_path}")
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        logging.info(f"Object loaded successfully from {file_path}")
        return obj
    except Exception as e:
        logging.error(f"Error loading object from {file_path}: {e}")
        raise CustomException(e, sys)
    



   
    """
    Evaluates multiple regression models and returns their performance metrics.
    
    Parameters:
    - X_train: Training feature set.
    - y_train: Training target values.
    - X_test: Testing feature set.
    - y_test: Testing target values.
    - models (dict): Dictionary of model names and their instances.
    
    Returns:
    - model_report (dict): Dictionary containing model names and their R2 scores.
    """
    model_report = {}

    for model_name, model in models.items():
        try:
            # Fit the model
            model.fit(X_train, y_train)
            # Predict on the test set
            y_pred = model.predict(X_test)
            # Calculate R2 score
            r2 = r2_score(y_test, y_pred)
            model_report[model_name] = r2
        except Exception as e:
            logging.error(f"Error evaluating {model_name}: {e}")
            model_report[model_name] = None

    return model_report