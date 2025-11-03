import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENROUTESERVICE_API_KEY = os.getenv('OPENROUTESERVICE_API_KEY')

# Default routes
DEFAULT_ORIGIN = "Munich, Germany"
DEFAULT_DESTINATION = "Stuttgart, Germany"

# Vehicle parameters
BMW_I4_PARAMS = {
    'vehicle_name': 'BMW i4 eDrive40',
    'vehicle_mass': 2100,
    'drag_coefficient': 0.24,
    'frontal_area': 2.3,
    'battery_capacity': 83.9,
    'drivetrain_efficiency': 0.95,
    'rolling_resistance': 0.01,
    'air_density': 1.225,
    'regenerative_braking_efficiency': 0.7,
    'auxiliary_power': 0.5
}
