import pandas as pd
import plotly.figure_factory as pff
import statistics as st
df = pd.read_csv('height-weight.csv')
height = df['Height(Inches)'].tolist()
#graph = pff.create_distplot([height],['Height(Inches)'], show_hist= False)
#graph.show()
mean = st.mean(height)
std = st.stdev(height)
# fstd_sp = mean - std
# fstd_ep = mean + std
# fstd_count = 0
# for eachheight in height:
#   if eachheight > fstd_sp and eachheight < fstd_ep:
#       fstd_count = fstd_count + 1
# fstd_percentage = (fstd_count/len(height))*100
# print(fstd_percentage)
# sftd_sp = mean - 2*std
# sftd_ep = mean + 2*std
# sftd_count = 0
# for eachHeight in height:
#     if eachHeight>sftd_sp and eachHeight<sftd_ep:
#         sftd_count = sftd_count + 1
# sftd_percentage = (sftd_count/len(height))*100
# print(sftd_percentage)
dfst_sp = mean - 3*std
dfst_ep = mean + 3*std
dfst_count = 0
for eachHeight in height:
    if eachHeight > dfst_sp and eachHeight < dfst_ep:
        dfst_count = dfst_count + 1
dfst_percentage = (dfst_count/len(height))*100
print(dfst_percentage)