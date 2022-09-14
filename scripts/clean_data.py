import pandas as pd
import numpy as np
import logging
import string

logging.basicConfig(filename='./logfile.log', filemode='a',
                    encoding='utf-8', level=logging.DEBUG)


class dataCleaning:
    ###############################################################################
    # data cleaning
    ################################################################################

    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object with the passed DataFrame Data
            Parameters
        """
        self.df = df

    def clean_text(self, col):
        self.df[col] = self.df[col].astype(str)
        self.df[col] = self.df[col].apply(lambda x: x.lower())
        self.df[col] = self.df[col].apply(lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
        return self.df

    def convert_to_datetime(self, col)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df[col] = pd.to_datetime(self.df['created_at'])
        return self.df
    

