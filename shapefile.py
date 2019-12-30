
import matplotlib.pyplot as plt
import geopandas as gpd

city_name = "Jaipur"

# import shapefile using geopandas
natural = gpd.read_file('BB/'+city_name+'/shape/natural.shp')
waters = gpd.read_file('BB/'+city_name+'/shape/waterways.shp')
rails = gpd.read_file('BB/'+city_name+'/shape/railways.shp')
roads = gpd.read_file('BB/'+city_name+'/shape/roads.shp')

fig, ax = plt.subplots(figsize = (10,10))
natural.plot(ax=ax, color= "green")
waters.plot(ax=ax)
rails.plot(ax=ax, color = 'magenta')
roads.plot(ax=ax, color = 'black')

plt.show()
