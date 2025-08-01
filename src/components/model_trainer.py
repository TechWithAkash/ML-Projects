# # src/components/model_trainer.py
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import save_object, evaluate_models

from src.exception import CustomException
from src.logger import logging

@dataclass
class ModelTrainerConfig:
    trained_mode_file_path: str = os.path.join(
        "artifacts","trained_model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):
        try:
            logging.info("Splitting training and testing data")

            X_train,X_test,y_train,y_test = (
                train_array[:,:-1],
                test_array[:,:-1],
                train_array[:,-1],
                test_array[:,-1]
            )

            models = {
                "RandomFores Regressor": RandomForestRegressor(),
                "DecisionTree Regressor": DecisionTreeRegressor(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor ": XGBRegressor(),
                "CatBoosting Classifier": CatBoostClassifier(verbose=False),
                "GradientBoosting Regressor": GradientBoostingRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            logging.info("Intiating the Model Hyperparameter Tuning...")
            params = {
                "RandomFores Regressor": {
                    "n_estimators": [8,12,32,64,128,256],
                    "max_depth": [10, 20]
                },
                "DecisionTree Regressor": {
                    "max_depth": [10, 20],
                    "min_samples_split": [2, 5],
                    'criterion': ['squared_error', 'absolute_error']
                },
                "K-Neighbors Regressor": {
                    "n_neighbors": [3, 5, 7]
                },
                "Linear Regression": {},
                "XGBRegressor ": {
                    "n_estimators": [100, 200],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 5, 7]
                },
                "CatBoosting Classifier": {
                    "iterations": [100, 200],
                    "depth": [6, 8]
                },
                "GradientBoosting Regressor": {
                    "n_estimators": [100, 200],
                    "learning_rate": [0.01, 0.1, 0.2,],
                },
                "AdaBoost Regressor": {
                    "n_estimators": [50, 100],
                    "learning_rate": [0.01, 0.1, 0.2]
                }
            }

            model_report:dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                params=params,
            )

            # TO get the best model score from the model report
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

            if best_model_score < 0.6:
                raise CustomException("No best model found with sufficient score")
            logging.info("Best model found, on both training and testing data...")


            # Saving the best model
            save_object(
                file_path=self.model_trainer_config.trained_mode_file_path,
                obj=best_model
            )

            logging.info(f"Model saved at {self.model_trainer_config.trained_mode_file_path}")

            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test, predicted)

            logging.info(f"R2 Score of the best model: {r2}")
            return r2

        except Exception as e:
            raise CustomException(e, sys)

