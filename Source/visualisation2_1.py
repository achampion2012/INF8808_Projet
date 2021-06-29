import plotly.express as px
ColorScatter = ["#0084ff","#44bec7","#ffc300","#fa3c4c","#d696bb"]
def draw_scatter_followers(data):
    fig = px.scatter(data, x="followers", y="reaction", range_y=[0, 60000], range_x=[0, 10000000], opacity=0.8, color='Color',
    color_discrete_sequence=ColorScatter)
    fig.update_layout(title="Nombre moyen de réactions par post selon le nombre de followers de la page")
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_x=0.5,
        font_color='rgb(59,89,152)'
    )
    
    hover_template = (
        "<b>Followers :</b> %{x}<br>" +
        "<b>Reactions :</b> %{y}<br>" + 
        "<extra></extra>"
    )
    
    fig.update_traces(hovertemplate=hover_template)
    fig.update_xaxes(title="Nombre de followers")
    fig.update_yaxes(title="Nombre de réaction")
    return fig

def draw_barchart_type(data):
    fig = px.bar(
        data.groupby(["type"]).median(), 
        y="reaction"
    )
    
    hover_template = (
        "<b>Type de publication :</b> %{x}<br>" +
        "<b>Reactions (median) :</b> %{y}<br>" + 
        "<extra></extra>")
    
    fig.update_traces(
        marker_color='rgb(59,89,152)',
        hovertemplate=hover_template
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_x=0.5,
        font_color='rgb(59,89,152)'
    )
                 
    fig.update_layout(
        yaxis={"title":"Nombre de réactions médian"}, 
        xaxis={'categoryorder':'array', 'categoryarray':["Live Video", "Photo", "Video", "Status", "Album", "Link"], "title":"Type de publication"}
    )
                 
    return fig
