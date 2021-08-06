#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


def lineNotifyMessage(token, msg, filename):
    headers = {'Authorization': 'Bearer ' + token}

    files = {'imageFile': (filename, open(filename, 'rb'),
             'multipart/form-data')}
    data = {'message': msg}
    r = requests.post('https://notify-api.line.me/api/notify',
                      headers=headers, files=files, data=data)
    return r.status_code


if __name__ == '__main__':
    token = '存取權杖'
    message = 'Line Notify 訊息'
    filename = 'sample.jpeg'

    lineNotifyMessage(token, message, filename)
