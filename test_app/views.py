from django.shortcuts import render
import folium
import os
# Create your views here.

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(SETTINGS_DIR))
MAP_ROOT = os.path.join(PROJECT_ROOT, 'test_app/media/')

def index(request):
    if request.method == 'GET':
        f_map = folium.Map(location=[0,0], tiles='OpenStreetMap', zoom_start=3)
        folium.TileLayer("stamenwatercolor", attr='attr').add_to(f_map)
        folium.TileLayer("stamenterrain", attr='attr').add_to(f_map)
        folium.TileLayer("cartodbpositron", attr='attr').add_to(f_map)
        folium.LayerControl().add_to(f_map)
        save_map(f_map.get_root().render(), 'test_map')
        return render(request, 'index.html', {'map': f_map.get_root().render()})


def save_map(map_html, filename):
    try:
        with open(MAP_ROOT+filename, "w") as file:
            file.write(map_html)
            return True
    except FileNotFoundError as e:
        print(f'{e} while writing map to file')
        return False