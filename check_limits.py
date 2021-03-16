import Constant
import localization
from battery_safety_tester import identify_battery_param_operating_range, is_battery_ok
from reporter import report_overall_battery_status

if __name__ == '__main__':
    # Battery Parameter Safety Testing (incl. Warning Tests)
    assert (identify_battery_param_operating_range("cell_temperature_in_celsius", float("nan")) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[0])
    assert (identify_battery_param_operating_range("soh_in_percent", 50) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[1])
    assert (identify_battery_param_operating_range("soc_in_percent", -50) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[2])
    assert (identify_battery_param_operating_range("charge_rate_in_c_rate", 1.5) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[3])
    assert (identify_battery_param_operating_range("soc_in_percent", 15) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[4])
    assert (identify_battery_param_operating_range("cell_temperature_in_celsius", 55) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[5])
    assert (identify_battery_param_operating_range("charge_rate_in_c_rate", 0.52) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[6])
    assert (identify_battery_param_operating_range("cell_temperature_in_celsius", 44) ==
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[7])

    # Overall Battery Safety Testing (Warnings are considered OK)
    assert (is_battery_ok(cell_temperature_in_celsius=25,
                          soc_in_percent=73,
                          charge_rate_in_c_rate=0.65) is Constant.BATTERY_STATUS_CLASSIFIER[1])
    assert (is_battery_ok(cell_temperature_in_celsius=95,
                          soc_in_percent=60,
                          charge_rate_in_c_rate=0) is Constant.BATTERY_STATUS_CLASSIFIER[0])
