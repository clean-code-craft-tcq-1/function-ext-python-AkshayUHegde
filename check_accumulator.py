from accumulator import accumulate_unsafe_params

if __name__ == '__main__':
    assert (
            accumulate_unsafe_params({
                "cell_temperature_in_celsius": "ALERT_UNDERLIMIT",
                "charge_rate_in_c_rate": "WARN_NEARUNDERLIMIT",
                "soc_in_percent": "INFO_NORMAL"
            }) == {
                "cell_temperature_in_celsius": "ALERT_UNDERLIMIT"
            }
    )
    assert (
            accumulate_unsafe_params({
                "cell_temperature_in_celsius": "WARN_NEAROVERLIMIT",
                "charge_rate_in_c_rate": "WARN_NEARUNDERLIMIT",
                "soc_in_percent": "INFO_NORMAL"
            }) == {}
    )
