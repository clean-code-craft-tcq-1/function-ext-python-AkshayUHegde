from sys import maxsize
from Constant import BATTERY_PARAM_CHARACTERISTICS, PARAM_OPERATING_RANGE_CLASSIFIER
from math import ceil, floor


def snap_range_limits_to_sensor_accuracy(battery_param_name, battery_param_operating_ranges):
    battery_param_sensor_accuracy = BATTERY_PARAM_CHARACTERISTICS[battery_param_name]['sensor_accuracy']
    for operating_range in battery_param_operating_ranges.values():
        operating_range[0] = battery_param_sensor_accuracy * ceil(operating_range[0] /
                                                                  battery_param_sensor_accuracy)
        operating_range[1] = battery_param_sensor_accuracy * floor(operating_range[1] /
                                                                   battery_param_sensor_accuracy)
    return battery_param_operating_ranges


def classify_operating_ranges(battery_param_name):
    param_operating_range = {}
    param_characteristics = BATTERY_PARAM_CHARACTERISTICS[battery_param_name]
    tolerance_correction = param_characteristics["tolerance"] * param_characteristics["sensor_limits"]["max"]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[2]] = [-maxsize, param_characteristics["sensor_limits"]["min"]]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[3]] = [param_characteristics["sensor_limits"]["max"], maxsize]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[4]] = [param_characteristics["sensor_limits"]["min"],
                                                                  param_characteristics["lower_safety_limit"]]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[5]] = [param_characteristics["upper_safety_limit"],
                                                                  param_characteristics["sensor_limits"]["max"]]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[6]] = [param_characteristics["lower_safety_limit"],
                                                                  param_characteristics[
                                                        "lower_safety_limit"] + tolerance_correction]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[7]] = [param_characteristics[
                                                        "upper_safety_limit"] - tolerance_correction,
                                                                  param_characteristics["upper_safety_limit"]]
    param_operating_range[PARAM_OPERATING_RANGE_CLASSIFIER[8]] = [param_characteristics[
                                                        "lower_safety_limit"] + tolerance_correction,
                                                                  param_characteristics[
                                                        "upper_safety_limit"] - tolerance_correction]
    return param_operating_range
