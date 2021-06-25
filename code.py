import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

student_details = df.loc[df['student_id']=="TRL_zny"]

print(df.groupby("level")["attempt"].mean())

#graph = px.bar(student_details, x= ["level 1","level 2", "level 3", "level 4"], y =student_details.groupby("level")["attempt"].mean() )
#graph.show()

fig = go.Figure(go.Bar(
    x =student_details.groupby("level")["attempt"].mean(),
    y=["level 1","level 2", "level 3", "level 4"],
    
    orientation = 'h'

))

fig.show();