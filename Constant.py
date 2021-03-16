BATTERY_PARAM_CHARACTERISTICS = {
    'cell_temperature_in_celsius': {
        'lower_safety_limit': 0,
        'upper_safety_limit': 45,
        'tolerance': 0.05,
        'sensor_accuracy': 1,
        'sensor_limits': {
            'min': -60,
            'max': 100
        },
        'console': True
    },
    'soc_in_percent': {
        'lower_safety_limit': 25,
        'upper_safety_limit': 75,
        'tolerance': 0.05,
        'sensor_accuracy': 0.1,
        'sensor_limits': {
            'min': 0,
            'max': 100
        },
        'console': True
    },
    'charge_rate_in_c_rate': {
        'lower_safety_limit': 0.5,
        'upper_safety_limit': 0.8,
        'tolerance': 0.05,
        'sensor_accuracy': 0.01,
        'sensor_limits': {
            'min': 0,
            'max': 1
        },
        'console': True
    }
}
# In descending order of severity
PARAM_OPERATING_RANGE_CLASSIFIER = [
    'ALERT_VALUENAN',
    'ALERT_PARAMNAMEUNKNOWN',
    'ALERT_MINOUTOFRANGE',
    'ALERT_MAXOUTOFRANGE',
    'ALERT_UNDERLIMIT',
    'ALERT_OVERLIMIT',
    'WARN_NEARUNDERLIMIT',
    'WARN_NEAROVERLIMIT',
    'INFO_NORMAL',
]

BATTERY_STATUS_CLASSIFIER = [
    'ALERT_BATTERYNOK',
    'INFO_BATTERYOK'
]
PARAM_OK = ["WARN", "INFO"]
PARAM_NOK = ["ALERT"]
LOCALIZATION_SUPPORT = ["en-US", "de-DE"]