import plotly.graph_objects as go
import preprocess as prepro


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
            x=temp_df.keys(),
            y=temp_df,
            mode='lines+markers'
            )
        )

    

    return fig


def draw_line_chart_publications_months(df, fbid):
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.count_post_bymonth(df)

    fig = go.Figure()
    fig = fig.add_traces(
        go.Scatter(
            x=temp_df.keys(),
            y=temp_df,
            mode='lines+markers'
            )
        )
    


    return fig


def draw_stacked_bar_chart_reactions_months(df, fbid):
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.sum_reactions_bymonth(df)

    # fig = go.Figure()
    fig = go.Figure(data=[
        go.Bar(x=temp_df['month'], y=temp_df['likes'], name='likes'),
        go.Bar(x=temp_df['month'], y=temp_df['comments'], name='comments'),
        go.Bar(x=temp_df['month'], y=temp_df['shares'], name='shares'),
        go.Bar(x=temp_df['month'], y=temp_df['love'], name='love'),
        go.Bar(x=temp_df['month'], y=temp_df['wow'], name='wow'),
        go.Bar(x=temp_df['month'], y=temp_df['haha'], name='haha'),
        go.Bar(x=temp_df['month'], y=temp_df['sad'], name='sad'),
        go.Bar(x=temp_df['month'], y=temp_df['angry'], name='angry'),
        go.Bar(x=temp_df['month'], y=temp_df['care'], name='care')
    ])

    fig.update_layout(barmode='stack')

    return fig


def draw_piechart_type(df, fbid): # Or barchart TO CONFIRM
    df = prepro.filter_by_fbid(df, fbid)
    df = prepro.filter_by_month(df)

    temp_df = prepro.count_post_type(df)

    # fig = go.Figure()
    fig = go.Figure(data=[
        go.Pie(
            labels=temp_df['type'], 
            values=temp_df['fbid']
            )
    ])



    return fig
