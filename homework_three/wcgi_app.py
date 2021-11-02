import datetime
import json

def app(environ, start_response):
    dt = datetime.datetime.now()
    data = {"time": dt.time().__str__(),
            "url": ""}
    data_one = json.dumps(data)
    data_two = bytes(data_one, encoding='utf-8')
    headers = [('content-type', 'application/json')]
    start_response('200 OK', headers)
    return [data_two]