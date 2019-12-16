#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 0016 10:52
# @Author  : HelloWorld
# @File    : sql_model.py


import pymysql


class SqlModel(object):

    def __init__(self, db_name, user_name, password, ip='localhost'):
        self.db_name = db_name
        self.user_name = user_name
        self.password = password
        self.db = pymysql.connect(ip, self.user_name, self.password, self.db_name)
        self.cursor = self.db.cursor()

    def select_data(self, sql):
        data = ''
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return data

    def ins_or_upd_or_del_data(self, sql):
        msg = ''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            msg = e
        return msg




