#importing Modules0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading Data
matches= pd.read_csv(r"C:\Users\Ahmed\Downloads\Indian Premier League\matches.csv")
print(matches.head(20))
deliveries = pd.read_csv(r"C:\Users\Ahmed\Downloads\Indian Premier League\deliveries.csv")
deliveries.rename(columns={'match_id':'id'},inplace=True)

#Droping Duplicats and Null Values
deliveries=deliveries.drop_duplicates()
deliveries=deliveries.dropna()
print(deliveries.shape)
print(matches.shape)

Null_Values = matches.isnull().sum()

matches=matches.drop('umpire3',axis=1)
matches=matches.drop_duplicates()
print(matches.shape)

#Filling Necessary columns
matches=matches.fillna('Unknown')
matches=matches.dropna()
print(matches.shape)


# Plotting Highest Winning Teams
plt.figure(figsize=(18,10))
sns.set_theme(style="whitegrid")
g=sns.countplot(x=matches['winner'],order=matches['winner'].value_counts(ascending=False).index,data=matches,palette='rocket')
abs_values = matches['winner'].value_counts().values
g.bar_label(container=g.containers[0],labels=abs_values)
g.set_title('Most Winning Teams')
g.set_ylabel('Number of wins')
plt.xticks(rotation = 90)
plt.show()

### Plotting Highest Winning Teams With Toss Decision

plt.figure(figsize=(18,10))
sns.set_theme(style="whitegrid")
g=sns.countplot(x=matches['winner'],order=matches['winner'].value_counts(ascending=False).index,
                data=matches,palette='rocket',hue='toss_decision')
abs_values = matches['winner'].value_counts().values
g.bar_label(container=g.containers[0],labels=abs_values)
g.set_title('Most Winning Teams With Toss Decision ')
g.set_ylabel('Number of wins')
plt.xticks(rotation = 90)
g.set_yticks(np.arange(0,120,10))

plt.show()

# Best 30 Players

best_players = matches.player_of_match.value_counts()[:30]
print(best_players)
plt.figure(figsize=(18,10))

g=sns.barplot(x=best_players,y=best_players.index,palette='ch:start=.2,rot=-.3')
g.set_xlim([0,25])
g.set_xlabel('Number of Matches')
g.set_ylabel('Man of the Match')
g.set_title('Best 30 Players')
plt.show()

# Winnings by Runs comparing between Bat or Bowl were first
matches['wins_by_runs']=np.where(matches['win_by_runs']>0,'Bat first','Bowl first')
print(matches['wins_by_runs'])
win=matches.wins_by_runs.value_counts()
labels=np.array(win.index)
sizes = win.values
colors=['#194A8D','#79fb98']
plt.figure(figsize=(10,8))
plt.suptitle('Winnings by Runs comparing between Bat or Bowl')

plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90,colors=colors)
plt.axis('equal')
plt.show()

#Highest Citites were Matches Played in
plt.figure(figsize=(18,10))
sns.set_theme(style="whitegrid")
g=sns.countplot(x=matches['city'],order=matches['city'].value_counts(ascending=False).index,data=matches)
abs_values = matches['city'].value_counts().values


g.bar_label(container=g.containers[0],labels=abs_values)
g.set_title('#Highest Citites were Matches Played in')
g.set_ylabel('Number of Matches')
plt.xticks(rotation = 90)
plt.show()


# Count of wins by Toss Descision


n=matches.groupby('toss_decision').agg(winner=('winner','count')).sort_values('winner',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='pie',title='Precentage of wins by Toss Descision',subplots=True,autopct='%1.1f%%',startangle=90)
plt.show()

#Teams Highest Runs
n=matches.groupby('winner').agg(win_by_runs=('win_by_runs','sum')).sort_values('win_by_runs',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Teams who have Highest Runs',color='navy',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()
#Top Bats Man Runs
n=deliveries.groupby('batsman').agg(total_runs=('total_runs','sum')).sort_values('total_runs',ascending=False).head(20)
g=n.plot(kind='bar',title=' Top Bats Men Runs',color='seagreen',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()
#Top Non Strikers Runs
n=deliveries.groupby('non_striker').agg(total_runs=('total_runs','sum')).sort_values('total_runs',ascending=False).head(20)
g=n.plot(kind='bar',title=' Top Non Strikers Runs',color='maroon',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()
#Top bowlers Runs
n=deliveries.groupby('bowler').agg(total_runs00=('total_runs','sum')).sort_values('total_runs',ascending=False).head(20)
g=n.plot(kind='bar',title=' Top Bowlers Runs',color='black',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()
0