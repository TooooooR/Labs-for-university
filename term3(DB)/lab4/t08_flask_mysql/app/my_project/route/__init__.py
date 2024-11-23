from t08_flask_mysql.app.my_project.controller.airlines_controller import airlines_bp
from t08_flask_mysql.app.my_project.controller.airplanes_controlle import airplanes_bp, airplanes_detailed_bp
from t08_flask_mysql.app.my_project.controller.flights_controller import flights_bp, flights_crew_bp


def register_routes(app):
    app.register_blueprint(airlines_bp, url_prefix='/airlines')
    app.register_blueprint(airplanes_bp, url_prefix='/airplanes')
    app.register_blueprint(flights_bp, url_prefix='/flights')
    app.register_blueprint(airplanes_detailed_bp, url_prefix='/airplanes/details')
    app.register_blueprint(flights_crew_bp, url_prefix='/flights/details')
    