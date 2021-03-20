# import matplotlib.pyplot as plt
# import geopandas
#
# states = geopandas.read_file('../../data/mapping/tl_2020_us_state.shp')
# type(states)
#
# states = states.to_crs("EPSG:3395")
#
# states.plot()
#
# states.boundary.plot()
#
# states.plot(cmap='magma', figsize=(12, 12))
#
# # states[states['NAME'] == 'Texas']
# #
# # states[states['NAME'] == 'Texas'].plot(figsize=(12, 12))
# #
# # west = states[states['region'] == 'West']
# #
# # west.plot(cmap='Pastel2', figsize=(12, 12))
# #
# # fig = plt.figure(1, figsize=(25,15))
# # ax = fig.add_subplot()
# #
# # west.apply(lambda x: ax.annotate(s=x.NAME, xy=x.geometry.centroid.coords[0], ha='center', fontsize=14),axis=1);
# #
# # west.boundary.plot(ax=ax, color='Black', linewidth=.4)
# #
# # west.plot(ax=ax, cmap='Pastel2', figsize=(12, 12))
# #
# # ax.text(-0.05, 0.5, 'https://jcutrer.com', transform=ax.transAxes,
# #         fontsize=20, color='gray', alpha=0.5,
# #         ha='center', va='center', rotation='90')
# #
# #
# # us_boundary_map = states.boundary.plot(figsize=(18, 12), color="Gray")
# # west.plot(ax=us_boundary_map,  color="DarkGray")
#
# west = states[states['region'] == 'West']
# southwest = states[states['region'] == 'Southwest']
# southeast = states[states['region'] == 'Southeast']
# midwest = states[states['region'] == 'Midwest']
# northeast = states[states['region'] == 'Northeast']
#
# us_boundary_map = states.boundary.plot(figsize=(18, 12), color='Black', linewidth=.5)
#
# west.plot(ax=us_boundary_map,  color="MistyRose")
#
# southwest.plot(ax=us_boundary_map, color="PaleGoldenRod")
#
# southeast.plot(ax=us_boundary_map, color="Plum")
#
# midwest.plot(ax=us_boundary_map, color="PaleTurquoise")
#
# final_map = northeast.plot(ax=us_boundary_map, color="LightPink")
#
#
# import geopandas as gpd
# from shapely.geometry import Point, Polygon
# import matplotlib.pyplot as plt
# import pandas as pd
# # matplotlib inline
#
# usa = gpd.read_file('../../data/mapping/tl_2020_us_state.shp')
# usa.head()
#
# usa.tail(2)
# usa.plot()
#
