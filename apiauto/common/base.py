import requests
import xlrd
import openpyxl

from logs.log import log
from config.cfg import Config


class Method(object):
    """请求方法"""

    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'https://127.0.0.1:8888'
    }

    @classmethod
    def get_method(cls, **kwargs):
        """get请求"""
        url = kwargs.get('url')
        params = kwargs.get('payload')
        log.info(
            f'case_id:{kwargs.get("case_id")}- {kwargs.get("case_description")}')

        res = None
        try:
            res = requests.get(url=url, params=params, proxies=cls.proxies)
            log.info(f'请求的url：{kwargs.get("url")}')
            log.info(f'响应体：{res.json()}')
        except BaseException as e:
            log.error(f'响应失败--{e}')
        finally:
            Assert.equal(kwargs, res)

    @classmethod
    def post_method(cls, **kwargs):
        """post请求"""
        res = None
        log.info(
            f'case_id:{int(kwargs.get("case_id"))} - {kwargs.get("case_description")}')
        try:
            res = requests.post(
                url=kwargs.get('url'),
                data=kwargs.get('data'),
                json=eval(kwargs.get('payload')),
            )
            log.info(f'请求体-->{res.request.body.decode(encoding="utf-8")}')
            log.info(f'响应体-->{res.json()}')
        except Exception as e:
            log.error(f'响应失败--{e}')
        finally:
            Assert.equal(kwargs, res)

    @classmethod
    def main_method(cls, kwargs):
        if kwargs.get('method') == 'post':
            return cls.post_method(**kwargs)
        elif kwargs.get('method') == 'get':
            return cls.get_method(**kwargs)
        else:
            log.error(f'请求接口类型错误--{kwargs.get("method")}')


class OperateExl(object):

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.sheet = xlrd.open_workbook(self.path).sheet_by_name(self.name)
        self.row_list = self.sheet.row_values(rowx=0)
        print(self.row_list)
        for key, value in dict(enumerate(self.row_list)).items():
            self.__setattr__(str(value), key)

    def readexcel(self, testname):
        cols = self.sheet.col_values(colx=self.casename)
        list0 = []
        if cols:
            for i, value in enumerate(cols):
                if value == testname:
                    list1 = self.sheet.row_values(rowx=i)
                    list0.append(dict(zip(self.row_list, list1)))
            return list0

    def writexcel(self, row, result):
        workbook = openpyxl.load_workbook(self.path)
        try:
            sheet_w = workbook[self.name]
            # sheet_w[f'K{int(row + 1)}']=result
            sheet_w.cell(row=row + 1, column=self.result + 1, value=result)
        except Exception as e:
            log.error(f'{e}')
        finally:
            workbook.save(self.path)


class Assert:

    @classmethod
    def equal(cls, kwargs, res):
        try:
            # assert kwargs['assert'] == res.json().get('info')
            assert kwargs['assert'] == res.json()['message']
            OperateExl(
                Config.file_path,
                Config.sheet_name).writexcel(
                row=kwargs['case_id'],
                result='PASS')
            log.info(f'row:{int(kwargs["case_id"])}--pass')
        except Exception as e:
            log.error(f'失败原因：{str(e)}')
            OperateExl(
                Config.file_path,
                Config.sheet_name).writexcel(
                row=kwargs['case_id'],
                result='FAIL')
        finally:
            assert kwargs['assert'] == res.json().get('message'), log.error(
                f'{kwargs["assert"]} != {res.json().get("info")} ->断言失败--FAIL')
            log.info(
                f'{kwargs["assert"]} == {res.json().get("info")}  ->响应成功-PASS\n\n')
