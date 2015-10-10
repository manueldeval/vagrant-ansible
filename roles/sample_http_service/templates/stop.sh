#! /bin/bash

pgrep -f 'python sample_http_service.py {{sample_http_service_port}}' | xargs kill -9

