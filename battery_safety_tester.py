from math import isnan
from Constant import BATTERY_PARAM_CHARACTERISTICS, \
    PARAM_OPERATING_RANGE_CLASSIFIER, \
    BATTERY_STATUS_CLASSIFIER
from accumulator import accumulate_unsafe_params
from reporter import report_params
from battery_param_range_handler import classify_operating_ranges, snap_range_limits_to_sensor_accuracy


def identify_battery_param_range_for_valid_param(battery_param_value, battery_param_operating_ranges):
    for operating_range_classifier, operating_range in battery_param_operating_ranges.items():
        if operating_range[0] <= battery_param_value < operating_range[1]:
            return operating_range_classifier


def identify_battery_param_operating_range(battery_param_name, battery_param_value):
    if isnan(battery_param_value):
        return PARAM_OPERATING_RANGE_CLASSIFIER[0]
    elif battery_param_name not in BATTERY_PARAM_CHARACTERISTICS:
        return PARAM_OPERATING_RANGE_CLASSIFIER[1]
    battery_param_operating_ranges = classify_operating_ranges(battery_param_name)
    battery_param_operating_ranges = snap_range_limits_to_sensor_accuracy(battery_param_name,
                                                                          battery_param_operating_ranges)
    return identify_battery_param_range_for_valid_param(battery_param_value, battery_param_operating_ranges)


def is_battery_ok(**battery_params):
    battery_params_operating_ranges = {}
    for battery_param_name in battery_params:
        battery_params_operating_ranges[battery_param_name] = identify_battery_param_operating_range(
            battery_param_name,
            battery_params[battery_param_name])
    unsafe_params = accumulate_unsafe_params(battery_params_operating_ranges)
    report_params(unsafe_params)
    return [BATTERY_STATUS_CLASSIFIER[0] if len(unsafe_params) else BATTERY_STATUS_CLASSIFIER[1]][0]