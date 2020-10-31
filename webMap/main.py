import pandas
import folium

# import and prepare data
volcanoes = pandas.read_csv("Volcanoes.txt")
lat = list(volcanoes.loc[:, "LAT"])
lon = list(volcanoes.loc[:, "LON"])
name = list(volcanoes.loc[:, "NAME"])

length = len(volcanoes)

# create a map of volcanoes
map_volcanoes = folium.Map(location=[41.520164, -100.320301], zoom_start=5, tiles="Stamen Watercolor")

# create a layer for markers and add markers
markers_layer = folium.FeatureGroup(name="markers")

for index in range(length):
    markers_layer.add_child(
        folium.Marker(location=[lat[index], lon[index]], popup=name[index], icon=folium.Icon(color="green")))

map_volcanoes.add_child(markers_layer)
map_volcanoes.save("MapVolcanoes.html")
