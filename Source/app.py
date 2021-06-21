
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
import heatmaps

from visualization_1 import Visual_1
from visualisation0 import draw_average_type
from visualisation0 import draw_average_lang

app = dash.Dash(__name__)
app.title = 'Project | INF8808'

#df = pd.read_csv('assets/data/facebookCanada2020.zip')

#fig1 = Visual_1(df)
fig00 = draw_average_type()
fig01 = draw_average_lang()


# Heatmaps
#   df = pd.read_csv('../src/assets/data/facebookCanada2020.csv', index_col=0)
#   df = preproc.FilterData(df)
#   df = preproc.datecreated_to_datetime(df)
#   df_hm = preproc.datecreated_to_datetime(df)
#   df_hm = preproc.week_hour_weekday(df_hm)
#   df_hm_week = preproc.week_hour_publication(df_hm)
#   df_hm_weekday = weekday_hour_publication(df_hm)

df_hm_week = pd.read_csv('assets/data/hm_week.csv', index_col=0)
df_hm_weekday = pd.read_csv('assets/data/hm_weekday.csv', index_col=0)

fig_hm_week = heatmaps.get_heatmap_week(df_hm_week)
fig_hm_weekday = heatmaps.get_heatmap_weekday(df_hm_weekday)



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
            ]),

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


        html.Div(children=[
            html.Header("Number of publications for each week of 2020"),
            dcc.Graph(figure=fig_hm_week, id='fig_hm_week',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            #html.Footer("First figure footer")
            ]),

            html.Div(children=[
                html.Header("Number of publications for each weekday of 2020"),
                dcc.Graph(figure=fig_hm_weekday, id='fig_hm_weekday',
                          config=dict(
                              showTips=False,
                              showAxisDragHandles=False,
                              doubleClick=False,
                              displayModeBar=False)),
                #html.Footer("First figure footer")
                ])


    ])
