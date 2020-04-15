#!/usr/bin/env python3

import json
import psycopg2
import os
import sys
import winprobestimator2

with open('sample_input.json') as f:
    req_json = json.load(f)

estimator = winprobestimator2.WinProbEstimator2()
res = estimator.estimate(req_json)

print(json.dumps(res))

