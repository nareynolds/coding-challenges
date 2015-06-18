# question 1

# dependencies
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# directory containing this file
filedir = os.path.dirname(os.path.realpath(__file__))



# import data
csv_path = os.path.join(filedir, "data.csv")
df = pd.read_csv(csv_path)

# get only requested data
df_filt = df[ (df['Activity']=='Drive') 
             & (df['Network_Types']=='LTE') 
             & (df['Data_Direction']=='Download')
            ]

# convert speed from kilobits to megabits
df_filt.loc[:,('Final_Test_Speed')] /= 1000

# Carrier B
df_filt_B = df_filt[df_filt['Carrier']=='B']

# Carrier C
df_filt_C = df_filt[df_filt['Carrier']=='C']

# plot Carrier C strength vs speed
xC = df_filt_C['LTE_Signal_Strength'].tolist()
yC = df_filt_C['Final_Test_Speed'].tolist()
plt.plot(xC, yC, 'ro')

# plot Carrier B strength vs speed
xB = df_filt_B['LTE_Signal_Strength'].tolist()
yB = df_filt_B['Final_Test_Speed'].tolist()
plt.plot(xB, yB, 'go')

# format plot
plt.title('Download Speed vs LTE Strength')
plt.xlabel('LTE Signal Strength')
plt.ylabel('Final Test Speed (megabits)')

# show plot
plt.show()
