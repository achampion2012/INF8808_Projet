#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.express as px


def draw_average_lang():

    #to be deleted once database solution is known
    x = ["Anglais", "Français", "Autre", "Arabe", "Espagnol"]
    y = [2456276, 601355, 385855, 118331, 37882 ]
    
    hover_template = (
        "<b>Type de publication :</b> %{x}<br>" +
        "<b>Nombre de publication :</b> %{y}<br>" + 
        "<extra></extra>"
    )
    
    fig = px.bar(x=x, y=y, 
    title='Répartition des publications selon la langue en 2020',  
    labels={'x':'Langue de publication', 'y': 'Nombre de publications'} )
    fig.update_traces(marker_color='rgb(59,89,152)',
                      hovertemplate=hover_template
    )
    
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title_x=0.5,
    font_color='rgb(59,89,152)')
        
    fig.update_traces()

    return fig
    
def draw_average_type():

    #to be deleted once database solution is known
    x = ["Photo", "Lien", "Video", "Statut", "Live Video"]
    y = [1746691, 1181804, 453208, 124767, 93029 ]
    

    fig = px.bar(x=x, y=y, 
    title='Répartition des publications selon le type en 2020',  
    labels={'x':'Type de publication', 'y': 'Nombre de publications'} )
    fig.update_traces(marker_color='rgb(59,89,152)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title_x=0.5,
    font_color='rgb(59,89,152)')
    
    hover_template = (
        "<b>Langue de publication :</b> %{x}<br>" +
        "<b>Nombre de publication :</b> %{y}<br>" + 
        "<extra></extra>"
    )
        
    fig.update_traces(hovertemplate=hover_template)

    return fig
    

