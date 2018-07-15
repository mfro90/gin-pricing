#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from data_collection.html_crawl import extract_price_tags
from datetime import date

# get data
tags = extract_price_tags()

# convert to pd df obj
df = pd.DataFrame([sub.split(' ') for sub in tags], columns=["a", "price"])
df['b'], df['c'] = df['price'].str.split(',', 1).str  
df['d'], df['e'] = df['price'].str.split(',', 1).str  
df = df.drop(['a','price', 'b', 'c', 'e'], axis=1) 
df.columns = ['price']
df['price'] = df['price'].str.replace(".", "")
df['price'] = df['price'].astype('float')
df = df.drop(df[df.price >= 1000].index)

# price grouping
s = 350
price_prem = df[df['price'] >= s]
x0 = price_prem.iloc[:,0]
price_mass = df[df['price'] < s]
x1 = price_mass.iloc[:,0]

# draw histogram
trace0 = go.Histogram(x=x0, name='Premium', opacity=0.75)
trace1 = go.Histogram(x=x1, name='Mass', opacity=0.75)

data = [trace1, trace0]
layout = go.Layout(barmode='overlay')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Overlaid price histogram')

# write data to file
today = date.today()
file_name = str(today) + ".csv"
df.to_csv(file_name)