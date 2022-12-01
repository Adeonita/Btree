import pandas as pd
from math import floor 

class Btree:
    order = 0
    minRegisterPerPage = 0

    def __init__ (self, order):
        if order <= 0:
            raise Exception("A ordem da árvore precisa ser maior que zero")
        
        self.order = order
        self.minRegisterPerPage = self.min_register_per_page(self, order)

    def min_register_per_page(self, order):
        if not self.is_par(self, order):
            return "A funcionalidade para arvores ímpares não está implementada"
            return floor(order)
        
        return order / 2

    def is_par(self, number):
        return number % 2 == 0
 
    def create_data_frame(self, file_path):
        return pd.read_csv(file_path)

    def insert(self, key):        
        #como criar as páginas ?
        return