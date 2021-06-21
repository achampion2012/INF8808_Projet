import plotly.express as px

def get_heatmap_week(df):
    fig = px.imshow(df, color_continuous_scale="magma", width=1000)
    fig.update_layout(xaxis_title="Semaine", yaxis_title="Heure")
    fig.update_traces(hovertemplate="<br>".join([
            "<b> Semaine: </b> %{x}",
            "<b> Heure: </b> %{y}h00 - %{y}h59",
            "<b> Interactions: </b> %{z} <extra></extra>"]))
    return fig

def get_heatmap_weekday(df):
    fig = px.imshow(df, color_continuous_scale="magma", width=300)
    fig.update_layout(xaxis_title="Jour", yaxis_title="Heure")
    fig.update_traces(hovertemplate="<br>".join([
            "<b> Jour: </b> %{x}",
            "<b> Heure: </b> %{y}h00 - %{y}h59",
            "<b> Interactions: </b> %{z} <extra></extra>"]))
    return fig
