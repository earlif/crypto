
def common_validation(response, expectedstatuscd):

    if response.httpstatuscd != int(expectedstatuscd):

        raise AssertionError(f"Common validation is fail, the expected result is {expectedstatuscd}, but the actual result is {response.httpstatuscd }")
