import csv
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
from pylab import *

def listindex(rate):
    if rate>=0 and rate<4.0:
        return 0
    elif rate>= 4.0 and rate<5.0:
        return 1
    elif rate>= 5.0 and rate< 6.0:
        return 2
    elif rate>= 6.0 and rate< 6.5:
        return 3
    elif rate>= 6.5 and rate< 7.0:
        return 4
    elif rate>= 7.0 and rate< 8.0:
        return 5
    elif rate>= 8.0 and rate< 9.0:
        return 6
    elif rate>= 9.0 and rate< 10.0:
        return 7
    else:
        return 8


folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'

label = ['0-4', '4-5', '5-6', '6-6.5', '6.5-7', '7-8', '8-9', '9-10', '10--']
win = [0, 0, 0, 0, 0, 0, 0, 0, 0]
loss = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tie = [0, 0, 0, 0, 0, 0, 0, 0, 0]
winpercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0]
losspercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for value in range(1, 648):

    filename = folder + str(value) + '.csv'

    file = open(filename, "r")

    reader = csv.reader(file)

    #change these indices if csv is updated( 0 based)
    ball_index = 1
    innings_index = 6
    run_index = 15
    decision_index = 5
    toss_index = 16
    winner_index = 20

    over = 20.0
    flag = 0
    for line in reader:
        ball = line[ball_index]
        innings = line[innings_index]
        if flag == 1:
            #print(ball)
            Ball = float(ball)
            if innings != '1st' or Ball>=over:
                break

            run = line[run_index]
        flag = 1
        decision = line[decision_index]
        toss = line[toss_index]
        winner = line[winner_index]


    #print(Run)
    Run = int(run)
    runrate = Run/over

    #print(runrate)

    i = listindex(runrate)
    #print(runrate,i)
    if winner == 'tie':
        tie[i] = tie[i] + 1
    elif decision == 'bat':
        if toss == winner:
            win[i] = win[i] + 1
        else:
            loss[i] = loss[i] + 1
    else:
        if toss == winner:
            loss[i] = loss[i] + 1
        else:
            win[i] = win[i] + 1

print(label)
print(win)
print(loss)

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
        color='Orange',
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
ax.set_xlabel('Run Rate')

# Set the chart's title
ax.set_title(str(int(over))+'th Over Run Rate Effect')

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





