from flask import Flask, jsonify, request
from redis import Redis
import os

app = Flask(__name__)

redis_client = Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), decode_responses=True)

# Initialize some example data on startup
def init_data():
    redis_client.geoadd("locations", [
        -73.965355, 40.782865, "Central Park",
        -73.985130, 40.758896, "Times Square",
        -74.044500, 40.689247, "Statue of Liberty"
    ], nx=True)

# Run initialization only if the key doesn't exist
if not redis_client.exists("locations"):
    init_data()

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = []
    for member in redis_client.zrange("locations", 0, -1):
        lon, lat = redis_client.geopos("locations", member)[0]
        locations.append({"name": member, "longitude": lon, "latitude": lat})
    return jsonify(locations)

@app.route('/locations/add', methods=['POST'])
def add_location():
    data = request.get_json()
    name = data.get('name')
    lon = float(data.get('longitude'))
    lat = float(data.get('latitude'))
    
    if not all([name, lon, lat]):
        return jsonify({"error": "Missing name, longitude, or latitude"}), 400
    
    redis_client.geoadd("locations", [lon, lat, name], nx=True)
    return jsonify({"message": f"Added {name}"}), 201

@app.route('/locations/near', methods=['GET'])
def get_nearby_locations():
    try:
        lon = float(request.args.get('lon'))
        lat = float(request.args.get('lat'))
        radius = float(request.args.get('radius', 1000))  # meters
        unit = request.args.get('unit', 'm')  # m, km, mi, ft
        
        results = redis_client.georadius("locations", lon, lat, radius, unit=unit, withcoord=True)
        locations = [
            {"name": name, "longitude": float(coord[0]), "latitude": float(coord[1])}
            for name, coord in results
        ]
        return jsonify(locations)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)