from Constant import PARAM_NOK


def accumulate_unsafe_params(battery_params_operating_ranges):
    unsafe_params = {}
    for battery_param in battery_params_operating_ranges:
        battery_param_reporting_level = battery_params_operating_ranges[battery_param].split('_')[0]
        if battery_param_reporting_level in PARAM_NOK:
            unsafe_params[battery_param] = battery_params_operating_ranges[battery_param]
    return unsafe_params