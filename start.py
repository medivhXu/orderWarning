# !/uer/bin/env python3
# coding=utf-8
import os
import logging
from run_sql import GetData
from send_email import send_email

LOGGER = logging.getLogger(__name__)

for filename in os.listdir('./'):
    if filename == "logs":
        break
else:
    os.mkdir('./' + '/logs')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename="log.log",
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def start():
    global file
    get_data = GetData()
    result = get_data.get_result("SELECT * FROM hahaha "
                                 "WHERE task_status=4 AND execute_count=6 AND yn=1")
    module_html = """
            <table border="1">
            <tr>
                <th>订单ID</th>
                <th>订单号</th>
                <th>报文</th>
                <th>任务类型</th>
            </tr>
                {}
            </table>
            """
    file = ''
    table = """
            <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>
            """
    for unit_order in result:
        order_list = list(unit_order)
        keyword1 = order_list[0]
        keyword2 = order_list[1]
        body = order_list[2]
        task_type = order_list[3]
        if task_type == 10:
            task_type = "acl支付订单"
        elif task_type == 20:
            task_type = "acl退款订单"
        elif task_type == 30:
            task_type = "**汽车支付订单"
        elif task_type == 40:
            task_type = "**汽车退款订单"
        elif task_type == 50:
            task_type = "hc支付订单"
        elif task_type == 60:
            task_type = "hc退款订单"
        file += ''.__add__(table).format(keyword1, keyword2, body, task_type)
    full_html = module_html.format(file)
    send_email(full_html.__str__())


start()
