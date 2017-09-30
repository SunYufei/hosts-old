# Author: Sun Yufei

import urllib.request
import os
import shutil
import time

HOSTS_URL = 'https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts'

LOCAL_PATH = os.environ['windir'] + '\\System32\\drivers\\etc\\hosts'


def main():
    '''Main Function'''

    print('欢迎使用Google Hosts更新工具')
    print('Gitee: https://gitee.com/sunovo/hosts')
    print('GitHub: https://github.com/sunyufei/hosts')

    # Download hosts file
    if(os.path.exists('hosts')):
        os.remove('hosts')
    try:
        urllib.request.urlretrieve(HOSTS_URL, 'hosts')
    except Exception:
        print('网络连接失败')
    # Backup old hosts file
    try:
        if(os.path.exists(LOCAL_PATH + '.bak')):
            os.remove(LOCAL_PATH)
        else:
            shutil.copyfile(LOCAL_PATH, LOCAL_PATH + '.bak')
        # Move new file to system
        shutil.move('hosts', LOCAL_PATH)
        # Update dns cache
        os.system('ipconfig /flushdns')
    except Exception:
        print('请使用管理员权限运行')

    time.sleep(2)


if __name__ == '__main__':
    main()