from math import isnan
from Constant import BATTERY_PARAM_CHARACTERISTICS, \
    PARAM_OPERATING_RANGE_CLASSIFIER, \
    PARAM_OK, \
    PARAM_NOK, \
    BATTERY_STATUS_CLASSIFIER
from reporter import report_parameters
from battery_param_range_handler import generate_operating_ranges, snap_limits_to_sensor_accuracy


def identify_battery_param_range_for_valid_param(battery_param_value, battery_param_operating_ranges):
    for operating_range_classifier, operating_range in battery_param_operating_ranges.items():
        if operating_range[0] <= battery_param_value < operating_range[1]:
            return operating_range_classifier


def identify_battery_param_operating_range(battery_param_name, battery_param_value):
    if isnan(battery_param_value):
        return PARAM_OPERATING_RANGE_CLASSIFIER[0]
    elif battery_param_name not in BATTERY_PARAM_CHARACTERISTICS:
        return PARAM_OPERATING_RANGE_CLASSIFIER[1]
    battery_param_operating_ranges = generate_operating_ranges(battery_param_name)
    battery_param_operating_ranges = snap_limits_to_sensor_accuracy(battery_param_name, battery_param_operating_ranges)
    return identify_battery_param_range_for_valid_param(battery_param_value, battery_param_operating_ranges)


def is_param_ok_to_operate(battery_param_status):
    alert_type = battery_param_status.split('_')[0]
    if alert_type in PARAM_OK:
        return True
    elif alert_type in PARAM_NOK:
        return False


def is_battery_ok(**battery_params):
    battery_params_ok = []
    for battery_param_name in battery_params:
        battery_param_operating_zone = identify_battery_param_operating_range(
            battery_param_name,
            battery_params[battery_param_name])
        print(report_parameters(
            battery_param_name,
            battery_param_operating_zone
        ))
        battery_param_ok = is_param_ok_to_operate(battery_param_operating_zone)
        battery_params_ok.append(battery_param_ok)
    print("*" * 100)
    return [BATTERY_STATUS_CLASSIFIER[1] if all(battery_params_ok) else BATTERY_STATUS_CLASSIFIER[0]][0]