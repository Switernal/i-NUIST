# 南京信息工程大学 i-NUIST 校园网一键登录
# 作者: Switernal


import json
import os
import platform
import sys

import requests
import configparser


def iNUIST_login():

    # 指定当前目录
    filename = os.path.basename(sys.argv[0])
    # 当前路径要去掉文件名和最后一个'/'
    current_path = sys.argv[0][0: -(len(filename) + 1)]
    # print(current_path)
    # print(platform.system())

    # 如果是Mac或Linux, 将当前执行文件权限设为755
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        os.system('chmod 755 %s' % (sys.argv[0]))

    # url
    url = 'http://10.255.255.46/api/v1'
    ipUrl = url + '/ip'
    loginUrl = url + '/login'
    logoutUrl = url + '/logout'

    # 用户信息
    user_name = ''
    password = ''
    channel = ''
    is_auto_login = ''

    # 先检查用户信息是否存在
    if not os.path.isfile(current_path + '/user.ini'):

        print('欢迎使用新版南京信息工程大学 i-NUIST 校园网一键登录程序')
        print('作者: Switernal')
        print('联系方式: switernal@outlook.com')
        print('请在遵守法律和相关规定的前提下使用本程序')

        # 如果是Mac或Linux, 需要授予读写权限
        if platform.system() == 'Darwin' or platform.system() == 'Linux':
            print('\n一键运行脚本不会盗取您的开机密码, 仅用作获取目录读写权限来保存配置文件user.ini, 如果不输入将无法保存配置信息')
            sudoPassword = input("请输入电脑开机密码: ")
            command = 'mount -uw /'
            os.system('echo %s | sudo -S %s' % (sudoPassword, command))

        print('\n以下设置仅首次运行显示, 后续需修改用户信息请直接修改同目录下的user.ini文件')
        print('为了快速登录, 不要删除目录下的user.ini, 否则每次运行需要重新输入配置信息')
        user_name = input("请输入用户名(手机号): ")
        password = input("请输入登录密码: ")
        channel = input("运营商代码: \n  1: 校园网\n  2: 中国移动 \n  3: 中国电信 \n  4: 中国联通 \n请输入运营商代码: ")
        is_auto_login = input("是否允许自动登录(1: 是, 0: 否): ")

        # 写入配置文件
        configure_file = configparser.ConfigParser()
        configure_file.add_section('User-Info')
        configure_file.set('User-Info', 'username', user_name)
        configure_file.set('User-Info', 'password', password)
        configure_file.set('User-Info', 'channel', channel)
        configure_file.set('User-Info', 'isAutoLogin', is_auto_login)

        with open(os.path.join(current_path, 'user.ini'), 'w+') as f:
            configure_file.write(f)

    else:
        # 直接读取配置文件
        config_file = configparser.ConfigParser()
        config_file.read(os.path.join(current_path, 'user.ini'))
        user_name = str(config_file.get('User-Info', 'username'))
        password = str(config_file.get('User-Info', 'password'))
        channel = str(config_file.get('User-Info', 'channel'))
        is_auto_login = str(config_file.get('User-Info', 'isAutoLogin'))

    # 获取ip
    ipRes = requests.get(ipUrl)
    ip = (json.loads(ipRes.text))["data"]

    # 设置login的请求头
    headers = {
        "Host": "10.255.255.46",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://10.255.255.46",
        "Referer": "http://10.255.255.46/authentication/login",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Content-Length": "128",
        "Connection": "keep-alive",
    }

    # login的请求体内容
    if channel is not 1:
        body = {
            "username": user_name,
            "password": password,
            "channel": channel,
            "ifautologin": is_auto_login,
            "pagesign": "secondauth",
            "usripadd": ip,
        }
    else:
        body = {
            "username": user_name,
            "password": password,
            "channel": channel,
            "ifautologin": is_auto_login,
            "pagesign": "firstauth",
            "usripadd": ip,
        }

    # 把 user_info 写成二进制文件 user_binary
    user_json_binary_file = open('user_binary', 'w+')
    user_json_binary_file.write(json.dumps(body).replace(' ', ''))  # 转成json文本后还得把空格全去掉, 他二进制文件数据里不能有空格
    user_json_binary_file.close()

    # 读入二进制文件, 发送登录请求
    user_json_binary_file = open('user_binary', 'rb')
    response = requests.post(url=url, headers=headers, data=user_json_binary_file)
    user_json_binary_file.close()
    os.remove('user_binary')  # 删除登录用的二进制文件

    # 解析请求结果
    responseJson = json.loads(response.text)
    if responseJson["code"] == 200 and responseJson["message"] == 'ok':
        print("\n登录成功!")
        print('用户名: ' + responseJson["data"]["username"])
        print('运营商: ' + responseJson["data"]["outport"])
        print('登录IP: ' + responseJson["data"]["usripadd"])

    else:
        print('\n登录失败!')
        print('返回代码: ' + str(responseJson["code"]))
        error_msg = responseJson['message']

        if error_msg == 'Passwd_Err':
            print('错误信息: 密码错误')
        elif error_msg == 'UserName_Err':
            print('错误信息: 用户名错误')
        else:
            print('错误信息: ' + responseJson["message"])

    # print(response.text)

    # 如果是Windows平台, 执行完会自动退出, 需要pause一下显示结果
    if platform.system() == "Windows":
        print('\n')
        os.system("pause")


if __name__ == '__main__':
    iNUIST_login()
