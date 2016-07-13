import csv
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
from pylab import *

folder = 'G:\\Google Drive\\Class file\Current\\Me\\Project300\\Data Analysis\\t20s_maleCSV\\'

for loop in range(1, 21):

    label = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    losspercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    winpercantage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tie = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    loss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    win = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    cnt = 0
    for value in range(1, 505):

        filename = folder + str(value) + '.csv'

        file = open(filename, "r")

        reader = csv.reader(file)

        #change these indices if csv is updated( 0 based)
        ball_index = 1
        innings_index = 8
        wicket_index = 19
        decision_index = 6
        toss_index = 18
        winner_index = 22

        over = float(loop) - 1.0 + 0.6
        flag = 0
        second_innings = 0
        for line in reader:
            ball = line[ball_index]
            innings = line[innings_index]

            if flag == 1:
                Ball_ = float(ball)
                if Ball_>=over and innings == '2nd':
                    second_innings = 1
                    wicket = line[wicket_index]
                    decision = line[decision_index]
                    toss = line[toss_index]
                    winner = line[winner_index]
                    break
            flag = 1

        if second_innings == 1:
            #print(Run)
            Wicket = int(wicket)

            #print(runrate)

            #print(runrate,i)
            cnt = cnt + 1
            #print(cnt, value, wicket)
            #print(win)
            #print(loss)
            #print(tie)

            if winner == 'tie':
                print(value, 'tie')
                tie[Wicket] = tie[Wicket] + 1
            elif decision == 'bat':
                if toss != winner:
                    win[Wicket] = win[Wicket] + 1
                else:
                    loss[Wicket] = loss[Wicket] + 1
            else:
                if toss != winner:
                    loss[Wicket] = loss[Wicket] + 1
                else:
                    win[Wicket] = win[Wicket] + 1

    #print(cnt)
    #print(label)
    #print(win)
    #print(loss)
    #print(tie)

    length = len(label)

    for i in range(0,length):
        try:
            winpercantage[i] = ((win[i] + tie[i])/(win[i]+loss[i]+tie[i])) * 100
        except:
            winpercantage[i] = 0

    for i in range(0,length):
        try:
            losspercantage[i] = ((loss[i] + tie[i])/(win[i]+loss[i]+tie[i])) * 100
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
            # using df['Loss'] data,
            df['Loss'],
            # of width
            width,
            # with alpha 0.5
            alpha=0.5,
            # with color
            color='Blue',
            # with label the second value in first_name
            label=df['label'][1])


    # Set the y axis label
    ax.set_ylabel('Percantage')
    ax.set_xlabel('Wicket')

    # Set the chart's title
    ax.set_title(str(loop)+'th Over Wicket Effect(2nd Innings)')

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
    plt.savefig(str(loop) + 'th Over')
    plt.close(fig)