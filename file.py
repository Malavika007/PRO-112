import statistics
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv

df = pd.read_csv('savings_data.csv')

quant_saved = df['quant_saved'].tolist()
highschool_completed = df['highschool_completed'].tolist()


with open ('savings_data.csv', newline = '') as f:
    reader = csv.reader(f)
    savings_data = list(reader)
savings_data.pop(0)

total_entries = len(savings_data)
total_people_given_remainder = 0

for data in savings_data:
    if int(data[3]) == 1:
        total_people_given_remainder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not reminded"], y=[total_people_given_remainder, (total_entries - total_people_given_remainder)]))
fig.show()

all_savings = []
for data in savings_data:
    all_savings.append(float(data[0]))


print(f"mean of savings: {statistics.mean(all_savings)}")
print(f"median of savings: {statistics.median(all_savings)}")
print(f"mode of savings: {statistics.mode(all_savings)}")

reminded_savings = []
not_reminded_savings = []


for data in savings_data:
    if int(data[3]) == 1:
      reminded_savings.append(float(data[0]))
    else:
       not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save: ")
print(f"mean of savings- {statistics.mean(reminded_savings)}")
print(f"mode of savings- {statistics.mode(reminded_savings)}")
print(f"median of savings- {statistics.median(reminded_savings)}")

print("results for people who were not reminded to save: ")
print(f"mean of savings- {statistics.mean(not_reminded_savings)}")
print(f"mode of savings- {statistics.mode(not_reminded_savings)}")
print(f"median of savings- {statistics.median(not_reminded_savings)}")


#Standard Deviation
print(f"standard deviation of all the data: {statistics.stdev(all_savings)}")
print(f"standard deviation of people who were reminded: {statistics.stdev(reminded_savings)}")
print(f"standard deviation of people who were not reminded: {statistics.stdev(not_reminded_savings)}")

import numpy as np
age = []
savings = []
for data in savings_data:
    if float(data[5]) != 0:
        age.append(float(data[5]))
        savings.append(float(data[0]))
correlation = np.corrcoef(age,savings)
print(f"correlation between age of the person and savings is : {correlation[0,1]}")

import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].tolist()], ["savings"], show_hist = False)
fig.show()
