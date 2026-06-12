import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
file1=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\deliveries.csv")
file2=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\matches.csv")
file3=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\most_runs_average_strikerate.csv")
file4=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\teamwise_home_and_away.csv")
script_dir=os.path.dirname(os.path.abspath(__file__))
save=os.path.join(script_dir,"Graphs_And_Charts")
if not os.path.exists(save):os.makedirs(save)
def Data_Assessment():
    print(file1.dtypes)
    print(file2.dtypes)
    print(file3.dtypes)
    print(file4.dtypes)
    print(file1.head())
    print(file2.head())
    print(file3.head())
    print(file4.head())
    print(file1.isnull().sum()) #Null values present in player_dismissed,dismissal_kind and fielder.
    print(file2.isnull().sum()) #Null values present in city,winner,umpire1,umpire2,umpire3.
    print(file3.isnull().sum()) #Null values present in average.
    print(file4.isnull().sum()) #No Null values present.
Data_Assessment()
