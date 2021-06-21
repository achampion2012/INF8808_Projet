
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file contains the source code for TP5.
'''
import pandas as pd

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go

import preprocess as preproc
import viz
import helper
import callback

import visualization_1

app = dash.Dash(__name__)
app.title = 'Project | INF8808'

df = pd.read_csv('assets/data/facebookCanada2020.zip')

fig = visualization_1.Visual_1(df)


app.layout = html.Div(
    className='test',
    children=[
        dcc.Graph(figure=fig, id='graph',
                  config=dict(
                      showTips=False,
                      showAxisDragHandles=False,
                      doubleClick=False,
                      displayModeBar=False)),])