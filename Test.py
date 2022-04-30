import pandas as pd

from StatisticsTestsCovid import calculate_statistics

archivo = './casos_diagnostico_ccaa.csv'
df = pd.read_csv(archivo)

calculate_statistics(df)

arr_test = "[['MD' 493480 'CE' 3758 350.02799838470855 756.9521803489858\n  572976.6033350836 'AN' 391]]"


def calculate_statistics_test():

    assert str(calculate_statistics(df)) == arr_test

calculate_statistics_test()