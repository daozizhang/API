from testdata.get_path import get_path
from logs.log import get_cwd


class Config:

    sheet_name = 'roms'
    file_path = get_path()

    @classmethod
    def test_path(cls):
        return get_path()

    @classmethod
    def log_path(cls):
        return get_cwd()
