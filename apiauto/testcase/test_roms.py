import requests
import unittest
import urllib3
import warnings
from config.cfg import Config
from ddt import ddt, data, file_data, unpack
from logs.log import log
from testdata.get_path import get_path
from common.base import Method, OperateExl


@ddt()
class Roms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        urllib3.disable_warnings()
        warnings.simplefilter('ignore', ResourceWarning)
        cls.proxies = {
            'http': 'http://127.0.0.1:8888',
            'https': 'https://127.0.0.1:8888'}

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*OperateExl(Config.file_path,
                      Config.sheet_name).readexcel('test_login_1_get_verifycode'))
    def test_login_1_get_verifycode(self, kwargs):
        # Method.main_method(kwargs)
        log.info(f'case_id:{kwargs.get("case_id")}')
        log.info(f'case_details:{kwargs["case_details"]}')
        log.info(f'请求的url：{kwargs.get("url")}')
        log.info(f'请求体-->{kwargs.get("payload")}')
        res = requests.post(
            url=kwargs.get('url'),
            json=eval(
                kwargs.get('payload')),
            proxies=self.proxies)
        log.info(f'响应消息体-->{res.json()}')
        self.assertEqual(
            kwargs.get('assert'),
            res.json()['message'],
            msg='响应失败-FAIL\n\n')
        log.info('响应成功-PASS\n\n')


if __name__ == '__main__':
    unittest.main()
