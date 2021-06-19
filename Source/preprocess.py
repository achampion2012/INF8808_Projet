'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd

def preprocessVisu1_1(df):
    df['interaction'] = df['likes'] + df['comments'] + df['shares'] + df['love'] + df['wow'] + df['haha'] + df['sad'] + df['angry'] + df['care']
    
    dataPage = df.groupby(['page']).size().reset_index()
    dataPage.columns = ['page','nombrePage']
    
    dataReaction = df.groupby(['page']).agg({'interaction':'sum'}).reset_index()
    dataReaction.columns = ['page','nombreReaction']
    
    dataFollowers = df.groupby(['page']).agg({'followers':'max'}).reset_index()
    
    #dataReactionPost = df.groupby(['page']).agg({'interaction':'max'}).reset_index()
    dataReactionPost = pd.concat([dataReaction['page'] , dataReaction['nombreReaction']/dataPage['nombrePage']],axis=1)
    dataReactionPost.columns = ['page','interaction'] 
    
    result = pd.merge(dataPage, dataReaction, on='page', how='inner')
    result = pd.merge(result, dataFollowers, on='page', how='inner')
    result = pd.merge(result, dataReactionPost, on='page', how='inner')
    return result


def preprocessVisu1_1_V1(data,col=1):
    data = preprocessVisu1_1(data)
    maxTableCol = 4
    colors = ['#1f77b4','#aec78e','#ff7f0e','#ffbb78','#2ca02c',
            '#98df8a','#d62728','#ff9896','#9467bd','#c5b0d5',
            '#8c564b','#c49c94','#e377c2','#f7b6d2','#7f7f7f',
            '#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']


    table = data.sort_values([data.columns[col]],ascending=[0]).head(20)['page'].rename(data.columns[col]).reset_index()
    table = table.drop(['index'], axis=1)
    table[data.columns[col]+"Color"] = colors
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