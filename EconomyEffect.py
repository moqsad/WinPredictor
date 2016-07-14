import csv
import pandas as pd
import numpy as nm
from pylab import*

folder = 'G:\\Google Drive\\Class file\Current\\Me\\Project300\\Data Analysis\\t20s_maleCSV\\'
# file_name = folder + teams + '.csv'

# if csv file column number changes, change this indexex according to the new csv file
decision_index = 6
toss_index = 18
winner_index = 22 #Something bad was happened for wrong indexing ................
team1_name_index = 15
team2_name_index = 16

economy_mixed_index = 3
team_name_mixed_index = 10

win = 0
loss = 0
tie = 0
team1_economy = 0
team2_economy = 0

#648
for value in range(1,505):

    global team1_economy
    global team2_economy

    filename = folder + str(value) + '.csv'
    file=open(filename, "r")
    reader = csv.reader(file)
    flag = 0
    for line in reader:
        if flag == 0:
            flag = 1
            continue
        decision=line[decision_index]
        toss=line[toss_index]
        winner=line[winner_index]
        team1_name = line[team1_name_index]
        team2_name = line[team2_name_index]
        break
    #print(decision,toss,winner)
    print(team1_name, team2_name)

    filename2 = folder + 'mixedCSV' + '.csv'
    file2=open(filename2, "r")
    reader2 = csv.reader(file2)
    flag = 0
    for line in reader2:
        if flag == 0:
            flag = 1
            continue

        if line[team_name_mixed_index] == team1_name:
            flag += 1
            print(line[economy_mixed_index] + '______________')
            team1_economy = float(line[economy_mixed_index])

        if line[team_name_mixed_index] == team2_name:
            flag += 1
            print(line[economy_mixed_index] + '______________')
            team2_economy = float(line[economy_mixed_index])

        if flag == 3:
            break

    print(team1_economy, team2_economy)
    print(winner)
    if(winner == 'tie'):
        tie = tie + 1
    elif winner == team1_name:
        if(team1_economy < team2_economy):
            win += 1
        else:
            loss += 1
    else:
        if(team1_economy > team2_economy):
            win += 1
        else:
            loss += 1

print(win,loss,tie)

figure(1, figsize=(8,8))
ax = axes([0.1,0.1,0.8,0.8])

x = (win/(win+loss+tie)) * 100
y = (loss/(win+loss+tie)) * 100
z = (tie/(win+loss+tie)) * 100
# The slices will be ordered and plotted counter-clockwise.
labels = 'Win', 'Loss', 'Tie'
fracs = [x , y , z ]
explode=(0, 0, 0)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('Effect of Economy', bbox={'facecolor':'0.8', 'pad':5})

show()

