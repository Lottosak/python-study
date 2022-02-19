import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

def marker_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[41.2242,-115.597304], zoom_start=6, tiles="Mapbox bright")


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

fgm = folium.FeatureGroup(name="Markers")
for place in data.iterrows():
    fgm.add_child(
        folium.CircleMarker(location=[place[1]['LAT'],place[1]['LON']],
        radius=6,
        popup=str(place[1]['ELEV'])+"m",
        fill_color=marker_color(place[1]['ELEV']),
        color="grey",
        fill_opacity=0.7
        )
    )

map.add_child(fgp)
map.add_child(fgm)
map.add_child(folium.LayerControl())
map.save("webmap.html")