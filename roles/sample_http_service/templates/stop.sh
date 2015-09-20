#! /bin/bash

ps -ef | grep 'python sample_http_service.py' | awk '{print $2}'| xargs kill -9

