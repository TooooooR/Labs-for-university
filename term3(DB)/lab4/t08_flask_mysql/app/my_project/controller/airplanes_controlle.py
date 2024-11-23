from flask import Blueprint, request, jsonify
from t08_flask_mysql.app.my_project.service.airplanes_service import AirplanesService

airplanes_bp = Blueprint('airplanes', __name__)
airplanes_detailed_bp = Blueprint('airplanes_detailed', __name__)

@airplanes_detailed_bp.route('/', methods=['GET'])
def get_all_airplanes_detailed():
    airplanes_detailed = AirplanesService.get_all_airplanes_detailed()
    return jsonify(airplanes_detailed)

@airplanes_bp.route('/', methods=['GET'])
def get_all_airplanes():
    airplanes = AirplanesService.get_all_airplanes()
    return jsonify([
        {
            "id": a.id,
            "registration_number": a.registration_number,
            "model": a.model,
            "total_flight_hours": a.total_flight_hours,
            "airline_id": a.airline_id
        } for a in airplanes
    ])

@airplanes_bp.route('/<int:airplane_id>', methods=['GET'])
def get_airplane_by_id(airplane_id):
    airplane = AirplanesService.get_airplane_by_id(airplane_id)
    if airplane:
        return jsonify({
            "id": airplane.id,
            "registration_number": airplane.registration_number,
            "model": airplane.model,
            "total_flight_hours": airplane.total_flight_hours,
            "airline_id": airplane.airline_id
        })
    return jsonify({"error": "Airplane not found"}), 404

@airplanes_bp.route('/', methods=['POST'])
def create_airplane():
    data = request.get_json()
    airplane = AirplanesService.create_airplane(
        data['registration_number'],
        data['model'],
        data['total_flight_hours'],
        data['airline_id']
    )
    return jsonify({
        "id": airplane.id,
        "registration_number": airplane.registration_number,
        "model": airplane.model,
        "total_flight_hours": airplane.total_flight_hours,
        "airline_id": airplane.airline_id
    }), 201

@airplanes_bp.route('/<int:airplane_id>', methods=['PUT'])
def update_airplane(airplane_id):
    data = request.get_json()
    airplane = AirplanesService.update_airplane(
        airplane_id,
        data['registration_number'],
        data['model'],
        data['total_flight_hours'],
        data['airline_id']
    )
    if airplane:
        return jsonify({
            "id": airplane.id,
            "registration_number": airplane.registration_number,
            "model": airplane.model,
            "total_flight_hours": airplane.total_flight_hours,
            "airline_id": airplane.airline_id
        })
    return jsonify({"error": "Airplane not found"}), 404

@airplanes_bp.route('/<int:airplane_id>', methods=['DELETE'])
def delete_airplane(airplane_id):
    success = AirplanesService.delete_airplane(airplane_id)
    if success:
        return jsonify({"message": "Airplane deleted"}), 204
    return jsonify({"error": "Airplane not found"}), 404
