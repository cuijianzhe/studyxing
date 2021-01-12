#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : user.py
# @Author: cuijianzhe
# @Date  : 2021/1/12
# @Desc  :

from django.urls import path
from account.apis import user as user_api

urlpatterns = [
    path('user/login/',user_api.LoginApi.as_view()),
]