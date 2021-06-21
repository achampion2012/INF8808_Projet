'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd

Top = 10
colors = ['#1f77b4','#aec78e','#ff7f0e','#ffbb78','#2ca02c',
        '#98df8a','#d62728','#ff9896','#9467bd','#c5b0d5',
        '#8c564b','#c49c94','#e377c2','#f7b6d2','#7f7f7f',
        '#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']
def FilterData(df):
    df['interaction'] = df['likes'] + df['comments'] + df['shares'] + df['love'] + df['wow'] + df['haha'] + df['sad'] + df['angry'] + df['care']

    dataPage = df.groupby(['page']).size().reset_index()
    dataPage.columns = ['page','nombrePage']

    dataReaction = df.groupby(['page']).agg({'interaction':'sum'}).reset_index()
    dataReaction.columns = ['page','nombreReaction']

    dataFollowers = df.groupby(['page']).agg({'followers':'max'}).reset_index()

    dataReactionPost = pd.concat([dataReaction['page'] , dataReaction['nombreReaction']/dataPage['nombrePage']],axis=1)
    dataReactionPost.columns = ['page','interaction']

    result = pd.merge(dataPage, dataReaction, on='page', how='inner')
    result = pd.merge(result, dataFollowers, on='page', how='inner')
    result = pd.merge(result, dataReactionPost, on='page', how='inner')
    return result


def SelectColor(data,col=1):
    maxTableCol = len(data.columns) - 1


    table = data.sort_values([data.columns[col]],ascending=[0]).head(Top)['page'].rename(data.columns[col]).reset_index()
    table = table.drop(['index'], axis=1)
    table[data.columns[col]+"Color"] = colors[:Top]
    dictColor = dict(zip(table[data.columns[col]], table[data.columns[col]+"Color"]))
    for i in range(1,maxTableCol+1,1):
        if i != col:
            Z = data.sort_values([data.columns[i]],ascending=[0]).reset_index()
            Z.drop(['index'], axis=1)
            temp = {}
            for cell in table[data.columns[col]]:
                temp[cell] = Z[Z['page']==cell].index.item()
            temp= sorted(temp.items(), key=lambda x: x[1])
            tempColor = [dictColor[name[0]] for name in temp]
            temp= [name[0]+" ("+str(name[1]+1)+")" for name in temp]
            table[data.columns[i]] = temp
            table[data.columns[i]+"Color"] = tempColor
    return table

def SelectDataVisual1(data):
    data = FilterData(data)
    data = SelectColor(data)
    return data

def DatecreatedToDateTime(df):
    df.datecreated = pd.to_datetime(df.datecreated)
    return df

def WeekHourWeekday(df):
    df['week'] = df.datecreated.dt.week
    df['hour'] = df.datecreated.dt.hour
    df['weekday'] = df.datecreated.dt.weekday
    return df

def WeekHourInteraction(df):
    df = df[['week', 'hour', 'interaction']]
    df = df.groupby(['week', 'hour'], as_index=False).count()
    df = df.pivot('hour', 'week', 'interaction')
    return df

def WeekdayHourInteraction(df):
    df = df[['weekday', 'hour', 'interaction']]
    df = df.groupby(['weekday', 'hour'], as_index=False).count()
    df = df.pivot('hour', 'weekday', 'interaction')
    return df
