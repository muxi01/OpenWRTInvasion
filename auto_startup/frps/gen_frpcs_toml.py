#!/bin/python3
import os,sys 

FRPC_AUTH_TOKEN="12345678"
FRPC_SERVER_IP="x.x.x.x"

def gen_server():
    content ='bindAddr = "0.0.0.0"\n'
    content ='%sbindPort = 9600\n\n' % (content)
    content ='%sauth.method = "token"\n' % (content)
    content ='%sauth.token = "%s"\n\n\n' % (content,FRPC_AUTH_TOKEN)
    return content

def gen_head():
    content ='serverAddr = "%s"\n' % (FRPC_SERVER_IP)
    content ='%sserverPort = 9600\n\n' % (content)
    content ='%sauth.method = "token"\n' % (content)
    content ='%sauth.token = "%s"\n\n\n' % (content,FRPC_AUTH_TOKEN)
    return content

def gen_body(svrid:int,ipx:int,local=0,remote=0):
    content ='[[proxies]]\n'
    content ='%sname = "loccal_host%d_%d"\n' % (content,ipx,svrid)
    content ='%stype = "tcp"\n' % (content)
    
    if ipx == 0 :
        content ='%slocalIP = "127.0.0.1"\n' % (content)
        content ='%slocalPort = %d\n' % (content,local)
        content ='%sremotePort = %d\n\n\n' % (content,remote)
    else:
        content ='%slocalIP = "192.168.0.%d"\n' % (content,ipx)
        content ='%slocalPort = %d\n' % (content,local)
        content ='%sremotePort = %d\n\n\n' % (content,remote)
    return content


def write_file(fname:str,content:str):
    fo =open(fname,"w+")
    fo.write(content)
    fo.close()


def gen_client():
    config =gen_head()
    #localhost 80 <---> remote 9680
    config ="%s%s" % (config,gen_body(0,0,80,9680))

    #192.168.0.101 22 <-----> remote 9622
    config ="%s%s" % (config,gen_body(1,101,22,9622))
    return config 


if __name__ == '__main__':  
    config =gen_client()
    write_file("frpc.toml",config)

    config =gen_server()
    write_file("frps.toml",config)
