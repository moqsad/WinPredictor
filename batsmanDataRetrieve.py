import  yaml
import pandas as pd
import numpy as np

value = 0
for num in range(211028,990000):
    try:
        with open('D:\\STUDY\\3.2\\Project 300\\T20_male\\' + str(num) + '.yaml') as fileName:
            data = yaml.load(fileName)
            fileName.close()

            retrieveData = 0

            try:
                result = data['info']['outcome']['winner']
                result_margin = data['info']['outcome']['by']
                retrieveData = 1
            except:
                result = data['info']['outcome']['result']
                try:
                    result_margin = data['info']['outcome']['bowl_out']
                    retrieveData = 1
                except:
                    try:
                        result_margin = data['info']['outcome']['eliminator']
                        retrieveData = 1
                    except:
                        retrieveData = 0

            if retrieveData == 0:
                print(num, value + 1)

            if retrieveData == 1:
                dates = data['info']['dates'][0]
                team1 = data['innings'][0]['1st innings']['team']
                team2 = data['innings'][1]['2nd innings']['team']
                #print(str(dates))
                #print(team1,team2)

                firstInningsDeliveryData = data['innings'][0]['1st innings']['deliveries']
                secondInningsDeliveryData = data['innings'][1]['2nd innings']['deliveries']

                team_list, name_list, ball_list, run_list, strikerate_list, four_list, six_list, status_list, date_list = \
                    [[], [], [], [], [], [], [], [], []]

                for k in firstInningsDeliveryData:
                    #print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    batsman = k[ball]['batsman']
                    run = k[ball]['runs']['batsman']

                    four = 0
                    if int(run) == 4:
                        four = 1

                    six = 0
                    if int(run) == 6:
                        six = 1

                    validBall = 1
                    try:
                        if k[ball]['extras']['wides']:
                            validBall = 0
                    except:
                        validBall = 1

                    flag = 0
                    i = 0
                    length = len(name_list)
                    #print(length)
                    for i in range(0,length):
                        if name_list[i] == batsman:
                            #print(i, name_list[i])
                            ball_list[i] = ball_list[i]+validBall
                            run_list[i] = run_list[i] + int(run)
                            four_list[i] = four_list[i] + four
                            six_list[i] = six_list[i] + six
                            #print(ball,i, name_list[i], ball_list[i],run_list[i])

                            flag = 1

                    if flag == 0:

                        status_list.append('not out')
                        strikerate_list.append(0.0)
                        date_list.append(str(dates))
                        team_list.append(team1)
                        name_list.append(batsman)
                        ballfaced = 1
                        ball_list.append(ballfaced)
                        run_list.append(int(run))
                        four_list.append(four)
                        six_list.append(six)

                    length = len(name_list)
                    outFlag = 0
                    try:
                        player_out = k[ball]['wicket']['player_out']
                        outFlag = 1
                        #print(player_out)
                    except:
                        player_out = '0'

                    if outFlag == 1:
                        #print(player_out)
                        i = 0
                        for i in range(0,length):
                            if name_list[i] == player_out:
                                status_list[i] = 'out'

                i = 0
                for i in range(0,length):
                    strikerate = (run_list[i] * 100.0) / ball_list[i]
                    strikerate_list[i] = strikerate
                    #print(date_list[i],name_list[i],ball_list[i],run_list[i],strikerate_list[i],four_list[i],six_list[i],status_list[i])

                for k in secondInningsDeliveryData:
                    # print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    batsman = k[ball]['batsman']
                    run = k[ball]['runs']['batsman']

                    four = 0
                    if int(run) == 4:
                        four = 1

                    six = 0
                    if int(run) == 6:
                        six = 1

                    validBall = 1
                    try:
                        if k[ball]['extras']['wides']:
                            validBall = 0
                    except:
                        validBall = 1

                    flag = 0
                    i = 0
                    length = len(name_list)
                    # print(length)
                    for i in range(0, length):
                        if name_list[i] == batsman:
                            # print(i, name_list[i])
                            ball_list[i] = ball_list[i] + validBall
                            run_list[i] = run_list[i] + int(run)
                            four_list[i] = four_list[i] + four
                            six_list[i] = six_list[i] + six
                            # print(ball,i, name_list[i], ball_list[i],run_list[i])

                            flag = 1

                    if flag == 0:
                        status_list.append('not out')
                        strikerate_list.append(0.0)
                        date_list.append(str(dates))
                        team_list.append(team2)
                        name_list.append(batsman)
                        ballfaced = 1
                        ball_list.append(ballfaced)
                        run_list.append(int(run))
                        four_list.append(four)
                        six_list.append(six)

                    length = len(name_list)
                    outFlag = 0
                    try:
                        player_out = k[ball]['wicket']['player_out']
                        outFlag = 1
                        #print(player_out)
                    except:
                        player_out = '0'

                    if outFlag == 1:
                        # print(player_out)
                        i = 0
                        for i in range(0, length):
                            if name_list[i] == player_out:
                                status_list[i] = 'out'

                i = 0
                for i in range(0, length):
                    strikerate = (run_list[i] * 100.0) / ball_list[i]
                    strikerate_list[i] = strikerate
                    #print(date_list[i], name_list[i], ball_list[i], run_list[i], strikerate_list[i], four_list[i], six_list[i],status_list[i])

                # Construction of a DataFrame
                data_set = pd.DataFrame({
                    'Team': pd.Series(team_list),
                    'Batsman': pd.Series(name_list),
                    'Ball': pd.Series(ball_list),
                    'Run': pd.Series(run_list),
                    'Fours': pd.Series(four_list),
                    'Six': pd.Series(six_list),
                    'Strike Rate': pd.Series(strikerate_list),
                    'Status': pd.Series(status_list),
                    'Winner/Result': result,
                    'Date': pd.Series(date_list)
                })

                value = value + 1
                # print(data_set)
                folder = 'D:\\STUDY\\3.2\\Project 300\\Batsman\\'
                # file_name = folder + teams + '.csv'
                file_name = folder + str(value) + '.csv'
                data_set.to_csv(file_name, encoding='utf-8')

    except OSError as e:
        nofile = 1
