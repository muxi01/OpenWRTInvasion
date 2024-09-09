#!/bin/bash
rm -rf    ./script_tools.tar
cp -rf    ./frps/frpc.toml   ./bin/frpc.toml
tar -cvf  ./script_tools.tar ./bin/*

