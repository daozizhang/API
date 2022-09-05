import os
from logs.log import log


def get_path(name):
    try:
        path_dir = os.path.dirname(os.path.abspath(__file__))
        # name = 'pagele.yaml'
        if name.split('.')[1]=='yaml':
            path = os.path.join(path_dir, name)
            return path
        elif name.split('.')[1]=='json':
            path=os.path.join(path_dir,name)
            return path
    except BaseException as e:
        print('获取 pagele.yaml 路径失败', e)


if __name__ == '__main__':
    print(get_path('login.json'))
