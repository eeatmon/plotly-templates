# SQL output is imported as a dataframe variable called 'df'
import pandas as pd 
import plotly.plotly as py
import plotly.graph_objs as go

line = go.Scatter(
  x = df['week'],
  y = df['count'],
  name = 'Signups',
  mode = 'lines',
  line = {
    'shape': 'spline',
    'smoothing': 1.3
  }
)

layout = layout = {
  'margin': {
    'l': 50,
    'r': 0,
    'b': 50,
    't': 0
  },
  'yaxis': {
    'title': 'Signups'
  },
  'xaxis': {
    'title': 'Week'
  }
}

fig = dict(data = [line], layout = layout)

periscope.plotly(fig)
