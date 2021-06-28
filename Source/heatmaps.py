import plotly.express as px

def get_heatmap_week(df):
    fig = px.imshow(df, color_continuous_scale="magma", width=1000)
    fig.update_layout(xaxis_title="Semaine", yaxis_title="Heure", paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title_x=0.5,
    font_color='rgb(59,89,152)',
    title="Nombre de publications par semaine en 2020")
    fig.update_traces(hovertemplate="<br>".join([
            "<b> Semaine: </b> %{x}",
            "<b> Heure: </b> %{y}h00 - %{y}h59",
            "<b> Interactions: </b> %{z} <extra></extra>"]))
    return fig

def get_heatmap_weekday(df):
    fig = px.imshow(df, color_continuous_scale="magma", width=300)
    fig.update_layout(xaxis_title="Jour", yaxis_title="Heure", paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title_x=0.5,
    font_color='rgb(59,89,152)',
    title="Nombre de publications selon le jour de la semaine en 2020")
    fig.update_traces(hovertemplate="<br>".join([
            "<b> Jour: </b> %{x}",
            "<b> Heure: </b> %{y}h00 - %{y}h59",
            "<b> Interactions: </b> %{z} <extra></extra>"]))
    return fig
