import csv
import pandas as pd
import numpy as nm
from pylab import*

folder = 'G:\\Google Drive\\Class file\Current\\Me\\Project300\\Data Analysis\\t20s_maleCSV\\'
# file_name = folder + teams + '.csv'

team_name_list = []

wicket_nice_list = []
over_korce_list = []
run_dice_list = []

wicket_haraice_list = []
over_khelce_list = []
run_korce_list = []

batting_avg_list = []
bowling_avg_list = []
bowling_economy_list = []
bowling_strike_rate_list = []
no_of_match_list = []
winning_percent_list = []
lossing_percent_list = []

max_value = 0
team1_pos = 0
team2_pos = 0

decision = '0'
toss = '0'
winner = '0'

ball_index = 1
innings_index = 8
wicket_index = 19
run_index = 17

decision_index = 6
toss_index = 18
winner_index = 22

extras_index = 7
bowling_extras_index = 4

team1_name_index = 15
team2_name_index = 16

def position_find( reader ):

    global max_value
    global team1_pos
    global team2_pos

    flag = 0
    for line in reader:
        if flag == 0:
            flag = 1
            continue

        team1_name = line[team1_name_index]
        team2_name = line[team2_name_index]

        break_flag = 0
        for i in range(0, max_value):
            if team1_name == team_name_list[i]:
                team1_pos = i
                break_flag = 1
                break

        if break_flag == 0:
            team1_pos = max_value
            team_name_list.append(team1_name)
            max_value += 1

        break_flag = 0
        for i in range(0, max_value):
            if team2_name == team_name_list[i]:
                team2_pos = i
                break_flag = 1
                break

        if break_flag == 0:
            team2_pos = max_value
            team_name_list.append(team2_name)
            max_value += 1
    return


for i in range(22):
    wicket_nice_list.append(0)
    over_korce_list.append(0.0)
    run_dice_list.append(0)

    wicket_haraice_list.append(0)
    over_khelce_list.append(0.0)
    run_korce_list.append(0)

    batting_avg_list.append(0.0)
    bowling_avg_list.append(0.0)
    bowling_economy_list.append(0.0)
    bowling_strike_rate_list.append(0.0)
    no_of_match_list.append(0)
    winning_percent_list.append(0.0)
    lossing_percent_list.append(0.0)

