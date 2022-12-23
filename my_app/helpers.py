def localized_datetime(timezone_obj, datetime_obj):
    as_localized = datetime_obj.astimezone(timezone_obj)
    return as_localized
