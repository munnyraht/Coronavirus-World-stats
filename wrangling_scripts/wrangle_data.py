import pandas as pd
import plotly.graph_objs as go
import requests
import json
import pandas as pd
import numpy as np

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
url = "https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true"
res = requests.get(url)
json_data = json.loads(res.text)
df = pd.DataFrame(json_data)
keepcolumns = ['infected', 'tested', 'recovered','deceased','country']
new_Df =df[keepcolumns]
new_Df = new_Df.replace('NA',np.nan)
lastUpdated = str(pd.to_datetime(df['lastUpdatedSource'][0]))[:10]

def return_figures():

  """Creates four plotly visualizations

  Args:
      None

  Returns:
      list (dict): list containing the four plotly visualizations

  """

  infected_df = new_Df[['infected','country']].dropna().sort_values(by = ['infected'])
  # first chart plots arable land from 1990 to 2015 in top 10 economies 
  # as a line chart
  graph_one = []    
  graph_one.append(
    go.Bar(
    y = infected_df['country'].tolist(),
    x = infected_df['infected'].tolist(),
    orientation = 'h'
    ),

  )

  layout_one = dict(title = 'Number of Infections',
              xaxis = dict(title = 'Infected'),
              yaxis = dict(title = 'Countries'),
              width=800,
              height=1000,

              )


  deceased_df = new_Df[['deceased','country']].dropna().sort_values(by = ['deceased']) 
  # second chart plots ararble land for 2015 as a bar chart    
  graph_two = []

  graph_two.append(
    go.Bar(
    y = deceased_df['country'].tolist(),
    x = deceased_df['deceased'].tolist(),
    orientation = 'h'
    )
  )

  layout_two = dict(title = 'Number of deaths',
              xaxis = dict(title = 'Countries',),
              yaxis = dict(title = 'deceased'),
              width=800,
              height=1000,

              )

  Recovered_df = new_Df[['recovered','country']].dropna().sort_values(by = ['recovered'])  
  # third chart plots percent of population that is rural from 1990 to 2015
  graph_three = []
  graph_three.append(
    go.Bar(
    y = Recovered_df['country'].tolist(),
    x = Recovered_df['recovered'].tolist(),
    orientation = 'h'

    )
  )

  layout_three = dict(title = 'Number of Recovery',
              xaxis = dict(title = 'Countries'),
              yaxis = dict(title = 'Recovered'),
              width=800,
              height=1000,
                     )


  # # fourth chart shows rural population vs arable land
  #     graph_four = []

  #     graph_four.append(
  #       go.Scatter(
  #       x = [20, 40, 60, 80],
  #       y = [10, 20, 30, 40],
  #       mode = 'markers'
  #       )
  #     )

  #     layout_four = dict(title = 'Chart Four',
  #                 xaxis = dict(title = 'x-axis label'),
  #                 yaxis = dict(title = 'y-axis label'),
  #                 )

  # append all charts to the figures list
  figures = []
  figures.append(dict(data=graph_one, layout=layout_one))
  figures.append(dict(data=graph_two, layout=layout_two))
  figures.append(dict(data=graph_three, layout=layout_three))
  # figures.append(dict(data=graph_four, layout=layout_four))

  return figures, lastUpdated