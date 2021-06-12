from datetime import timedelta
from time import time
from logger import Logger


def decorate_test(test_function):
    def wrapper():
        Logger.log_test_start(test_function)
        time_delta, _ = measure_time(test_function)
        Logger.log_test_finish(test_function, timedelta(seconds=time_delta))

    return wrapper


def measure_time(function):
    start = time()
    result = function()
    end = time()
    return end - start, result


class Constants:
    id = 'id'
    latitude = 'latitude'
    longitude = 'longitude'
    name = 'name'
    city = 'city'
    country = 'country'
    provider = 'provider'
    evses = 'evses'
    eves_group_name = 'groupName'
    eves_connectors = 'connectors'
    type = 'type'
    max_kw = 'maxKw'


class DataModel:
    station_data_length = 1
    id_value = 8617
    latitude_value = 60.164102
    longitude_value = 24.899113
    name_value = 'Test station advanced pricing'
    city_value = 'Helsinki'
    country_value = 'FI'
    provider_value = 'Virta'
    evses_length = 2
    evses_id = 8616
    eves_group_name = ''
    evses_connector_type = "Mennekes"
    evses_connector_max_kw = 0


class RequestParams:
    lat_min_key = 'latMin'
    lat_max_key = 'latMax'
    long_min_key = 'longMin'
    long_max_key = 'longMax'
    lat_min_value = 60.164101
    lat_max_value = 60.164104
    long_min_value = 24
    long_max_value = 25
