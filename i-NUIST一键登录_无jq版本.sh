# 南京信息工程大学 i-NUIST 校园网一键登录脚本(无需jq版本)
# 作者：Switernal
# 联系方式：switernal@outlook.com
# 使用说明：
# 	按需替换下面的个人信息即可使用
# 登录结果说明：
# 	code == 200 && message == "ok" 即为登陆成功
# 	浏览器中打开登录页可能还是显示未登录状态，但是此时已经可以上网了，不影响使用
# 	如果code == 201或其它即为登录失败，请参考message中的错误信息


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


# ----- 登录部分 -----
# 获取ip

# ip请求结果json存到./ipResult.json
ipRes=`curl -H 'Host: 10.255.255.34' -H 'Accept: application/json, text/plain, */*' -H 'User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' -H 'Referer: http://10.255.255.34/authentication' -H 'Accept-Language: zh-CN,zh;q=0.9' --compressed 'http://10.255.255.34/api/v1/ip'`

# 解析json得到ip
ip=`echo "$ipRes" | grep -Eo "((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))"` 

echo $ip

# 发起登录请求，结果暂存到./loginResult.json
loginQuery=`curl -H 'Host: 10.255.255.34' -H 'Accept: application/json, text/plain, */*' -H 'User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' -H 'Origin: http://10.255.255.34' -H 'Referer: http://10.255.255.34/authentication/login' -H 'Accept-Language: zh-CN,zh;q=0.9' --data-binary '{"username":"'$username'","password":"'$password'","channel":"'$channel'","ifautologin":"'$isAutoLogin'","pagesign":"secondauth","usripadd":"'$ip'"}' --compressed 'http://10.255.255.34/api/v1/login' > login.json`

# 打印登录结果
echo "\n 登录结果"
cat login.json
rm login.json
