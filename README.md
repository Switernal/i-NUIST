# i-NUIST 一键登录

南京信息工程大学 i-NUIST 校园网一键登录脚本

## iOS 15.0+ / iPadOS 15.0+ / macOS 12.0+ 快捷指令

注：由于该快捷指令在 iOS 15 系统创建，iOS 14 或更低系统版本无法安装

使用安装有 iOS 15.0+ 的 iPhone/iPod Touch/iPadOS 15.0+ 的 iPad/macOS 12.0+ 的 Mac 点击下方链接即可添加，需先安装”快捷指令“

https://www.icloud.com/shortcuts/bf0fdad30e714a319b8836b6f7e64733

配合自动化或是桌面小组件更为方便。

## Windows

Shell脚本（使用git bash）：./Windows/iNUIST-win.sh

可执行文件（双击运行）：稍后上传

## Mac

Shell脚本（终端运行）：./Mac/iNUIST.sh

可执行文件（双击运行）：./Mac/iNUIST

# 使用说明

 1. Windows用户需要先安装git，使用`git bash`，在bash环境中运行脚本。
 2. Shell脚本中使用了第三方库jq用于解析返回结果的json，运行前请先安装jq。Mac用户可以使用brew进行安装（需先安装brew）：`brew install jq`。其它安装方式：https://github.com/stedolan/jq
 3. Shell脚本运行方式：`sh iNUIST.sh`
 4. 一键登录脚本中的请求内容均为抓包所得，不存在破解等非法操作。
 5. 一键登录脚本在测试时可以使用，但不保证在其他设备上正常运行。
 6. 请在遵守法律的前提下使用一键登录脚本。
