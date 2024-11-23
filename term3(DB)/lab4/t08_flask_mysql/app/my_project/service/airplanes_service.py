from t08_flask_mysql.app.my_project.dao.airplanes_dao import AirplanesDAO
from t08_flask_mysql.app.my_project.domain.airplanes import Airplane

class AirplanesService:
    @staticmethod
    def get_all_airplanes():
        return AirplanesDAO.get_all_airplanes()

    @staticmethod
    def get_airplane_by_id(airplane_id):
        return AirplanesDAO.get_airplane_by_id(airplane_id)

    @staticmethod
    def create_airplane(registration_number, model, total_flight_hours, airline_id):
        return AirplanesDAO.create_airplane(registration_number, model, total_flight_hours, airline_id)

    @staticmethod
    def update_airplane(airplane_id, registration_number, model, total_flight_hours, airline_id):
        return AirplanesDAO.update_airplane(airplane_id, registration_number, model, total_flight_hours, airline_id)

    @staticmethod
    def delete_airplane(airplane_id):
        return AirplanesDAO.delete_airplane(airplane_id)

    @staticmethod
    def get_all_airplanes_detailed():
        return AirplanesDAO.get_all_airplanes_detailed()