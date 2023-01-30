# i-NUIST 一键登录

新·南京信息工程大学 i-NUIST 校园网一键登录脚本

2021年7月份校园网升级后，原登录接口失效，新的一键登录脚本基于新的登录接口编写。

Python版本代码已开源，并新增了校园网账号登录，推荐使用。Shell版本目前尚不支持校园网账号登录。

2022.11.21 更新：校园网登录地址突然换到了`10.255.255.46`，导致现有的一键登录脚本全部失效，目前 Mac 版已更新，iOS 和 Windows 版请继续等待，Windows 用户也可使用 Python 脚本自行打包为可执行文件。如果有其他问题欢迎在Issues中评论。

2023.01.30 更新：如果无法使用，将脚本中的IP：`10.255.255.34` 或 `10.255.255.46` 全部替换为 `a.nuist.edu.cn` 即可。校园网登录页可能会变更 IP，但登录 URL 不变


## iOS 16.0+ / iPadOS 16.0+ / macOS 12.0+ 快捷指令

注：由于该快捷指令在 iOS 16 系统创建，iOS 15 或更低系统版本无法安装

使用安装有 iOS 16.0+ 的 iPhone、iPod Touch，iPadOS 16.0+ 的 iPad 或 macOS 12.0+ 的 Mac 点击下方链接即可添加，需先安装”快捷指令“

https://www.icloud.com/shortcuts/883f9575be074e849d0770e5873c5a79

如果您仍在使用 iOS 15，请使用以下链接：

https://www.icloud.com/shortcuts/f6ec2b6d91a34e8a87c556824c278e23

配合自动化或是桌面小组件更为方便。

## Windows

Shell脚本（配合git bash使用）：[Windows/iNUIST-win.sh](https://github.com/Switernal/i-NUIST/blob/main/Windows/iNUIST-win.sh)

Shell脚本（无需jq）：[i-NUIST一键登录_无jq版本.sh](https://github.com/Switernal/i-NUIST/blob/main/i-NUIST一键登录_无jq版本.sh)

可执行文件（双击运行）：[Windows/i-NUIST一键登录_windows.exe](https://github.com/Switernal/i-NUIST/blob/main/Windows/i-NUIST一键登录_windows.exe)

## Mac

Shell脚本（终端运行）：[Mac/iNUIST.sh](https://github.com/Switernal/i-NUIST/blob/main/Mac/iNUIST.sh)

Shell脚本（无需jq）：[i-NUIST一键登录_无jq版本.sh](https://github.com/Switernal/i-NUIST/blob/main/i-NUIST一键登录_无jq版本.sh)

可执行文件（双击运行）：[Mac/i-NUIST一键登录[双击运行]_macos](https://github.com/Switernal/i-NUIST/blob/main/Mac/i-NUIST一键登录%5B双击运行%5D_macos)（第一次运行会要求输入系统开机密码，仅用作获取目录读写权限，否则无法保存配置文件，不会盗取密码）

## Linux

Shell脚本：[Mac/iNUIST.sh](https://github.com/Switernal/i-NUIST/blob/main/Mac/iNUIST.sh)

Shell脚本（无需jq）：[i-NUIST一键登录_无jq版本.sh](https://github.com/Switernal/i-NUIST/blob/main/i-NUIST一键登录_无jq版本.sh)

# 使用说明

## Shell脚本

 1. Windows 用户需要先安装git，使用`git bash`，在 bash 环境中运行脚本。
 2. Shell脚本中使用了第三方库jq用于解析返回结果的json，运行前请先安装jq。Mac用户可以使用brew进行安装（需先安装brew）：`brew install jq`。其它安装方式：https://github.com/stedolan/jq
 3. Shell脚本运行方式：`sh iNUIST.sh`
 4. 使用"i-NUIST一键登录_无jq版本.sh"无需安装jq即可直接使用，返回结果是一串原始json

## Python脚本

 Python 脚本兼容多平台，直接运行`i-NUIST.py`即可。需要先安装 Python3 环境和依赖。
 
## 可执行文件 

 1. Windows和Mac用户使用可执行程序时，第一次运行会在程序所在目录下创建"user.ini"配置文件，请不要删除。如果删除下次运行时仍需要重新输入登录信息。
 2. 使用可执行程序时，后续如需修改登录信息，请直接修改所在目录下的"user.ini"文件
 
## 其它

 1. i-NUIST一键登录脚本中的请求内容均为抓包所得，不存在破解等非法操作。
 2. i-NUIST一键登录脚本不会收取任何费用，如果您已经为此付款，请联系获取渠道要求退款。
 3. i-NUIST一键登录脚本在编写测试时可以正常使用，但不保证在其他设备和环境中正常运行。
 4. 请在遵守中华人民共和国法律和相关规定的前提下使用一键登录脚本，非法或违规使用所造成的后果将全部由使用者承担。
