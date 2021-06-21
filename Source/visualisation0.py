#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.graph_objects as go
import preprocessing as prepro


def draw_average_lang():

    #to be deleted once database solution is known
    x = ["Anglais", "Français", "Autre", "Arabe", "Espagnol"]
    y = [2456276, 601355, 385855, 118331, 37882 ]
    

    fig = px.bar(dftype, x=x, y=y, 
    title='Répartition des publications selon la langue en 2020',  
    labels={'x':'Langue de publication', 'y': 'Nombre de publications'} )
    fig.update_traces(marker_color='rgb(59,89,152)')

    return fig
    
def draw_average_type():

    #to be deleted once database solution is known
    x = ["Photo", "Lien", "Video", "Statut", "Live Video"]
    y = [1746691, 1181804, 453208, 124767, 93029 ]
    

    fig = px.bar(dftype, x=x, y=y, 
    title='Répartition des publications selon le type en 2020',  
    labels={'x':'Type de publication', 'y': 'Nombre de publications'} )
    fig.update_traces(marker_color='rgb(59,89,152)')

    return fig
    
