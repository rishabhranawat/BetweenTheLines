import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(186,58,51)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['AR', 'GA', 'KY', 'MO', 'UT', 'TX', 'WY'],
    name='Republican',
    showscale=False,
    text=['Arkansas', 'Georgia', 'Kentucky', 'Missouri', 'Utah', 'Texas', 'Wyoming'],
    zauto=False,
    zmax=1,
    zmin=0,
)
trace2 = Choropleth(
    z=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(68,94,150)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['CA', 'CI', 'DOC', 'IL', 'MD', 'NJ', 'NM', 'NY', 'OR', 'RI', 'VT'],
    name='Democrat',
    showscale=False,
    text=['California', 'Connecticut', 'District of Columbia', 'Illinois', 
          'Maryland', 'New Jersey', 'New Mexico', 'New York', 'Oregon',
          'Rhode Island', 'Vermont'],
    zauto=False,
    zmax=1,
    zmin=0,
)
trace3 = Choropleth(
    z=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255, 255, 255)'], [1, 'rgb(187, 170, 144)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['CO', 'FL', 'MI', 'MN', 'NH', 'OH', 'VA', 'WI'],
    name='Swing State',
    showscale=False,
    text=['Colorado', 'Florida', 'Michigan', 'Minnesota', 
          'New Hampshire', 'Ohio', 'Virginia', 'Wisconsin'],
    zauto=False,
    zmax=1,
    zmin=0,
)

data = Data([trace1, trace2, trace3])
layout = Layout(
    autosize=False,
    geo=dict(
        countrycolor='rgb(102, 102, 102)',
        countrywidth=0.1,
        lakecolor='rgb(255, 255, 255)',
        landcolor='rgba(237, 247, 138, 0.28)',
        lonaxis=dict(
            gridwidth=1.5999999999999999,
            range=[-180, -50],
            showgrid=False
        ),
        projection=dict(
            type='albers usa'
        ),
        scope='usa',
        showland=True,
        showrivers=False,
        showsubunits=True,
        subunitcolor='rgb(102, 102, 102)',
        subunitwidth=0.5
    ),
    hovermode='closest',
    images=list([
        dict(
            x=1,
            y=0.6,
            sizex=0.155,
            sizey=0.4,
            source='http://i.imgur.com/Xe3f1zg.png',
            xanchor='right',
            xref='paper',
            yanchor='bottom',
            yref='paper'
        )
    ]),
    showlegend=True,
    title='<b>PACE Approved legislation</b>',
    width= 800,
    margin = dict(
        l=0,
        r=50,
        b=100,
        t=100,
        pad=4)
)
fig = Figure(data=data, layout=layout)
py.iplot(fig, filename='pace')