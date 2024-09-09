#拷贝auto_startup到你服务器
---
# 1.修改gen_frpcs_toml.py 脚本
## 修改参数
* 修改 FRPC_AUTH_TOKEN 成随机长字符串的内容
* 修改 FRPC_SERVER_IP 成你服务器IP
## 2.添加你的端口
* 在gen_client 中添加端口， gen_body(1,101,22,9622) 服务ID 主机地址 本地服务端口号  远程服务端口
## 3.生成配置文件
python3  gen_frpcs_toml.py
# 2.修改startup.sh脚本
* 修改 SCRIPT_REMOTE_PATH 成你服务器的脚本工具存放路径（不包含脚本工具本身）
# 3.生成script_tools.tar
* ./compress.sh
# 4.下载startup.sh 到路由器
*  wget 你的服务器/xxxxx/startup.sh   -O /userdisk/startup.sh
*  chmod +x /userdisk/startup.sh
# 5.开机启动服务器
*  在/etc/rc.local 中添加 /userdisk/startup.sh &

# 6.服务器运行 frps -c frps.toml

