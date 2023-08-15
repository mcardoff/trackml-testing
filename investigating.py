import os
import pandas as pd
import plotly.express as px
# import matplotlib.pyplot as plt
from trackml.dataset import load_event

event_prefix = 'event000001000'
hits, cells, particles, truth = load_event(os.path.join('./input/train_100_events', event_prefix))

volume_id_8 = hits[hits["volume_id"] == 8]

## plotly code, opens in browser
fig = px.scatter_3d(volume_id_8, x=volume_id_8.x, y=volume_id_8.y, z=volume_id_8.z)
fig.show()
