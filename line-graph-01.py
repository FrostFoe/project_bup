import plotly.graph_objs as go

# Data
years = list(range(1990, 2025))
male = [84.827,83.924,83.056,82.228,81.442,80.697,79.994,79.336,78.706,78.093,77.519,76.973,76.46,75.986,75.551,75.148,74.774,74.431,74.114,73.821,73.55,73.298,73.063,72.842,72.636,72.437,72.247,72.062,71.884,71.709,71.538,71.368,71.2,71.033,70.871]
female = [34.318,34.781,35.257,35.748,36.257,36.782,37.322,37.876,38.441,39.016,39.601,40.19,40.783,41.385,41.997,42.616,43.238,43.864,44.49,45.118,45.742,46.363,46.975,47.575,48.163,48.736,49.294,49.836,50.362,50.871,51.361,51.834,52.292,52.736,53.167]
total = [57.125,57.001,57.065,57.186,57.348,57.545,57.77,58.017,58.28,58.557,58.847,59.146,59.45,59.761,60.076,60.392,60.707,61.019,61.325,61.623,61.912,62.19,62.456,62.709,62.947,63.17,63.376,63.567,63.742,63.901,64.044,64.172,64.284,64.383,64.471]

# Create traces
trace1 = go.Scatter(x=years, y=male, mode='lines+markers', name='Male', line=dict(color='blue'))
trace2 = go.Scatter(x=years, y=female, mode='lines+markers', name='Female', line=dict(color='red'))
trace3 = go.Scatter(x=years, y=total, mode='lines+markers', name='Total', line=dict(color='green'))

layout = go.Layout(
    title='Labor Force Participation Rate in Bangladesh (1990–2024)',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Participation Rate (%)'),
    hovermode='x unified'
)

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
fig.show()
