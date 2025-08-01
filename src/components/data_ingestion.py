# # src/components/data_ingestion.py
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

# method to initiate data ingestion -> reading the dataset from source like mongodb or from the csv dataset
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or Component")
        try:
            # Read the dataset from the csv file
            # You can change the path to your dataset file OR You can use mongoDB or any other source to read the dataset
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the Dataset from the Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated...")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed...")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except:
            raise CustomException("Error occurred during data ingestion", sys) from None

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path=train_data, test_path=test_data)

    model_trainer = ModelTrainer()
    # print(model_trainer.initiate_model_trainer(train_arr,test_arr))
    print("Best accuracy of the model is : ",model_trainer.initiate_model_trainer(train_array=train_arr, test_array=test_arr, preprocessor_path=data_transformation.data_transformation_config.preprocessor_obj_file_path))



    print(f"Train Data Path: {train_data}")
    print(f"Test Data Path: {test_data}")


