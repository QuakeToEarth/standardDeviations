import pandas as pd
import plotly.figure_factory as pff
import statistics as st
df = pd.read_csv('height-weight.csv')
weight = df['Weight(Pounds)'].tolist()
mean = st.mean(weight)
std = st.stdev(weight)
fstd_sp = mean - std
fstd_ep = mean + std
fstd_count = 0
for eachWeight in weight:
    if eachWeight > fstd_sp and eachWeight < fstd_ep :
        fstd_count = fstd_count + 1
fstd_percentage = (fstd_count/len(weight))*100
print(fstd_percentage)



sftd_sp = mean - 2*std
sftd_ep = mean + 2*std
sftd_count = 0
for eachWeight in weight:
    if eachWeight > sftd_sp and eachWeight < sftd_ep :
        sftd_count = sftd_count + 1
sftd_percentage = (sftd_count/len(weight))*100
print(sftd_percentage)



abtd_sp = mean - 3*std
abtd_ep = mean + 3*std
abtd_count = 0
for eachWeight in weight:
    if eachWeight > abtd_sp and eachWeight < abtd_ep :
        abtd_count = abtd_count + 1
abtd_percentage = (abtd_count/len(weight))*100
print(abtd_percentage)