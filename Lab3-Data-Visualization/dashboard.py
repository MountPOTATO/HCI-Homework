# -*- coding: UTF-8 -*-
"""
 # @Project     : Lab3-Data-Visualization
 # @File        : dashboard.py
 # #@Author     : mount_potato
 # @Date        : 2022/5/29 20:07
"""

import dash
import plotly.express as px
import plotly.graph_objs as go
from dash import dcc, html
from draw_html import *
import pandas as pd
import numpy as np
from utils import *

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dropdown_css = {'width': '40%', 'display': 'inline-block', 'padding': '10px 50px','margin-top':"2%"}
radio_css = {'padding': '10px 50px', 'margin': '0 auto','margin-bottom':'1%'}
pie_css={'width': '50%','margin-top':'2%'}
graph_css = {'width': '40%', 'margin-top': '1%', 'display': 'inline-block'}

df = pd.read_csv(r"data/googleDataVis.csv")

# data filter

category_list = df['Category'].unique()
type_list = ['Free', 'Paid']
rating_list = df['Content Rating'].unique()

app.layout = html.Div([

    html.Div([
        div_graph('rating-graph', pie_css),

        div_dropdown('Category', category_list, dropdown_css),

        div_dropdown('Type', type_list, dropdown_css),



    ]),

    div_radio_bar('rating-radio', rating_list, radio_css),




    html.Div([

        div_graph('installs-rating', graph_css), # installs-rating 柱状图

        div_graph('reviews-rating', graph_css),  # Review-Rating 柱状图

        div_graph('reviews-installs', graph_css), # Review-Installs 散点图

        div_graph('installs-size', graph_css),  # Installs-Size 折线图

    ]),

])




@app.callback(
    dash.dependencies.Output('rating-graph', 'figure'),
    [
        dash.dependencies.Input('Category', 'value'),
        dash.dependencies.Input('Type', 'value'),
    ])
def refresh_pie(category, type):
    dff = df[(df['Category'] == category) & (df['Type'] == type)]

    label_list = list(rating_list)
    value_list = [0 for _ in range(len(label_list))]

    for index, row in dff.iterrows():
        value_list[label_list.index(row[8])] += 1

    return create_pie(label_list,value_list)





@app.callback(
    dash.dependencies.Output('installs-size', 'figure'),
    [
        dash.dependencies.Input('Category', 'value'),
        dash.dependencies.Input('Type', 'value'),
        dash.dependencies.Input('rating-radio', 'value')
    ]
)
def refresh_install_size_line_graph(category, type, radio):
    dff = df[(df['Category'] == category) & (df['Content Rating'] == radio) & (df['Type'] == type)]

    installs, sizes = [0, 0, 0, 0, 0, 0, 0, 0], []
    sizes = [
        '0~300k', '300k~600k', '600k~900k', '900k~25m', '25m~50m',
        '50m~75m', '75m~100m', 'Varies with device'
    ]
    for index, row in dff.iterrows():
        if row['Size'] == 'Varies with device':
            installs[-1] += row['Installs']

        else:
            tmp=float(row['Size'][:-1])
            i=int(tmp//300) if row['Size'][-1] == 'k' else int(tmp//25)+3
            installs[i] += row['Installs']

    return create_line_graph(sizes,'Size',installs,'Installs','Installs-Size Line Graph')




@app.callback(
    dash.dependencies.Output('reviews-installs', 'figure'),
    [
        dash.dependencies.Input('Category', 'value'),
        dash.dependencies.Input('Type', 'value'),
        dash.dependencies.Input('rating-radio', 'value')
    ]
)
def refresh_review_install_scatter(category, type, radio):

    dff = df[(df['Category'] == category) & (df['Content Rating'] == radio) & (df['Type'] == type)]

    reviews, installs, names = [], [], []
    for index, row in dff.iterrows():
        reviews.append(row['Reviews'])
        installs.append(row['Installs'])
        names.append(row['App'])

    return create_scatter(installs, 'Installs', reviews, 'Reivews', names, 'Reviews-Installs Scatter Diagram')



@app.callback(
    dash.dependencies.Output('installs-rating', 'figure'),
    [
        dash.dependencies.Input('Category', 'value'),
        dash.dependencies.Input('Type', 'value'),
        dash.dependencies.Input('rating-radio', 'value')
    ]
)
def refresh_install_rating_bar(category, type, radio):

    dff = df[(df['Category'] == category) & (df['Content Rating'] == radio) & (df['Type'] == type)]

    installs = [0, 0, 0, 0, 0, 0]
    ratings = ['0~1', '1~2', '2~3', '3~4', '4~5', '5+']
    for index, row in dff.iterrows():
        if not np.isnan(row['Rating']):
            installs[int(float(row['Rating']))] += row['Installs']


    return create_bar(ratings,"Rating",installs,"Install","Installs-Rating Bar Diagram")



# reviews-rating柱状图
@app.callback(
    dash.dependencies.Output('reviews-rating', 'figure'),
    [
        dash.dependencies.Input('Category', 'value'),
        dash.dependencies.Input('Type', 'value'),
        dash.dependencies.Input('rating-radio', 'value')
    ]
)
def update_RI_scatters(category, type, radio):
    dff = df[(df['Category'] == category) & (df['Content Rating'] == radio) & (df['Type'] == type)]

    reviews = [0, 0, 0, 0, 0, 0]
    ratings = ['0~1', '1~2', '2~3', '3~4', '4~5', '5+']
    for index, row in dff.iterrows():
        if not np.isnan(row['Rating']):
            reviews[int(float(row['Rating']))] += row['Reviews']

    return create_bar(ratings,"Rating",reviews,"Reviews","Review-Rating Bar Diagram")



if __name__ == '__main__':
    app.run_server(debug=True, host='localhost')
