import gunicorn
import datetime
import json


def application(env, start_response):
    data = json.dumps(
        {
            "time": str(datetime.datetime.now()),
            "url": env['HTTP_HOST'] + '/api' + env['RAW_URI'],
        }
    )

    headers = [
        ('Content-Type', 'text/json'),
    ]

    start_response('200 OK', headers)
    # print('Raw URI: ' + env['RAW_URI'])
    # print('Path: ' + env['PATH_INFO'])
    # print('Host: ' + env['HTTP_HOST'])
    # print('server port: ' + env['SERVER_PORT'])
    data = data.encode('utf-8')
    return iter([data])

