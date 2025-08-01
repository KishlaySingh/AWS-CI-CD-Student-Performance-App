from pyclbr import Class
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model = load_object("artifacts\model.pkl")
            preprocessor = load_object("artifacts\preprocessor.pkl")
            features = preprocessor.transform(features)
            prediction = model.predict(features)
            return prediction
        
        except Exception as e:
            logging.error("Error occurred while making prediction")
            raise CustomException(e, sys)

class CustomData:
    '''
    Responsible for mapping all the data points we receive in the front end to the back end.
    '''
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: int,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int) -> None:
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict, index=[0])
        except Exception as e:
            raise CustomException(e, sys)
