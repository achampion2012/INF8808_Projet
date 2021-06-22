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
import visualization_2
from visualisation2_1 import draw_scatter_followers

app = dash.Dash(__name__)
app.title = 'Project | INF8808'

df = pd.read_csv('assets/data/reduced_db.zip')


fig00 = draw_average_type()
fig01 = draw_average_lang()
fig02 = Visual_1([])

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

df_scatter = pd.read_csv('assets/data/scatter.csv', index_col=0)
fig2_1 = draw_scatter_followers(df_scatter)

#Creates dropdown options {pagename: fbid}
df_pagename_fbid = pd.read_csv('assets/data/pagename_fbid_reduced.csv')
list_of_dicts = []
for index, row in df_pagename_fbid.iterrows():
    temp = {
        'label' : '{}'.format(row['page']), 
        'value' : '{}'.format(row['fbid'])
        }
    list_of_dicts.append(temp)


app.layout = html.Div(
    className='content',
    children=[
        html.Header(children=[
            html.H1('Les pages Facebook canadiennes en 2020'),
            html.H3('Que s’est-il passé sur Facebook en 2020 ? Quelles sont les pages canadiennes qui se sont démarquées et quelles sont les caractéristiques de ces pages ? L’article suivant vous propose de plonger dans les données de 3,6 millions de publications, c’est-à-dire les 300,000 ayant reçues le plus de likes à chaque mois durant l’année 2020. ')
        ]),

        # first figure
        html.Div(children=[
            html.H2("Mise en contexte"),
            html.H3("Les pages canadiennes ont principalement publié des photos, avec près de la moitié des publications appartenant à ce type."),
            dcc.Graph(figure=fig00, id='graph00',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            html.Footer("")
            ]),

        #second figure
        html.Div(children=[
            html.H3("Comme on pouvait s’y attendre, les pages canadiennes publient principalement en anglais. Cependant, des publications ont été faites dans plus de 89 langues !"),
            dcc.Graph(figure=fig01, id='graph01',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            html.Footer("")
            ]),
        
        #third figure
        html.Div(children=[
            html.H2("Meilleures pages canadiennes en 2020"),
            html.H3("Un ranking chart présente d’abord les pages s’étant démarquées selon différentes catégories. Il est ensuite possible de sélectionner une seule page et d’aller voir en détail pourquoi elle s’est démarquée. Cela permet aussi de voir son ranking pour toutes les catégories, même si elle n’était pas dans le top 20"),
            html.H3("Absolute number of posts: Ici, on regarde les pages qui ont le plus posté en 2020. Ce sont principalement des pages de nouvelles."),
            html.H3("Absolute number of reactions: On regarde les pages qui ont généré le total de réactions le plus grand en 2020."),
            html.H3("Reactions per post: On divise le nombre de réactions par le nombre de post d’une page pour avoir le nombre de réactions moyen par publication."),
            html.H3("Total followers: On classe les pages en fonction du nombre de followers moyen qu’ils ont eu dans l’année."),
            dcc.Graph(figure=fig02, id='graph02_1',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            html.Footer("")
            ]),

        html.Div(children=[
            html.H2("Comment maximiser les réactions sur ses posts Facebook ?"),
            html.H3("Pour les gestionnaires de pages, le but est d'atteindre le plus grand nombre de personnes possible par publication. Quelles sont donc les conditions optimales pour atteindre cet objectif? Est-ce que le nombre de followers de la page impacte le niveau d'interaction?"),
            dcc.Graph(figure=fig2_1, id='graph2_1',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            html.H3("Étonnament, on remarque qu'il n'y a pas de lien évident entre les followers et le nombre de réaction, il est donc possible d'avoir un grand nombre de réaction même avec peu de followers !"),
            html.Footer("")
            ]),

        html.Div(children=[
            html.Header("Nombre de publications par semaine en 2020"),
            dcc.Graph(figure=fig_hm_week, id='fig_hm_week',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          doubleClick=False,
                          displayModeBar=False)),
            #html.Footer("First figure footer")
            ]),

            html.Div(children=[
                html.Header("Nombre de publications selon le jour de la semaine en 2020"),
                dcc.Graph(figure=fig_hm_weekday, id='fig_hm_weekday',
                          config=dict(
                              showTips=False,
                              showAxisDragHandles=False,
                              doubleClick=False,
                              displayModeBar=False)),
                #html.Footer("First figure footer")
                ]),
        
        html.Div([
#             dcc.Dropdown(
#                 id='fb-pages',
#                 options=list_of_dicts,
#                 placeholder="Select a page",
#                 clearable=False,
#                 style={'color':'black'},
#                 value=273000682715952
#             ),
            html.Div(
                children=[
                    html.H2("Cette section présente des données plus en détail pour une seule page. Il sera possible de sélectionner la page dans un menu déroulant."),
                    html.Header("Nombre de followers moyen par mois"),
                    dcc.Graph(
                        id='line-chart-followers',
                        className='graph',
                        figure=visualization_2.draw_line_chart_followers_months(df, 100044362032719),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False)
                            ),
                    html.Header("Nombre de publications par mois"),
                    dcc.Graph(
                        id='line-chart-posts',
                        className='graph',
                        figure=visualization_2.draw_line_chart_publications_months(df, 100044362032719),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False)
                            ),
                    html.Header("Nombre total de reactions par mois"),
                    dcc.Graph(
                        id='bar-chart-reactions',
                        className='graph',
                        figure=visualization_2.draw_stacked_bar_chart_reactions_months(df, 100044362032719),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False)
                            ),
                    html.Header("Type de publication"),
                    dcc.Graph(
                        id='pie-chart-type',
                        className='graph',
                        figure=visualization_2.draw_piechart_type(df, 100044362032719),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False)
                            )
                    ])
                ])
        ])

# @app.callback(
#     [Output('line-chart-followers', 'figure'), 
#     Output('line-chart-posts', 'figure'),
#     Output('bar-chart-reactions', 'figure'),
#     Output('pie-chart-type', 'figure')],
#     [Input('fb-pages', 'value')]
# )
# def update_output(value):
#     line_chart_followers = visualization_2.draw_line_chart_followers_months(df, value)
#     line_chart_posts = visualization_2.draw_line_chart_publications_months(df, value)
#     bar_chart_reactions = visualization_2.draw_stacked_bar_chart_reactions_months(df, value)
#     pie_chart_type = visualization_2.draw_piechart_type(df, value)

#     return line_chart_followers, line_chart_posts, bar_chart_reactions, pie_chart_type
