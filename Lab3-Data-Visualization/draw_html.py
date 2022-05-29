# -*- coding: UTF-8 -*-
"""
 # @Project     : Lab3-Data-Visualization
 # @File        : draw_html.py
 # #@Author     : mount_potato
 # @Date        : 2022/5/29 21:01
"""

from dash import dcc, html


def div_dropdown(title, content_list, style):
    return html.Div(
        [
            dcc.Dropdown(
                id=title,
                options=[{'label': i, 'value': i} for i in content_list],
                value=content_list[0]
            )
        ],
        style=style
    )


def div_non_animate_graph(title, style):
    return html.Div(
        [
            dcc.Graph(
                id=title,
            )
        ],
        style=style
    )

def div_graph(title, style):
    return html.Div(
        [
            dcc.Graph(
                id=title,
                animate=True
            )
        ],
        style=style
    )


def div_radio_bar(title,content_list,style):
    return html.Div(
        [
            dcc.RadioItems(
                id=title,
                options=[{'label': i, 'value': i} for i in content_list],
                value=content_list[0],
                labelStyle={'padding': '0 20px', 'display': 'inline-block'}
            )
        ],
        style=style
    )

