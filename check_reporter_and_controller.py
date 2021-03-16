from random import randint, sample

import Constant
import localization
from reporter import report_to_console, report_overall_battery_status
from controller import deploy_corrective_measures

if __name__ == '__main__':
    supported_params = list(Constant.BATTERY_PARAM_CHARACTERISTICS.keys())

    # en-US Single Parameter Console Reporting/Controller Output Testing
    enUS_localization_range_selector = randint(0, len(Constant.PARAM_OPERATING_RANGE_CLASSIFIER) - 1)
    enUS_localization_param_selector = randint(0, len(supported_params) - 1)
    enUS_localization_test_input = {
        supported_params[enUS_localization_param_selector]:
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[enUS_localization_range_selector],
    }
    enUS_localization_console_test_output = [localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[0]][
                                                 "battery_param_report"][
                                                 Constant.PARAM_OPERATING_RANGE_CLASSIFIER[
                                                     enUS_localization_range_selector]] \
                                             % supported_params[enUS_localization_param_selector]]
    enUS_localization_controller_test_output = [localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[0]][
                                                    "controller_log"]["dummy"] \
                                                % (Constant.PARAM_OPERATING_RANGE_CLASSIFIER[
                                                       enUS_localization_range_selector],
                                                   supported_params[enUS_localization_param_selector]
                                                   )]
    assert (
            report_to_console(enUS_localization_test_input) == enUS_localization_console_test_output
    )
    assert (
            deploy_corrective_measures(enUS_localization_test_input) == enUS_localization_controller_test_output
    )
    assert (
            report_overall_battery_status(Constant.BATTERY_STATUS_CLASSIFIER[1]) ==
            localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[0]]
            ["overall_battery_report"]
            [Constant.BATTERY_STATUS_CLASSIFIER[1]]
    )
    assert (
            localization.set_localization("de-DE") == True
    )
    assert (
            localization.set_localization("German") == False
    )

    # de-De Multi Parameter Console Reporting/Controller Output Testing
    deDE_localization_range_selectors = sample(range(0, len(Constant.PARAM_OPERATING_RANGE_CLASSIFIER)), 2)
    deDE_localization_param_selectors = sample(range(0, len(supported_params)), 2)
    deDE_localization_test_input = {
        supported_params[deDE_localization_param_selectors[0]]:
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[0]],
        supported_params[deDE_localization_param_selectors[1]]:
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[1]]
    }
    deDE_localization_console_test_output = [
        localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
        ["battery_param_report"]
        [Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[0]]] %
        supported_params[deDE_localization_param_selectors[0]],
        localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
        ["battery_param_report"]
        [Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[1]]] %
        supported_params[deDE_localization_param_selectors[1]]
    ]
    deDE_localization_controller_test_output = [
        localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
        ["controller_log"]["dummy"] %
        (Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[0]],
         supported_params[deDE_localization_param_selectors[0]]),
        localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
        ["controller_log"]["dummy"] %
        (Constant.PARAM_OPERATING_RANGE_CLASSIFIER[deDE_localization_range_selectors[1]],
         supported_params[deDE_localization_param_selectors[1]])
    ]
    assert (
            report_to_console(deDE_localization_test_input) == deDE_localization_console_test_output
    )
    assert (
            deploy_corrective_measures(deDE_localization_test_input) == deDE_localization_controller_test_output
    )
    assert (
            report_overall_battery_status(Constant.BATTERY_STATUS_CLASSIFIER[0]) ==
            localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
            ["overall_battery_report"]
            [Constant.BATTERY_STATUS_CLASSIFIER[0]]
    )