for value in range(1,505):
    filename = folder + str(value) + '.csv'
    file = open(filename, "r")
    reader = csv.reader(file)

    position_find(reader)
    print(team1_pos, team2_pos)

    run1 = 0
    run2 = 0
    wicket1 = 0
    wicket2 = 0
    over1 = 0.0
    over2 = 0.0
    extras1 = 0
    extras2 = 0
    bowling_extras1 = 0
    bowling_extras2 = 0

    flag = 0
    file = open(filename, "r")
    reader = csv.reader(file)
    for line in reader:
        if flag == 0:
            flag = 1
            continue

        innings = line[innings_index]

        if innings == '1st':
            run1 = int(line[run_index])
            over1 = float(line[ball_index])
            wicket1 = int(line[wicket_index])
            extras1 = int(line[extras_index])
            bowling_extras1 = int(line[bowling_extras_index])
        else:
            run2 = int(line[run_index])
            over2 = float(line[ball_index])
            wicket2 = int(line[wicket_index])
            extras2 = int(line[extras_index])
            bowling_extras2 = int(line[bowling_extras_index])

    #print(run1, wicket1, over1, extras1, bowling_extras1)
    #print(run2, wicket2, over2, extras2, bowling_extras2)

    flag = 0
    file = open(filename, "r")
    reader = csv.reader(file)
    for line in reader:
        if flag == 0:
            flag = 1
            continue
        decision = line[decision_index]
        toss = line[toss_index]
        winner = line[winner_index]
        break
    #print(decision, toss, winner)

    if decision == 'bat':
        if toss == team_name_list[team1_pos]:

            wicket_nice_list[team1_pos] += wicket2
            over_korce_list[team1_pos] += over2
            run_dice_list[team1_pos] += run2 - (extras2 - bowling_extras2)
            wicket_haraice_list[team1_pos] += wicket1
            over_khelce_list[team1_pos] += over1
            run_korce_list[team1_pos] += run1 - extras1

            wicket_nice_list[team2_pos] += wicket1
            over_korce_list[team2_pos] += over1
            run_dice_list[team2_pos] += run1 - (extras1 - bowling_extras1)
            wicket_haraice_list[team2_pos] += wicket2
            over_khelce_list[team2_pos] += over2
            run_korce_list[team2_pos] += run2 - extras2

        else:
            wicket_nice_list[team2_pos] += wicket2
            over_korce_list[team2_pos] += over2
            run_dice_list[team2_pos] += run2 - (extras2 - bowling_extras2)
            wicket_haraice_list[team2_pos] += wicket1
            over_khelce_list[team2_pos] += over1
            run_korce_list[team2_pos] += run1 - extras1

            wicket_nice_list[team1_pos] += wicket1
            over_korce_list[team1_pos] += over1
            run_dice_list[team1_pos] += run1 - (extras1 - bowling_extras1)
            wicket_haraice_list[team1_pos] += wicket2
            over_khelce_list[team1_pos] += over2
            run_korce_list[team1_pos] += run2 - extras2
    else:

        if toss == team_name_list[team1_pos]:  #Something wrong was happened not equal sign...........
            wicket_nice_list[team2_pos] += wicket2
            over_korce_list[team2_pos] += over2
            run_dice_list[team2_pos] += run2 - (extras2 - bowling_extras2)
            wicket_haraice_list[team2_pos] += wicket1
            over_khelce_list[team2_pos] += over1
            run_korce_list[team2_pos] += run1 - extras1

            wicket_nice_list[team1_pos] += wicket1
            over_korce_list[team1_pos] += over1
            run_dice_list[team1_pos] += run1 - (extras1 - bowling_extras1)
            wicket_haraice_list[team1_pos] += wicket2
            over_khelce_list[team1_pos] += over2
            run_korce_list[team1_pos] += run2 - extras2
        else:
            wicket_nice_list[team1_pos] += wicket2
            over_korce_list[team1_pos] += over2
            run_dice_list[team1_pos] += run2 - (extras2 - bowling_extras2)
            wicket_haraice_list[team1_pos] += wicket1
            over_khelce_list[team1_pos] += over1
            run_korce_list[team1_pos] += run1 - extras1

            wicket_nice_list[team2_pos] += wicket1
            over_korce_list[team2_pos] += over1
            run_dice_list[team2_pos] += run1 - (extras1 - bowling_extras1)
            wicket_haraice_list[team2_pos] += wicket2
            over_khelce_list[team2_pos] += over2
            run_korce_list[team2_pos] += run2 - extras2

    print(value, team_name_list[team1_pos], team_name_list[team2_pos])

    no_of_match_list[team1_pos] += 1
    no_of_match_list[team2_pos] += 1

    if winner == 'tie':
        print('tie')
        winning_percent_list[team1_pos] += 1
        lossing_percent_list[team1_pos] += 1
        winning_percent_list[team2_pos] += 1
        lossing_percent_list[team2_pos] += 1
    elif winner == team_name_list[team1_pos]:
        winning_percent_list[team1_pos] += 1
        lossing_percent_list[team2_pos] += 1
    else:
        lossing_percent_list[team1_pos] += 1
        winning_percent_list[team2_pos] += 1


for j in range(22):
    winning_percent_list[j] = winning_percent_list[j] / (winning_percent_list[j] + lossing_percent_list[j])
    batting_avg_list[j] = run_korce_list[j] / wicket_haraice_list[j]
    bowling_avg_list[j] = run_dice_list[j] / wicket_nice_list[j]
    bowling_economy_list[j] = run_dice_list[j] / over_korce_list[j]
    bowling_strike_rate_list[j] = over_korce_list[j] * 6.0 / wicket_nice_list[j]

# Construction of a DataFrame
data_set = pd.DataFrame({
    'Team Name': pd.Series(team_name_list),
    'Wicket Nice': pd.Series(wicket_nice_list),
    'Over Korce': pd.Series(over_korce_list),
    'Run Dice': pd.Series(run_dice_list),
    'Wicket Haraice': pd.Series(wicket_haraice_list),
    'Over Khelce': pd.Series(over_khelce_list),
    'Run Korce': pd.Series(run_korce_list),
    'Batting Average': pd.Series(batting_avg_list),
    'Bowling Average': pd.Series(bowling_avg_list),
    'Bowling Economy': pd.Series(bowling_economy_list),
    'Bowling Strike Rate': pd.Series(bowling_strike_rate_list),
    'Winning Percentage': pd.Series(winning_percent_list),
    'No Of Matches': pd.Series(no_of_match_list)
})

# print(data_set)
folder = 'G:\\Google Drive\\Class file\\Current\\Me\\Project300\\Data Analysis\\t20s_maleCSV\\'
file_name = folder + 'mixedCSV' + '.csv'
data_set.to_csv(file_name, encoding='utf-8')

print(team_name_list)
print(wicket_nice_list)
print(over_korce_list)
print(run_dice_list)
print(wicket_haraice_list)
print(over_khelce_list)
print(run_korce_list)
print(max_value, team1_pos, team2_pos)
print(run1, wicket1, over1, extras1, bowling_extras1)
print(run2, wicket2, over2, extras2, bowling_extras2)