1. test case and test data is at data/
2. html format will be generated at reports/
3. run testRunner.py to start testing.

description:
The script will read the test data from get-candlestick_testdata.xls, and pass it to pytest_generate_tests to generate the tests. And then send the requests based on the test data to do the tests. After getting the response, it will validate the http status code and the json data. Finally, it will gnerate the html format report on reports.

The meaning of the test data collum:
case_id: The id of the test case
request_method: the reuest method	
method: the method need to be tested	
request_data: The parameters, json data, etc of the request.
expected_statuscd: expected status code
expected_response: expected response json data	
case_type:	determine how to validate the json data.
executed: The flag to determine run this case or not	
test_result: The test case is passed or not
