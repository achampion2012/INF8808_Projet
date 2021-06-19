import plotly.graph_objects as go
from plotly.subplots import make_subplots

FontSize = 11
HeadTable = ['nombrePage','nombreReaction','interaction','followers']
Top = 20

def Visual_1(data):
    fig = make_subplots(column_widths=[0.2, 0.1,0.2, 0.1,0.2, 0.1,0.2],rows=1,horizontal_spacing=0.0, cols=7,specs=[[{"type": "table"},{"type": "scatter"},{"type": "table"},{"type": "scatter"},{"type": "table"},{"type": "scatter"},{"type": "table"}]])

    fig.add_trace(go.Table(header=dict(font_size=FontSize,values=["<b> {} </b>".format(HeadTable[0])],align='center'), 
    cells=dict(font=dict(color='white', size=FontSize),values=[data[HeadTable[0]]], align='center', height=25,line_color=[data['nombrePageColor']], fill_color=[data['nombrePageColor']])
        ,),
        row=1,col=1)

    fig.add_trace(go.Table(header=dict(font_size=FontSize,values=["<b> {} </b>".format(HeadTable[1])],align='center'), 
    cells=dict(font=dict(color='white', size=FontSize),values=[data[HeadTable[1]]], align='center', height=25,line_color=[data['nombreReactionColor']], fill_color=[data['nombreReactionColor']])
        ,),
        row=1,col=3)

    fig.add_trace(go.Table(header=dict(font_size=FontSize,values=["<b> {} </b>".format(HeadTable[2])],align='center'), 
    cells=dict(font=dict(color='white', size=FontSize),values=[data[HeadTable[2]]], align='center', height=25,line_color=[data['interactionColor']], fill_color=[data['interactionColor']])
        ,),
        row=1,col=5)

    fig.add_trace(go.Table(header=dict(font_size=FontSize,values=["<b> {} </b>".format(HeadTable[3])],align='center'), 
    cells=dict(font=dict(color='white', size=FontSize),values=[data[HeadTable[3]]], align='center', height=25,line_color=[data['followersColor']], fill_color=[data['followersColor']])
        ,),
        row=1,col=7)



    fig.update_layout(dragmode=False,width=1650, height=710,plot_bgcolor="white")

    for col in range(len(HeadTable)-1):
        fig['layout']['xaxis'+str(col+1)].update(range=[0,1],showgrid=False,visible=False)
        fig['layout']['yaxis'+str(col+1)].update(range=[0,21.18],tick0=0,dtick=0.5,showgrid=False,visible=False)
        for cellColor in data[HeadTable[col]+'Color']:
            fig.add_annotation(
                x=1,
                y=20 - data[data[HeadTable[col+1]+'Color']  == cellColor].index.tolist()[0] - 0.5,
                xref = "x"+str(col+1),yref = "y"+str(col+1),showarrow=True,
                arrowhead=3,arrowsize=1,arrowwidth=3,
                arrowcolor = cellColor,
                ax=0,
                ay=20 - data[data[HeadTable[col]+'Color'] == cellColor].index.tolist()[0] - 0.5,
                axref="x"+str(col+1),ayref='y'+str(col+1))
    return fig