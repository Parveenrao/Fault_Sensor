import os
import sys
from dataclasses import dataclass

from src.constants import *
from src.exception import CustomException
from src.logger import logging
from src.utlis import export_collection_as_dataframe

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts' , 'train.csv')
    raw_data_path : str = os.path.join('artifacts' , 'data.csv')
    test_data_path : str = os.path.join('artifacts' , 'test.csv')