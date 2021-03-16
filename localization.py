import Constant

CURR_LOCALIZATION = "en-US"

TRANSLATION_TABLE = {
    Constant.LOCALIZATION_SUPPORT[0]: {
        "battery_param_report": {
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[0]: "ALERT: Battery parameter %s is NaN.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[1]: "ALERT: Battery parameter %s is not supported for safety checks.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[2]: "ALERT: Battery parameter %s is out of range!",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[3]: "ALERT: Battery parameter %s is out of range!",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[4]: "ALERT: Battery parameter %s is under the prescribed limit",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[5]: "ALERT: Battery parameter %s is over the prescribed limit",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[6]: "WARNING: Battery parameter %s is approaching the prescribed "
                                                "underlimit.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[7]: "WARNING: Battery parameter %s is approaching the prescribed "
                                                "overlimit.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[8]: "INFO: Battery parameter %s is normal. Running within prescribed "
                                                "limits. "
        },
        "overall_battery_report": {
            Constant.BATTERY_STATUS_CLASSIFIER[0]: "ALERT: Battery operating outside safe parameters. Please stop usage"
                                                   " immediately.",
            Constant.BATTERY_STATUS_CLASSIFIER[1]: "INFO: Battery running normally."
        },
        "controller_log": {
            "dummy": "Deploying appropriate corrective measure for %s condition for %s."
        }
    },
    Constant.LOCALIZATION_SUPPORT[1]: {
        "battery_param_report": {
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[0]: "ALARM: Batterieparameter %s ist NaN.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[1]: "ALARM: Batterieparameter %s ist wird für Sicherheitsüberprüfungen "
                                                "nicht unterstützt.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[2]: "ALARM: Batterieparameter %s ist außer Reichweite.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[3]: "ALARM: Batterieparameter %s ist außer Reichweite.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[4]: "ALARM: Batterieparameter %s ist unter der vorgeschriebenen Grenze.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[5]: "ALARM: Batterieparameter %s ist über der vorgeschriebenen Grenze.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[6]: "WARNUNG: Batterieparameter %s ist annäherung vorgeschrieben unter "
                                                "Grenze.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[7]: "WARNUNG: Batterieparameter %s ist annäherung vorgeschrieben über "
                                                "Grenze.",
            Constant.PARAM_OPERATING_RANGE_CLASSIFIER[
                8]: "INFO: Batterieparameter %s ist normal. Laufen innerhalb vorgeschriebener Grenzen.",
        },
        "overall_battery_report": {
            Constant.BATTERY_STATUS_CLASSIFIER[0]: "ALARM: Batterie arbeitet außerhalb sicherer Parameter. "
                                                   "Bitte beenden Sie die Nutzung sofort.",
            Constant.BATTERY_STATUS_CLASSIFIER[1]: "INFO: Batterie läuft normal."
        },
        "controller_log": {
            "dummy": "Bereitstellen einer geeigneten Korrekturmaßnahme für die %s-Bedingung des %s-Parameters."
        }

    }
}


def set_localization(language):
    if language in Constant.LOCALIZATION_SUPPORT:
        global CURR_LOCALIZATION
        CURR_LOCALIZATION = language
        return True
    else:
        print(f"ALERT: Localization not set. {language} not supported.")
        return False
