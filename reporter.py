import localization


def report_parameters(battery_param_name, battery_param_status):
    return localization.TRANSLATION_TABLE[localization.CURR_LOCALIZATION]["battery_param_report"][
               battery_param_status] % battery_param_name


def report_overall_battery_status(overall_battery_status):
    return localization.TRANSLATION_TABLE[localization.CURR_LOCALIZATION]["overall_battery_report"][
        overall_battery_status]
