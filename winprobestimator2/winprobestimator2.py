import os
import requests
import json

class WinProbEstimator2:
    def __init__(self):
        self.__server_url = os.environ['WIN_PROB_ESTIMATOR2_URL']

    # @param id [ 'year', 'monthday', 'jyocd', 'kaiji', 'nichiji', 'racenum']
    def estimate(self, dataset):

        query = json.dumps(dataset)
        r = requests.post(self.__server_url, query)

        if r.status_code != 200 or r.status_code != 400:
            body = json.loads(r.text)
            raise RuntimeError("TimeForecaster server says: %s" % (body["error"],))

        body = json.loads(r.text)
        return body
