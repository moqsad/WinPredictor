import csv
import pandas as pd
import numpy as nm
from pylab import*

match = 41 + 27 + 31 + 31 + 27 + 26 + 20
win = 24 + 17 + 17 + 16 + 14 + 11 + 10
loss = 17 + 10 + 11 + 12 + 12 + 13 + 10
tie = 0 + 0 + 3 + 0 + 0 + 1 + 0

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

title('Effect of Homeground', bbox={'facecolor':'0.8', 'pad':5})

show()

