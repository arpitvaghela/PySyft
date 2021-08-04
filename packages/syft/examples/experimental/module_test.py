import pandas as pd

class A:
    def __init__(self,n:int,data:pd.DataFrame):
        self.n = n
        self.data = data
    
    def get_n(self)->int:
        return self.n
    
    def get_data(self)->pd.DataFrame:
        return self.data