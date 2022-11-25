import pandas as pd

class Btree:

    def create_data_frame(self, file_path):
        return pd.read_csv(file_path)
