# 南京信息工程大学 i-NUIST 校园网一键登录脚本（Windows版本） 
# 作者：Switernal
# 联系方式：switernal@outlook.com
# 使用方式：替换掉个人信息，使用Powershell执行即可
# 使用说明：
# 	由于使用第三方库jq进行json解析
# 	Windows版本需要配合jq-win64.exe一起使用，请把jq-win64.exe放在shell脚本同一目录下
# 	如果能把jq加入系统环境变量中，也可以直接用
# 	也可以考虑使用其他json解析工具

# --- 填写用户信息 ---
# 1.手机号
username=15300000000

# 2.密码
password=123456

# 3.运营商
#	2：中国移动
# 	3：中国电信
#	4：中国联通
channel=3

# 4.是否自动登录
isAutoLogin=0

# 获取ip
ipRes=`curl -H 'Host: 10.255.255.34' -H 'Accept: application/json, text/plain, */*' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' -H 'Referer: http://10.255.255.34/authentication' -H 'Accept-Language: zh-CN,zh;q=0.9' --compressed 'http://10.255.255.34/api/v1/ip' > ipResult.json`
ip=`jq-win64.exe .data ipResult.json | awk -F \" '{print $2}' ` 
`rm ipResult.json`
echo $ip

# ----- 登录部分 -----
# 需要使用到第三方库jq解析json，Mac用户可以使用`brew install jq`进行安装
# Windows和Mac用户也可以到 https://github.com/stedolan/jq/releases 获取
# 如果是直接获取jq可执行版本，需要修改下面对应的jq命令，请自行调试

# 发起登录请求
loginQuery=`curl -H 'Host: 10.255.255.34' -H 'Accept: application/json, text/plain, */*' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' -H 'Origin: http://10.255.255.34' -H 'Referer: http://10.255.255.34/authentication/login' -H 'Accept-Language: zh-CN,zh;q=0.9' --data-binary '{"username":"'$username'","password":"'$password'","channel":"'$channel'","ifautologin":"'$isAutoLogin'","pagesign":"secondauth","usripadd":"'$ip'"}' --compressed 'http://10.255.255.34/api/v1/login' > loginResult.json`

# 打印登录结果
echo "\n 登录结果"
echo 'code:	  ' `jq-win64.exe .code loginResult.json`
echo 'message:  ' `jq-win64.exe .message loginResult.json`
echo 'username: ' `jq-win64.exe .data.username loginResult.json`
echo 'outport:  ' `jq-win64.exe .data.outport loginResult.json`
echo 'ip:	  ' `jq-win64.exe .data.usripadd loginResult.json`
`rm loginResult.json`
