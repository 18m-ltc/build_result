# (c) 2016 Haoran Hu <huhaoran@cn.ibm.com>
#
# This file is part of BVT pipeline for RDO
#

import sys

import pexpect


def download_rebuild_report(host, user, password, file_location):
    """ we try to use this function to execute:
    scp root@9.114.112.227:/var/log/mockchain .
    """
    try:
        scp_cmd_local = ''.join(['scp', ' ', user, '@', host, ':', file_location, ' ', '.'])
        print(scp_cmd_local)
        child_local = pexpect.spawn(scp_cmd_local)
        child_local.logfile_send = sys.stdout
        while True:
            index = child_local.expect(['\s*Are you sure you want to continue connecting\s*',
                                        '\s*password: '])
            if index == 0:
                child_local.sendline('yes')
            elif index == 1:
                child_local.sendline(password)
            else:
                break
        return 0
    except Exception as e:
        print('have exception: %s', e)
        return 1


def main():
    download_rebuild_report(host='9.114.112.227',
                            user='root',
                            password='passw0rd',
                            file_location='/var/log/mockchain')


if __name__ == '__main__':
    sys.exit(main())
