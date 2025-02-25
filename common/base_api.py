#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from common import mysql_util


def send_requests(testdata):
    method = testdata['method']  # POST or GET or DELETE
    url = testdata['url']  # 接口
    params = eval(testdata['params'])  # 参数
    test_func = testdata['function']  # 功能
    print("*******正在执行用例：-----  %s  ----**********" % test_func)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    try:
        if method == "post":
            r = requests.post(url, data=params)
        else:
            r = requests.get(url, params)
        result = r.json()
    except Exception as e:
        print(e)

    return result


if __name__ == "__main__":
    op = mysql_util.OperationDbInterface()
    testdata = op.select_one_sql('select * from api where function = \'login\'')['data']
    print(testdata)
    req = send_requests(testdata)
    print(req['data'])
