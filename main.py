from binance_api import binanceus_request
import time
import dotenv
import os

dotenv.load_dotenv()
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]

recvWindow = 10000
# route to data resources
uri_path = "/api/v3/account"
data = {
    "timestamp": int(round(time.time() * 1000)),
}

result = binanceus_request(uri_path, data, api_key, api_secret)
print("GET {}: {}".format(uri_path, result))
