import localization


def deploy_corrective_measures(param_operating_ranges):
    corrective_measures_completed = []
    for param in param_operating_ranges:
        corrective_measures_completed.append(localization.TRANSLATION_TABLE[localization.CURR_LOCALIZATION][
                                                 "controller_log"]["dummy"] % (param_operating_ranges[param], param))
    return corrective_measures_completed
