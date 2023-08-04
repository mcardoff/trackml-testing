import os
from trackml.dataset import load_event

event_prefix = 'event000001000'
hits, cells, particles, truth = load_event(os.path.join('./input/train_100_events', event_prefix))
