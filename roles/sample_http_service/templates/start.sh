#! /bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $DIR
nohup python sample_http_service.py {{sample_http_service_port}} &> /dev/null &




