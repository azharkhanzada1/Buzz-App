import pybreaker
import requests
from urllib3 import request

# Create a circuit breaker instance
circuit_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=30)

@circuit_breaker
def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Api call failed", e)
        raise