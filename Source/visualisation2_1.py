import plotly.express as px

def draw_scatter_followers(data):
    fig = px.scatter(data, x="followers", y="reaction", range_y=[0, 60000], range_x=[0, 10000000], opacity=0.8, color='Color')
    fig.update_layout(title="Nombre moyen de réactions par post selon le nombre de followers de la page")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title_x=0.5,
    font_color='rgb(59,89,152)')
    return fig
