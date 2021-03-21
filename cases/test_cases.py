import pytest, json
import time
from qalogger import log
from qaconfig import TestCases as tc, DataConstant as dc
from qa import qadatacentral as dtc
from qa import qainterface
from validation import comvalidation, specialvalidation


# ========fixture=============
def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0]) if len(funcarglist) > 0 else funcarglist
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist],
                         ids=[item[dc.case_id] for item in funcarglist])


class TestCases:
    # Step1: Get test data
    _datac = dtc.get_data_central(tc.data_type, tc.test_data_file_path)
    _dataset = _datac.read_data()
    _testdata = _datac.convert_to_parameter(_dataset)

    logging = log()

    params = {
        "test_cases": _testdata,
    }

    def test_cases(self, case_id,  request_method, method, request_data,
                   expected_statuscd, expected_response, case_type):
        if "null" in expected_response:
            expected_response = expected_response.replace("null", "None")
        expected_response = eval(expected_response)
        # noinspection PyBroadException
        try:

            # Step2:  Send request and get response

            response = qainterface.InterFace(request_method, method,
                                             headers=eval(request_data).get("headers") if request_data else None,
                                             param=eval(request_data).get("param") if request_data else None,
                                             data=eval(request_data).get("form-data") if request_data else None,
                                             json=eval(request_data).get("json-data") if request_data else None,
                                             files=eval(request_data).get("files") if request_data else None)

            self.logging.debug("the response for case %s is %s" % (case_id, response.responsetext))

            # Step3: Get response to do common validation

            comvalidation.common_validation(response, expected_statuscd)

            # Step4: Special validation base on caseType
            if case_type:
                specialvalidation.special_validation(case_type, response.responsejson, expected_response)

            self.logging.info("Cases Pass ! %s passed" % case_id)

        except AssertionError as error:

            self.logging.info("Cases Fail ! %s failed, the actual result is different with expected result" % case_id)

            self.logging.error(error)

            pytest.fail()

        except Exception as e:

            self.logging.info(
                "Cases Fail ! %s failed,  some error hit in test scripts, please contact QA team for more help!" %
                case_id)

            self.logging.error(e, exc_info=True)

            pytest.fail()

