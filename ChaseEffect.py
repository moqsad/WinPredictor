import csv
import pandas as pd
import numpy as nm
from pylab import*

folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'
# file_name = folder + teams + '.csv'

# if csv file column number changes, change this indexex according to the new csv file
decision_index = 5
toss_index = 16
winner_index = 20

win = 0
loss = 0
tie = 0
#648
for value in range(1,648):
    filename = folder + str(value) + '.csv'

    file=open(filename, "r")

    decision = []
    toss = []
    winner = []
    reader = csv.reader(file)

    for line in reader:
       decision=line[decision_index]
       toss=line[toss_index]
       winner=line[winner_index]
    #print(decision,toss,winner)

    if(winner == 'tie'):
        tie = tie + 1
    elif(decision == 'bat'):
        if(toss == winner):
            loss = loss + 1
        else:
            win = win + 1
    else:
        if(toss == winner):
            win = win + 1
        else:
            loss = loss +1

#print(win,loss,tie)

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

title('Effect of batting second in result', bbox={'facecolor':'0.8', 'pad':5})

show()






