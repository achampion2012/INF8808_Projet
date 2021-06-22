import plotly.express as px

def draw_scatter_followers(data):
    fig = px.scatter(data, x="followers", y="reaction", range_y=[0, 60000], range_x=[0, 10000000], opacity=0.8, color='Color')
    fig.update_layout(title="Nombre moyen de réactions par post selon le nombre de followers de la page")
    return fig