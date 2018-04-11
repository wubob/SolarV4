#!/usr/bin/env python
# -*- coding: utf-8 -*-

#封装所有的API接口

import requests
import json
import logging

class UserAPI():

    def Userlist():
        headers = {'content-type': 'application/json'}
        url = "http://120.24.239.**:9080/user/app/get_sys_time.do"
        r = requests.get(url=url, headers=headers)
        return r.json()
    
    def UserGet():
      headers = {'content-type': 'application/json'}
      urlget = 'http://192.168.1.241/api/users/admin'
      rget = requests.get(urlget, cookies=rlogin.cookies, headers=headers)
      print("用户查看"+str(rget.status_code))


if __name__ == "__main__":
    test()