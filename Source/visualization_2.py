import plotly.graph_objects as go
import preprocess as prepro

color_palette = [ '#3b5998', '#ffc300', '#0084ff', '#fa3c4c', '#44bec7', '#7646ff', '#d696bb', '#8b9dc3', '#6699cc']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def empty_fig():
    fig = go.Figure()
    return fig

def draw_line_chart_followers_months(df, fbid):

    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.mean_followers_bymonth(df)


    fig = go.Figure()
    fig = fig.add_traces(
        go.Scatter(
            x=months,
            y=temp_df,
            mode='lines+markers',
            marker=dict(color=color_palette[0])
            )
        )

    fig.update_layout(
        title="Le nombre de follower moyen par mois",
        font=dict(
            family="Klavika",
            size=15,
            color="#3b5998"
            ),
        paper_bgcolor='#dfe3ee',
        plot_bgcolor='#dfe3ee',
        yaxis_title="Followers",
        xaxis_title="Months"
        )
    
    hover_template = (
        "<b>Month :</b> %{x}<br>" +
        "<b>Followers :</b> %{y}<br>" + 
        "<extra></extra>"
    )

    fig.update_traces(
        hovertemplate=hover_template
    )

    return fig


def draw_line_chart_publications_months(df, fbid):
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.count_post_bymonth(df)

    fig = go.Figure()
    fig = fig.add_traces(
        go.Scatter(
            x=months,
            y=temp_df,
            mode='lines+markers',
            marker=dict(color=color_palette[0])
            )
        )

    fig.update_layout(
        title="Le nombre de publication(s) par mois",
        font=dict(
            family="Klavika",
            size=15,
            color="#3b5998"
            ),
        paper_bgcolor='#dfe3ee',
        plot_bgcolor='#dfe3ee',
        yaxis_title="Number of posts",
        xaxis_title="Months"
        )
    
    hover_template = (
        "<b>Month :</b> %{x}<br>" +
        "<b>Nb of posts :</b> %{y}<br>" + 
        "<extra></extra>"
    )

    fig.update_traces(
        hovertemplate=hover_template
    )
    
    return fig


def draw_stacked_bar_chart_reactions_months(df, fbid):
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.sum_reactions_bymonth(df)

    fig = go.Figure(data=[
        go.Bar(x=months, y=temp_df['likes'], name='likes', marker=dict(color=color_palette[0])),
        go.Bar(x=months, y=temp_df['comments'], name='comments', marker=dict(color=color_palette[1])),
        go.Bar(x=months, y=temp_df['shares'], name='shares', marker=dict(color=color_palette[2])),
        go.Bar(x=months, y=temp_df['love'], name='love', marker=dict(color=color_palette[3])),
        go.Bar(x=months, y=temp_df['wow'], name='wow', marker=dict(color=color_palette[4])),
        go.Bar(x=months, y=temp_df['haha'], name='haha', marker=dict(color=color_palette[5])),
        go.Bar(x=months, y=temp_df['sad'], name='sad', marker=dict(color=color_palette[6])),
        go.Bar(x=months, y=temp_df['angry'], name='angry', marker=dict(color=color_palette[7])),
        go.Bar(x=months, y=temp_df['care'], name='care', marker=dict(color=color_palette[8]))
    ])

    fig.update_layout(barmode='stack')

    fig.update_layout(
        title="Le nombre total d'interaction totale par mois",
        font=dict(
            family="Klavika",
            size=15,
            color="#3b5998"
            ),
        legend_title="Reactions",
        paper_bgcolor='#dfe3ee',
        plot_bgcolor='#dfe3ee',
        yaxis_title="Number of interactions",
        xaxis_title="Months"
        )
    
    hover_template = (
        "<b>Month :</b> %{x}<br>" +
        "<b>Nb of reactions :</b> %{y}<br>"
    )

    fig.update_traces(
        hovertemplate=hover_template
    )

    return fig


def draw_piechart_type(df, fbid):
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.count_post_type(df)

    fig = go.Figure(data=[
        go.Pie(
            labels=temp_df['type'], 
            values=temp_df['fbid']
            )
    ])

    fig.update_layout(
        title="Le type de publication",
        font=dict(
            family="Klavika",
            size=15,
            color="#3b5998"
            ),
        legend_title="Types",
        paper_bgcolor='#dfe3ee',
        plot_bgcolor='#dfe3ee'
        )
    
    fig.update_traces(
        marker=dict(colors=color_palette)
    )

    return fig
