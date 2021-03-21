import operator
from qaconfig import InterfaceConstant as ic
import requests
from operator import itemgetter
from functools import reduce
import time


def special_validation(case_type, response, expected_response):
    if "get-candlestick-normal" == case_type:
        validate_get_candlestick_resp(response, expected_response)
    if "get-candlestick-bad" == case_type:
        validate_get_candlestick_bad(response,expected_response)


def validate_get_candlestick_resp(response, expected_response):
    # validate the response,except data in result.
    resp_data = response["result"].pop("data")
    expected_data = list()
    if "data" in expected_response["result"]:
        expected_data = expected_response["result"].pop("data")
    if response != expected_response:
        raise AssertionError(f"expected response is {expected_response}, but actual response is {response}")

    # validate the data contains all attributes
    if expected_data is None and resp_data is None:
        return
    for candlestick in resp_data:
        if "t" not in candlestick or candlestick["t"] is None:
            raise AssertionError(f"some data does not contain t attribute or t is None")
        if "o" not in candlestick or candlestick["o"] is None:
            raise AssertionError(f"some data does not contain o attribute or o is None")
        if "h" not in candlestick or candlestick["h"] is None:
            raise AssertionError(f"some data does not contain h attribute or h is None")
        if "l" not in candlestick or candlestick["l"] is None:
            raise AssertionError(f"some data does not contain l attribute or l is None")
        if "c" not in candlestick or candlestick["c"] is None:
            raise AssertionError(f"some data does not contain c attribute or c is None")
        if "v" not in candlestick or candlestick["v"] is None:
            raise AssertionError(f"some data does not contain v attribute or v is None")
    print(response)


def validate_get_candlestick_bad(response, expected_response):
    # ignore timestamp and requestId
    if "timestamp" in expected_response:
        expected_response.pop("timestamp")
    if "timestamp" in response:
        response.pop("timestamp")
    if "requestId" in expected_response:
        expected_response.pop("requestId")
    if "requestId" in response:
        response.pop("requestId")
    if response != expected_response:
        raise AssertionError(f"expected response is {expected_response}, but actual response is {response}")
