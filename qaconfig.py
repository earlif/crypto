
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


class InterfaceConstant:

    base_url = "https://uat-api.3ona.co/v2"


class DataConstant:
    FILE_TYPE_EXCEL = "excel"
    case_id = "case_id"


class LogConstant:
    all_when = "midnight"
    all_backupCount = 7

    error_when = "midnight"
    error_backupCount = 7

class RabbitmqConstant:
    mq_host = "172.16.35.164"
    mq_port = "5672"
    mq_vhost = "/vms"
    mq_username = "vmsmquser"
    mq_password = "vmsmqpassword"
    ssl_required = False
    # if ssl_required = True, then these two fields must have values
    mq_ssl_certfile = os.path.join(PROJECT_DIR, "ssl-conf", "client_certificate.pem")
    mq_ssl_keyfile = os.path.join(PROJECT_DIR, "ssl-conf", "client_key.pem")


class TestCases:

    TESTDATA_COLS_EXCLUDE = [
        'executed',
        "test_result"
    ]

    PRECON_COLS_EXCLUDE = [
        'executed',
        'tdrequest_method',
        'tdconnection_info',
        'tdrequest_param',
        'tdrequest_data',
        'tdresponse_param',
        'tdinteraction_type',
        'tdexecuted'
    ]

    TRARDOWN_COLS_EXCLUDE = [
        'request_method',
        'connection_info',
        'request_param',
        'request_data',
        'response_param',
        'interaction_type',
        'field_value',
        'tdfield_value',
        'executed',
        'tdexecuted'
    ]

    data_type = "excel"
    test_data_file_path = os.path.join(PROJECT_DIR, "data", "get-candlestick_testdata.xls") + "&test_data"
    # setup_teardown_data_path = os.path.join(PROJECT_DIR, "data", "test_data.xls") + "&setup_teardown_method"
    # precondition_clearup_path = os.path.join(PROJECT_DIR, "data", "test_data.xls") + "&precondition_clearup"

    # Specific the cases' type need to be executed, if no cases type provided, default to execute all the test cases
    case_type_to_execute = []
