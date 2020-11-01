import pandas
import folium

# import and prepare data
volcanoes = pandas.read_csv("Volcanoes.txt")
lat = list(volcanoes.loc[:, "LAT"])
lon = list(volcanoes.loc[:, "LON"])
name = list(volcanoes.loc[:, "NAME"])
elev = list(volcanoes.loc[:, "ELEV"])


def color_elevation(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <3000:
        return "orange"
    else:
        return "purple"


# create a map of volcanoes
map_volcanoes = folium.Map(location=[41.520164, -100.320301], zoom_start=5, tiles="Stamen Watercolor")

# create a layer for markers and add markers
markers_layer = folium.FeatureGroup(name="markers")

for lt, ln, n, e in zip(lat, lon, name, elev):
    markers_layer.add_child(
        folium.Marker(location=[lt, ln], popup=f"Name: {n} Height: {e}m", icon=folium.Icon(color=color_elevation(e))))

map_volcanoes.add_child(markers_layer)
map_volcanoes.save("MapVolcanoes.html")
