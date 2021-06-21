
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

from visualization_1 import Visual_1

app = dash.Dash(__name__)
app.title = 'Project | INF8808'

df = pd.read_csv('assets/data/facebookCanada2020.zip')

fig1 = Visual_1(df)
fig00 = draw_average_type()
fig01 = draw_average_lang()


app.layout = html.Div(
    className='content',
    children=[
        html.Header(children=[
            html.H1('Les pages Facebook Canadiennes en 2020'),
            html.H2('Que s’est-il passé sur Facebook en 2020 ? Quelles sont les pages canadiennes qui se sont démarquées et quelles sont les caractéristiques de ces pages ? L’article suivant vous propose de plonger dans les données de 3,6 millions de publications, c’est-à-dire les 300,000 ayant reçues le plus de likes à chaque mois durant l’année 2020. ')
        ]),

        # first figure
        html.Div(children=[
            html.Header("Type de publication"),
            dcc.Graph(figure=fig00, id='graph1',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            html.Footer("First figure footer")
            ])

        # second figure
        # html.Div(children=[
        #     html.Header("First figure header"),
        #     dcc.Graph(figure=fig1, id='graph1',
        #               config=dict(
        #                   showTips=False,
        #                   showAxisDragHandles=False,
        #                   doubleClick=False,
        #                   displayModeBar=False)),
        #     html.Footer("First figure footer")
        # ])


    ])
