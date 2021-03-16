import localization
from controller import deploy_corrective_measures


def report_params(param_operating_ranges, console=True, controller_alert=True):
    if console:
        print(report_to_console(param_operating_ranges))
    if controller_alert:
        print(deploy_corrective_measures(param_operating_ranges))


def report_to_console(param_operating_ranges):
    consolidated_report = []
    for param in param_operating_ranges:
        consolidated_report.append(localization.TRANSLATION_TABLE[localization.CURR_LOCALIZATION][
                                       "battery_param_report"][param_operating_ranges[param]] % param)
    return consolidated_report


def report_overall_battery_status(overall_battery_status):
    return localization.TRANSLATION_TABLE[localization.CURR_LOCALIZATION]["overall_battery_report"][
        overall_battery_status]
