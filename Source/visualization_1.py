import plotly.graph_objects as go
from plotly.subplots import make_subplots
import preprocess as preproc


FontSize = 11
HeightCell = 25
HeightHeader = 30
WidthsTablePlot = 0.2
WidthsArrowPlot = WidthsTablePlot/2

HeaderTemplate = ['nombrePage','nombreReaction','interaction','followers']

def CreateTable(data,fig):
    subplot = 1
    Top = len(data.index)
    for strHeader in HeaderTemplate:
        fig.add_trace(go.Table(header=dict(font_size=FontSize,values=["<b> {} </b>".format(strHeader)],
        height=HeightHeader, align='center'), 
        
        cells=dict(font=dict(color='white', size=FontSize),
        values=[data[strHeader]], 
        align='center', height=HeightCell,
        line_color=[data[strHeader+"Color"]], fill_color=[data[strHeader+"Color"]])),
        row=1,col=subplot
        )
        subplot = subplot + 2
    fig.update_layout(dragmode=False,width=1650, height=(Top*HeightCell + HeightHeader + 180))
    return fig
    
def CreateArrow(data,fig):
    fig.update_layout(plot_bgcolor="white")
    Top = len(data.index)
    HeadTable = [StrHead+"Color"  for StrHead in HeaderTemplate]
    for col in range(len(HeadTable)-1):
        fig['layout']['xaxis'+str(col+1)].update(range=[0,1],showgrid=False,visible=False)
        fig['layout']['yaxis'+str(col+1)].update(range=[0,(Top*HeightCell+HeightHeader)/HeightCell],tick0=0,dtick=0.5,showgrid=False,visible=False)
        for cellColor in data[HeadTable[col]]:
            fig.add_annotation(
                x=1,
                y=Top - data[data[HeadTable[col+1]]  == cellColor].index.tolist()[0] - 0.5,
                xref = "x"+str(col+1),yref = "y"+str(col+1),showarrow=True,
                arrowhead=3,arrowsize=1,arrowwidth=3,
                arrowcolor = cellColor,
                ax=0,
                ay=Top - data[data[HeadTable[col]] == cellColor].index.tolist()[0] - 0.5,
                axref="x"+str(col+1),ayref='y'+str(col+1))
    return fig
def CreateSubPlot(data):
    NumSubPlot = len(data.columns) - 1
    ColumnWidths = [WidthsTablePlot , WidthsArrowPlot]* int(NumSubPlot//2) + [WidthsTablePlot]

    fig = make_subplots(column_widths=ColumnWidths,
    rows=1,cols=NumSubPlot,
    horizontal_spacing=0.0,
    specs=[[{"type": "table"},{"type": "scatter"}]*int(NumSubPlot//2) +[{"type": "table"}]])
    

    return fig
def Visual_1(data,col):
    data = preproc.SelectDataVisual1(data,col)
    fig = CreateSubPlot(data)
    fig = CreateTable(data,fig)
    fig = CreateArrow(data,fig)

    return fig