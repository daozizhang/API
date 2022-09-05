import os


def get_cwd():
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        name = os.path.basename(os.path.abspath(__file__))

        return path
    except BaseException as e:
        print('获取文件夹路径失败', e)


if __name__ == '__main__':
    get_cwd()
