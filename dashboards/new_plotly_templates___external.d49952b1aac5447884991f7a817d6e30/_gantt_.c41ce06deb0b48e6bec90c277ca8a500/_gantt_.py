# PERISCOPE GANTT CHART TEMPLATE
# SQL output should have 3 columns:
#    1) task: the name of the task
#    2) start: a date indicating when the task has started or is scheduled to start
#    2) finish: a date indicating when the task has ended or is scheduled to end

# Import Libraries
import pandas as pd
import plotly.plotly as py
import plotly.figure_factory as ff

# Create dummy data
community_post = 'https://community.periscopedata.com/t/63s966'
dummy_df = pd.DataFrame()
dummy_df['task'] = ['Task 1', 'Task 2', 'Task 3']
dummy_df['start'] = ['2019-02-07', '2018-12-24', '2018-11-09']
dummy_df['finish'] = ['2019-03-08', '2019-05-08', '2019-04-08']

# HELPER FUNCTIONS
def style_link(text, link, **settings):
  style = ';'.join([f'{key.replace("_","-")}:{settings[key]}' for key in settings])
  return f'<a href="{link}" style="{style}">{text}</a>'

# MAIN FUNCTION
def plot(df, annotation=None):
  # Create and assign list of column names
  df.columns = [c.title() for c in df.columns]

  # Use figure factory to create gantt chart
  fig = ff.create_gantt(df)
  if annotation is not None:
    fig['layout']['annotations'] = [annotation]
  periscope.plotly(fig)

  
try:
  plot(df)
except Exception as e:
	print(e)
	annotation = {
    'x': 0.5,
    'y': 0.5,
    'ax': 0,
    'ay': 0,
    'xref': 'paper',
    'yref': 'paper',
    'text': style_link('DUMMY<br><br><br><br>DATA<br><br><br><br>EXAMPLE', community_post, font_size='60px', font_weight='bold', color='rgba(0, 0, 0, .25)'),
    'showarrow': False,
    'textangle': -25
  }
	plot(dummy_df, annotation=annotation)
