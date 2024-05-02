import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np


df=pd.read_csv("covid_19_data.csv")

df_ts=df.groupby(['ObservationDate']).sum()
df_bd=df.where(df['Country/Region']=='Bangladesh')


df1=df.where(df.ObservationDate==max(df.ObservationDate))
df2=df1.groupby('Country/Region').sum()
df3=df2.sort_values(by='Deaths',ascending=False)
df3=df3.head(20)


app=dash.Dash()
app.layout= html.Div([
    html.H1('COVID-19 Dashboard'),
    
    dcc.Graph(
        id='line_bd',
        figure={            
                'data':[ 
                {'x': df_bd.ObservationDate, 'y': df_bd.Confirmed,'type':'bar','name':'Confirmed_bd'},
                {'x': df_bd.ObservationDate, 'y': df_bd.Deaths,'type':'bar','name':'Deaths_bd', 'marker' : { "color" : 'rgb(255,0,0)'}},
                {'x': df_bd.ObservationDate, 'y': df_bd.Recovered,'type':'bar','name':'Recovered_bd', 'marker' : { "color" : 'rgb(0,128,0)'}}
                        ],
                'layout':go.Layout(title='Bangladesh Time Series Cases')           
                }
            ),
    
     dcc.Graph(
        id='line',
        figure={            
                'data':[ 
                {'x': df_ts.index, 'y': df_ts.Confirmed,'name':'Confirmed'},
                {'x': df_ts.index, 'y': df_ts.Deaths,'name':'Deaths', 'marker' : { "color" : 'rgb(255,0,0)'}},
                {'x': df_ts.index, 'y': df_ts.Recovered,'name':'Recovered', 'marker' : { "color" : 'rgb(0,128,0)'}}
                        ],
                'layout':go.Layout(title='Worldwide Time Series Cases')           
                }
            ),
    
    dcc.Graph(
        id='confirmed',
        figure={            
                'data':[
                {'x': df3.index, 'y': df3.Confirmed, 'type':'bar','name':'Confirmed'}
                        ],
                'layout':go.Layout(title='Confirmed Cases by Country')           
                }
            ),
    
    dcc.Graph(
        id='death',
        figure={            
                'data':[                
                {'x': df3.index, 'y': df3.Deaths, 'type':'bar','name':'Deaths', 'marker' : { "color" : 'rgb(255,0,0)'}}
                        ],
                'layout':go.Layout(title='Death Cases by Country')            
                }
            ),
    
    dcc.Graph(
        id='recovered',
        figure={            
                'data':[              
                {'x': df3.index, 'y': df3.Recovered, 'type':'bar','name':'Recovered', 'marker' : { "color" : 'rgb(0,128,0)'}}
                        ],
                'layout':go.Layout(title='Recovered Cases by Country')            
                }
            )
])



if __name__=="__main__":
    app.run_server(port=4051)