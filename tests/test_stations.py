from asserter import assert_true, assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes
from test_utils import decorate_test, Constants, DataModel, RequestParams

ENDPOINT = Endpoints.STATIONS

params = {RequestParams.lat_min_key: RequestParams.lat_min_value,
          RequestParams.lat_max_key: RequestParams.lat_max_value,
          RequestParams.long_min_key: RequestParams.long_min_value,
          RequestParams.long_max_key: RequestParams.long_max_value}

class TestStations:

    @staticmethod
    @decorate_test
    def test_station_api_status_code():
        status_code, _ = HTTPSession.send_request(RequestTypes.GET, ENDPOINT, params)
        assert_equal(status_code, StatusCodes.STATUS_200, f'Status code of {ENDPOINT} enpoint')

    @staticmethod
    @decorate_test
    def test_station_api_returned_list_length():
        _, station_data = HTTPSession.send_request(RequestTypes.GET, ENDPOINT, params)
        assert_equal(len(station_data), DataModel.station_data_length,
                     'Number of stations returned by data response:')

    @staticmethod
    @decorate_test
    def test_data_model():
        _, station_data = HTTPSession.send_request(RequestTypes.GET, ENDPOINT, params)
        assert_equal(type(station_data), list, 'The initial level of data type where')
        assert_true(any([isinstance(a, dict) for a in station_data]),
                    'Station data contains dictionary data type')

        assert_true(all(isinstance(a.get(Constants.id, None), int) for a in station_data),
                    'All Station data entities have "id" attribute of int type')
        station_id = station_data[0][Constants.id]
        assert_equal(station_id, DataModel.id_value, 'Station data have "id" entity where')

        station_latitude = station_data[0][Constants.latitude]
        assert_true((isinstance(station_latitude, float)),
                    'Station data have "Latitude" entity attribute of float type')
        assert_equal(station_latitude, DataModel.latitude_value, 'Station data have "Latitude" entity where')

        station_longitude = station_data[0][Constants.longitude]
        assert_true((isinstance(station_longitude, float)),
                    'Station data have "Longitude" entity attribute of float type')
        assert_equal(station_longitude, DataModel.longitude_value, 'Station data have "Longitude" entity where')

        station_name = station_data[0][Constants.name]
        assert_equal(station_name, DataModel.name_value, 'Station data have "name" entity where')

        station_city = station_data[0][Constants.city]
        assert_true(isinstance(station_city, str), 'Station data have "city" entity attribute of String type')
        assert_equal(station_city, DataModel.city_value, 'Station data have "city" entity where')

        station_country = station_data[0][Constants.country]
        assert_true(isinstance(station_country, str), 'Station data have "country" entity attribute of String type')
        assert_equal(station_country, DataModel.country_value, 'Station data have "country" entity where')

        station_provider = station_data[0][Constants.provider]
        assert_true(isinstance(station_provider, str), 'Station data have "provider" entity attribute of String type')
        assert_equal(station_provider, DataModel.provider_value, 'Station data have "provider" entity where')

        assert_equal(len(station_data[0][Constants.evses]), DataModel.evses_length,
                     'Number of eves returned by station data response:')

        evses_id = station_data[0][Constants.evses][0][Constants.id]
        assert_true(isinstance(evses_id, int), 'Eves Id have "provider" entity attribute of int type')
        assert_equal(evses_id, DataModel.evses_id, 'Eves Id have "provider" entity where')

        evses_group_name = station_data[0][Constants.evses][0][Constants.eves_group_name]
        assert_true(isinstance(evses_group_name, str),
                    'Eves Group Name have "provider" entity attribute of String type')
        assert_equal(evses_group_name, DataModel.eves_group_name,
                     'Eves Group Name have "provider" entity where')

        evses_connector_type = station_data[0][Constants.evses][0][Constants.eves_connectors][0][Constants.type]
        assert_true(isinstance(evses_connector_type, str),
                    'Eves connector type have "provider" entity attribute of String type')
        assert_equal(evses_connector_type, DataModel.evses_connector_type,
                     'Eves connector type have "provider" entity where')

        evses_connector_max_kw = station_data[0][Constants.evses][0][Constants.eves_connectors][0][Constants.max_kw]
        assert_true(isinstance(evses_connector_max_kw, int),
                    'Eves connector maxKw have "provider" entity attribute of int type')
        assert_equal(evses_connector_max_kw, DataModel.evses_connector_max_kw,
                     'Eves connector maxKw have "provider" entity where')
