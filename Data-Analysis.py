import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
file1=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\deliveries.csv")
file2=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\matches.csv")
script_dir=os.path.dirname(os.path.abspath(__file__))
save=os.path.join(script_dir,"Graphs_And_Charts")
if not os.path.exists(save):os.makedirs(save)
def Data_Assessment():
    print(file1.dtypes)
    print(file2.dtypes)
    print(file1.head())
    print(file2.head())
    print(file1.isnull().sum()) #Null values present in player_dismissed,dismissal_kind and fielder.
    print(file2.isnull().sum()) #Null values present in city,winner,umpire1,umpire2,umpire3.
    print(file1[file1.duplicated()]) #No Major duplicates out of more than 20000 matches few coincidences can be neglected.
    print(file2[file1.duplicated()]) #No Duplicates at all.
def Match_Analysis():
    plt.figure(figsize=(10,8))
    sns.set_style("whitegrid")
    lock=file2["winner"].value_counts().head(14).index
    sns.countplot(data=file2[file2["winner"].isin(lock)],y="winner",hue="winner",order=lock,palette="viridis",legend=False)
    plt.title("IPL Teams That Have Won Most Of The Matches")
    plt.xlabel("No. Of Matches Won")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10,8))
    sns.set_style("whitegrid")
    lock1=file2["venue"].value_counts().index
    sns.countplot(data=file2[file2["venue"].isin(lock1)],y="venue",order=lock1,color="darkcyan")
    plt.title("Stadium That Have Hosted Highest No. Of Matches")
    plt.xlabel("No. Of Matches Played")
    plt.ylabel("Stadium")
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10,8))
    sns.set_style("whitegrid")
    top7=file2["player_of_match"].value_counts().head(7).index
    sns.countplot(data=file2[file2["player_of_match"].isin(top7)],x="player_of_match",order=top7,color="yellow")
    plt.title("Top 7 Players With Highest No. Of Player Of The Match Titles")
    plt.ylabel("No. Of Times Player Of The Match Awarded")
    plt.xlabel("Player")
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10,8))
    sns.set_style("whitegrid")
    file2["toss_match_same"] = file2["toss_winner"] == file2["winner"]
    count=file2["toss_winner"].value_counts().head(14).index
    sns.countplot(data=file2[file2["toss_winner"].isin(count)],y="toss_winner",order=count,hue="toss_match_same",palette="mako")
    plt.title("Toss Winner - Match Winner Connection Chart")
    plt.xlabel("No. Of Matches")
    plt.ylabel("Team")
    plt.legend(bbox_to_anchor=(1,0.5),title="Won Both Match And Toss ?",loc="upper left")
    plt.tight_layout()
    plt.show()
    count1=file2["Season"].value_counts().index
    sns.countplot(data=file2[file2["Season"].isin(count1)],y="Season",order=count1,color="turquoise")
    plt.title("IPL Seasons With Most Matches")
    plt.xlabel("No. Of Matches")
    plt.ylabel("IPL Season")
    plt.tight_layout()
    plt.show()


# Data_Assessment()
Match_Analysis()