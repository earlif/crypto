import requests
from qaconfig import InterfaceConstant as ic


class InterFace:

    def __init__(self, method, path, headers=None, param=None, data=None, json=None, files=None):
        self._method = method
        self._path = ic.base_url + path
        self._headers = headers
        self._param = param
        self._data = data
        self._json = json
        self._files = files

        if self._method == "get":
            self._response = requests.get(self._path, params=self._param, json=self._json, headers=self._headers)
            print(self._response.text)
        elif self._method == "post":
            self._response = requests.post(self._path, data=self._data, params=self._param, json=self._json, headers=self._headers, files=self._files)
        elif self._method == "put":
            self._response = requests.put(self._path, data=self._data, params=self._param, json=self._json, headers=self._headers)
        elif self._method == "delete":
            self._response = requests.delete(self._path, params=self._param, headers=self._headers)

    status_ok = [200, 201, 204]

    @property
    def responseurl(self):

        return self._response.url

    @property
    def httpstatuscd(self):

        return self._response.status_code

    @property
    def responsejson(self):

        return self._response.json()

    @property
    def responsetext(self):

        return self._response.text

    @property
    def responseheaders(self):

        return self._response.headers


