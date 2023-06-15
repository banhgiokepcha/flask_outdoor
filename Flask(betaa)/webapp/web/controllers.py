from sqlalchemy import desc, func
from flask import render_template, Blueprint, flash, redirect, url_for, current_app, render_template_string, request
from flask_login import login_required, current_user
from .models import db, Markers, Activity, Places
from ..auth.models import User
import folium 
from folium.plugins import Geocoder
from folium.map import Marker
from flask import jsonify
import json
import geopy
from geopy.geocoders import Nominatim

app_blueprint = Blueprint(
    'web',
    __name__,
    template_folder='./templates',
    #url_prefix="/main"
    )

@app_blueprint.route('/getmap')
def getMap():
    return redirect(url_for('web.mapView')) 

@app_blueprint.route('/maps')
@login_required
def map():
    return render_template('mapSearch.html')
 

@app_blueprint.route('/map')
@login_required
def mapView():
    users=User.query.all()
    map = folium.Map(width=800, height=600,location=[21.2820, 106.1975] , zoom_start=12)
    places = Places.query.all()
    for place in places:
        lat = place.latitude
        lon = place.longitude
        folium.Marker(
            location=[float(lat), float(lon)],
            popup = folium.Popup(
                html='<img src="https://res.cloudinary.com/dggvywzge/image/upload/v1684314331/cat_jwiq4j.jpg" width="100px" height="90px">',
            
            max_width=200,
            show=False,
            sticky=False,        
            lazy=True)
        ).add_to(map)
        

    iframe = map.get_root()._repr_html_()
    

    
    return render_template("mapTest.html", iframe=iframe, users=users)

@app_blueprint.route('/usermap/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_map(user_id):       

    return render_template('userMap.html', current_user=current_user)

@app_blueprint.route('/usermarkers', methods=['GET', 'POST']) 
@login_required
def get_markers():
    markers = Markers.query.filter_by(user_id=current_user.id).all()
    markers_data = []

    for marker in markers:
        # Extract the necessary attributes from the marker object
        marker_data = {
            'title': marker.title,
            'text': marker.text,
            'id': marker.id,
            'latitude': marker.latitude,
            'longitude': marker.longitude,
            # Add other attributes as needed
        }
        markers_data.append(marker_data)

    markers_json = json.dumps(markers_data)
    return markers_json

@app_blueprint.route('/new', methods=['GET','POST'])
@login_required
def create_new_marker():
    new_marker = Markers()
    new_marker.title = request.form['title']
    new_marker.text = request.form['text']
    new_marker.latitude= request.form.get('lat')
    new_marker.longitude = request.form.get('lon')
    new_marker.user_id = current_user.id
    try: 
      db.session.add(new_marker) 
      db.session.commit()
    except Exception as e:
      flash('Error adding your marker: %s' % str(e), 'error')
      print('error adding marker')
      db.session.rollback()
    else: 
      flash('Created marker successfully', "message")
      print(new_marker.latitude, new_marker.longitude)
      return redirect(url_for('.user_map', user_id=current_user.id))

@app_blueprint.route('/selectRegion')
@login_required
def render_map_by_region(region):
    if region == 'Bac Giang':
        map = folium.Map(width=800, height=600,location=[21.2820, 106.1975] , zoom_start=12)
    place01 = folium.Marker(
        location=[21.2820, 106.2072],
        popup = folium.Popup(
        html='<img src="https://res.cloudinary.com/dggvywzge/image/upload/v1684314331/cat_jwiq4j.jpg" width="100px" height="90px">',
        max_width=200,
        show=False,
        sticky=False,        
        lazy=True
    )).add_to(map)
    
@app_blueprint.route('/delete/<int:marker_id>', methods=['GET', 'POST'])
@login_required
def delete_marker(marker_id):
    marker_to_delete = Markers.query.filter_by(id=marker_id).first()
    if marker_to_delete is None: 
     print("Cannot delete selected marker")
     return "False"
    else:
     print(marker_to_delete)
     db.session.delete(marker_to_delete)
     db.session.commit()
     print("Deleted successfully")
     flash("Deleted") 
     return "True"
 
@app_blueprint.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('query')
    #filter_params = request.args
    places = Places.query.filter(Places.title.ilike(f'%{query}%'))
    results = places.all()
    results_data = []
    print(results)
    for result in results:
        result_data= {
        'name': result.title,
        'lat' : result.latitude,
        'lon' : result.longitude,
        'description': result.text
        }
        results_data.append(result_data) 
    
    return json.dumps(result_data)
    #return render_template("mapTest.html", results=results)
    
@app_blueprint.route('/places', methods = ['GET'])
@login_required
def mapSearch():
    places = Places.query.all()
    places_data = []
    for place in places:
        place_data= {
        'name': place.title,
        'lat' : place.latitude,
        'lon' : place.longitude,
        'description': place.text
        }
        places_data.append(place_data) 
    places_json = json.dumps(places_data)
    print(places_json)
    return places_json   
    
@app_blueprint.route('/edit', methods = ['GET', 'POST'])
     


