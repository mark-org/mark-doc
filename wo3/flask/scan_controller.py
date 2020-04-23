#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/20


def _list():
    return 'scan...xxxx.......001xx----7xx77'


def add_url_rule(app, module_name):
    app.add_url_rule("/%s/abc" % module_name, view_func=_list)

    # @app.route('/my_list')
    # def my_list():
    #     return 'Hello Worldx1234!xxxx'



