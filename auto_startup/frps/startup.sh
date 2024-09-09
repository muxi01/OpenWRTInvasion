#!/bin/sh
SCRIPT_LOCAL_PATH=/tmp/script_tools
SCRIPT_BIN_PATH=/tmp/script_tools/bin
SCRIPT_REMOTE_PATH=http://xxxxxx

export PATH=${PATH}:${SCRIPT_BIN_PATH}

while :
do
    [ -e ${SCRIPT_LOCAL_PATH} ] || mkdir -p ${SCRIPT_LOCAL_PATH}
    [ -e ${SCRIPT_LOCAL_PATH}/script_tools.tar ] || wget ${SCRIPT_REMOTE_PATH}/script_tools.tar  -O ${SCRIPT_LOCAL_PATH}/script_tools.tar
    [ -e ${SCRIPT_LOCAL_PATH}/script_tools.tar ] &&  tar -xvf  ${SCRIPT_LOCAL_PATH}/script_tools.tar  -C ${SCRIPT_LOCAL_PATH}/
    
    if [ $? = 0 ] ; then
        ${SCRIPT_BIN_PATH}/busybox telnetd
        ${SCRIPT_BIN_PATH}/frpc -c ${SCRIPT_BIN_PATH}/frpc.toml > /dev/null  &
        break
    else 
        rm -rf ${SCRIPT_LOCAL_PATH}
    fi
    sleep 30
done

while :
do 
    flag=$(ps |grep frpc |grep script_tools) 
    [ "${flag}x" = "x" ] &&  ${SCRIPT_BIN_PATH}/frpc -c ${SCRIPT_BIN_PATH}/frpc.toml > /dev/null  &
    sleep 60
done
