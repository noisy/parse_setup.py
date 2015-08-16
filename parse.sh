#!/usr/bin/env bash

ID=$(cat $@ | docker run -i -a stdin parse /parse.py ); docker wait $ID > /dev/null ;
docker logs $ID
