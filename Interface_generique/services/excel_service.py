import pandas as pd


class ExcelService:

    def load(self, file):

        return pd.read_excel(file)

    def save(self, df, file):

        df.to_excel(file, index=False )