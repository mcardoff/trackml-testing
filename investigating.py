import os
import pandas as pd
import plotly.express as px
import random
# import matplotlib.pyplot as plt
from trackml.dataset import load_event

event_prefix = 'event000001000'
hits, cells, particles, truth = load_event(os.path.join('./input/train_100_events', event_prefix))

volume_id_8 = hits[(hits["volume_id"] == 8) & (hits["layer_id"] == 2)]
volume_id_13 = hits[(hits["volume_id"] == 13) & (hits["layer_id"] == 2)]
particle_ids = truth.particle_id.unique()
# print(len(particle_ids))

particles_to_plot = random.sample(list(particle_ids), 10)
print(particles_to_plot)

tracks = hits.iloc[truth[(truth["particle_id"].isin(particles_to_plot))]["hit_id"].index,:]

print(tracks.head())

## plotly code, opens in browser
# fig = px.scatter_3d(truth[truth['particle_id'] == 22525763437723648], x='tx', y='ty', z='tz')
fig = px.scatter_3d(tracks, x='x', y='y', z='z', color='volume_id')
fig.update_traces(marker=dict(size=2))
fig.show()
