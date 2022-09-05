import os


def get_path():
    try:
        dir_name = os.path.dirname(os.path.abspath(__file__))
        base_name = os.path.basename(os.path.abspath(__file__))
        file_path = os.path.join(dir_name, 'roms.xlsx')
        return file_path
    except BaseException as e:
        print('获取文件夹路径失败', e)


if __name__ == '__main__':
    path = get_path()
    print(path)
