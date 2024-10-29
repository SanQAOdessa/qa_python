import requests
import logging

class BaseClient:

    def make_request(self, method, endpoint, **kwargs):
        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        logging.info(
            "Making %s a request to %s%s%s",
            method.upper(),
            endpoint,
            f" with params {params}" if params else "",
            f" with params {data}" if data else "",
        )
        response = requests.request(method, endpoint, **kwargs)
        response.raise_for_status()
        return response