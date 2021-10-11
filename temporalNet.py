import pathpy as pp

t = pp.TemporalNetwork()
t.add_edge('a', 'b', 1)
t.add_edge('b', 'a', 3)
t.add_edge('b', 'c', 3)
t.add_edge('d', 'c', 4)
t.add_edge('c', 'd', 5)
t.add_edge('c', 'b', 6)
#print(t)

style = {
  'ts_per_frame': 1,
  'ms_per_frame': 2000,
  'look_ahead': 2,
  'look_behind': 2,
  'node_size': 15,
  'inactive_edge_width': 2,
  'active_edge_width': 4,
  'label_color' : '#ffffff',
  'label_size' : '24px',
  'label_offset': [0,5]
  }
#pp.visualisation.plot(t, **style)

#pp.visualisation.export_html(t, 'my_temporal_network.html', **style)


p = pp.Paths()
p.add_path(('a', 'c', 'd'), frequency=10)
print(p)
