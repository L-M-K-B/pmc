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
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "purple"


# create a map of volcanoes
new_map = folium.Map(location=[41.520164, -100.320301], zoom_start=5, tiles="Stamen Toner")

# create a layer for volcanoes
layer_volcanoes = folium.FeatureGroup(name="volcanoes")

for lt, ln, n, e in zip(lat, lon, name, elev):
    layer_volcanoes.add_child(
        folium.CircleMarker(location=(lt, ln), popup=f"Name: {n} Height: {e}m", color="black", fill=True,
                            fill_color=color_elevation(e), fill_opacity=0.7))

new_map.add_child(layer_volcanoes)

# create a layer for the population
layer_population = folium.FeatureGroup(name="population")

layer_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x:
{"fillColor": "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"][
    "POP2005"] < 20000000 else "red" if 20000000 <= x["properties"][
    "POP2005"] < 50000000 else "darkpurple"}))

new_map.add_child(layer_population)

# create a control panel in order to turn single layers on and off
new_map.add_child(folium.LayerControl())

new_map.save("new_map.html")
