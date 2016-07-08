import csv
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
from pylab import *


def listindex(total):
    if total >= 30 and total < 40:
        return 0
    elif total >= 40 and total < 50:
        return 1
    elif total >= 50 and total < 60:
        return 2
    elif total >= 60 and total < 70:
        return 3
    elif total >= 70 and total < 80:
        return 4
    elif total >= 80 and total < 90:
        return 5
    elif total >= 90 and total < 100:
        return 6
    elif total >= 100 and total < 110:
        return 7
    elif total >= 110 and total < 120:
        return 8
    elif total >= 120 and total < 130:
        return 9
    elif total >= 130 and total < 140:
        return 10
    elif total >= 140 and total < 150:
        return 11
    elif total >= 150 and total < 160:
        return 12
    elif total >= 160 and total < 170:
        return 13
    elif total >= 170 and total < 180:
        return 14
    elif total >= 180 and total < 190:
        return 15
    elif total >= 190 and total < 200:
        return 16
    elif total >= 200 and total < 210:
        return 17
    elif total >= 210 and total < 220:
        return 18
    elif total >= 220 and total < 230:
        return 19
    elif total >= 230 and total < 240:
        return 20
    elif total >= 240 and total < 250:
        return 21
    elif total >= 250 and total < 260:
        return 22
    elif total >= 260 and total < 270:
        return 23


folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'

label = ['30--', '40--', '50--', '60--', '70--', '80--', '90--', '100--', '110--', '120--', '130--',
         '140--', '150--',
         '160--', '170--', '180--', '190--', '200--', '210--', '220--', '230--','240--','250--','260--']
win = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
loss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tie = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
winpercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
losspercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#print(label)
#print(win[10])
#print(loss)
for value in range(1, 648):
    filename = folder + str(value) + '.csv'

    file = open(filename, "r")

    reader = csv.reader(file)
    #change these indices if csv is updated(0 based)
    innings_index = 6
    run_index = 15
    decision_index = 5
    toss_index = 16
    winner_index = 20

    for line in reader:
        innings = line[innings_index]
        if innings == '1st':
            run = line[run_index]

        decision = line[decision_index]
        toss = line[toss_index]
        winner = line[winner_index]

    target = int(run) + 1
    i = listindex(target)
    #print(target,i)
    if winner == 'tie':
        tie[i] = tie[i] + 1
    elif decision == 'bat':
        if toss == winner:
            loss[i] = loss[i] + 1
        else:
            win[i] = win[i] + 1
    else:
        if toss == winner:
            win[i] = win[i] + 1
        else:
            loss[i] = loss[i] + 1


            # print(winner,target,win,loss,tie)

#print(label)
#print(win)
#print(loss)

length = len(label)

for i in range(0,length):
    try:
        winpercantage[i] = (win[i]/(win[i]+loss[i]+tie[i])) * 100
    except:
        winpercantage[i] = 0

for i in range(0,length):
    try:
        losspercantage[i] = (loss[i]/(win[i]+loss[i]+tie[i])) * 100
    except:
        losspercantage[i] = 0

raw_data = {'label': label,
            'Win': winpercantage,
            'Loss': losspercantage
           }

df = pd.DataFrame(raw_data, columns=['label', 'Win', 'Loss'])

# Setting the positions and width for the bars
pos = list(range(len(df['Win'])))
width = 0.15

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# in position pos,
plt.bar(pos,
        #using df['Win'] data,
        df['Win'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='Red',
        # with label the first value in first_name
        label=df['label'][0])

plt.bar(pos,
        # using df['Win'] data,
        df['Loss'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='Blue',
        # with label the first value in first_name
        label=df['label'][1])


# Set the y axis label
ax.set_ylabel('Percantage')

# Set the chart's title
ax.set_title('Target Effect')

# Set the position of the x ticks
ax.set_xticks([p + 2.0 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['label'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Win'] + df['Loss'])])

# Adding the legend and showing the plot
plt.legend(['Win','Loss'], loc='upper left')
plt.grid()
plt.show()







