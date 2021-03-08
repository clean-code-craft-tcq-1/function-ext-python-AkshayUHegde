import Constant
import localization
from reporter import report_parameters, report_overall_battery_status

if __name__ == '__main__':
    assert (
            report_parameters("cell_temperature_in_celsius", Constant.PARAM_OPERATING_RANGE_CLASSIFIER[0]) ==
            localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[0]]
                                      ["battery_param_report"]
                                      [Constant.PARAM_OPERATING_RANGE_CLASSIFIER[0]] % "cell_temperature_in_celsius"
    )
    assert(
              localization.set_localization(Constant.LOCALIZATION_SUPPORT[1]) == True
    )
    assert(
        localization.set_localization("German") == False
    )
    assert (
            report_parameters("soc_in_percent", Constant.PARAM_OPERATING_RANGE_CLASSIFIER[5]) ==
            localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
            ["battery_param_report"]
            [Constant.PARAM_OPERATING_RANGE_CLASSIFIER[5]] % "soc_in_percent"
    )
    assert (
        report_overall_battery_status(Constant.BATTERY_STATUS_CLASSIFIER[0]) ==
        localization.TRANSLATION_TABLE[Constant.LOCALIZATION_SUPPORT[1]]
        ["overall_battery_report"]
        [Constant.BATTERY_STATUS_CLASSIFIER[0]]
    )