# i-NUIST 一键登录

新·南京信息工程大学 i-NUIST 校园网一键登录脚本

2021年7月份校园网升级后，原登录接口失效，新的一键登录脚本基于新的登录接口编写。

## iOS 15.0+ / iPadOS 15.0+ / macOS 12.0+ 快捷指令

注：由于该快捷指令在 iOS 15 系统创建，iOS 14 或更低系统版本无法安装

使用安装有 iOS 15.0+ 的 iPhone、iPod Touch，iPadOS 15.0+ 的 iPad 或 macOS 12.0+ 的 Mac 点击下方链接即可添加，需先安装”快捷指令“

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

 1. Windows用户需要先安装git，使用`git bash`，在bash环境中运行脚本。
 2. Shell脚本中使用了第三方库jq用于解析返回结果的json，运行前请先安装jq。Mac用户可以使用brew进行安装（需先安装brew）：`brew install jq`。其它安装方式：https://github.com/stedolan/jq
 3. Shell脚本运行方式：`sh iNUIST.sh`
 4. 使用"i-NUIST一键登录_无jq版本.sh"无需安装jq即可直接使用，返回结果是一串原始json
 
## 可执行文件 

 1. Windows和Mac用户使用可执行程序时，第一次运行会在程序所在目录下创建"user.ini"配置文件，请不要删除。如果删除下次运行时仍需要重新输入登录信息。
 2. 使用可执行程序时，后续如需修改登录信息，请直接修改所在目录下的"user.ini"文件
 
## 其它

 1. i-NUIST一键登录脚本中的请求内容均为抓包所得，不存在破解等非法操作。
 2. i-NUIST一键登录脚本不会收取任何费用，如果您已经为此付款，请联系获取渠道要求退款。
 3. i-NUIST一键登录脚本在编写测试时可以正常使用，但不保证在其他设备和环境中正常运行。
 4. 请在遵守中华人民共和国法律和相关规定的前提下使用一键登录脚本，非法或违规使用所造成的后果将全部由使用者承担。
