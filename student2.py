import csv
import plotly.graph_objects as go 
import pandas as pd 

df= pd.read_csv("data.csv")

studentDf= df.loc[df["student_id"] == 'TRL_abc']

#print(studentDf)

print(studentDf.groupby('level')['attempt'].mean())

fig = go.Figure(go.Bar(
    x = studentDf.groupby('level')['attempt'].mean(),
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation = 'h'
))

fig.show()