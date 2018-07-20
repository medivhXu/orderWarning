# !/uer/bin/env python3
# coding=utf-8

import pymysql
import logging
import configparser

LOGGER = logging.getLogger(__name__)


class GetData:
    def __init__(self):
        self._conf = configparser.ConfigParser()
        self._conf.read('conf.ini')
        self._db = None
        self._cursor = None

    def _connect_db(self):
        _server_conf = {'host': self._conf.get("SERVER", "host"),
                        'user': self._conf.get("SERVER", "username"),
                        'passwd': self._conf.get("SERVER", "password"),
                        'port': int(self._conf.get("SERVER", "port")),
                        'charset': self._conf.get("SERVER", "charset")}
        try:
            self._db = pymysql.connect(**_server_conf)
            self._cursor = self._db.cursor()
            LOGGER.info("数据库连接成功！")
        except ConnectionError as ex:
            LOGGER.error(str(ex))

    def get_result(self, sql):
        LOGGER.info("sql is :{}".format(sql))
        self._connect_db()
        try:
            self._cursor.execute(sql)
            self._db.commit()
            result = self._cursor.fetchall()
            return result
        except Exception as e:
            LOGGER.error("执行语句出错了。错误信息：{}".format(e))
            return e
        finally:
            self._close_db()

    def _close_db(self):
        self._db.close()
        LOGGER.info("数据库连接关闭！")


if __name__ == '__main__':
    run = GetData()
    c = run.get_result(
        sql="SELECT * FROM hahah "
            "WHERE task_status=4 AND execute_count=6")
    print(c)
