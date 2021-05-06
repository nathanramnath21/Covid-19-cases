import pandas as pd 
import plotly.express as px
df=pd.read_csv("Copy+of+data+-+data.csv")
flg=px.line(df, x="cases", y="date", color="country", title='Covid-19 cases')
flg.show()