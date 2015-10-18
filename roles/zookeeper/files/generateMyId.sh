#! /bin/bash
CONF=$1
MYID=$2

ips=`ip addr show | grep "inet " | sed 's/.*inet //' | sed 's/\/.*//'`
servers=`cat $CONF | grep server | sed 's/server\.//' | sed 's/:.*//'`

for ip in $ips
do
        for server in $servers
        do
                echo "$server" | grep "$ip" &> /dev/null
                RETVAL=$?
                if [ $RETVAL -eq 0 ]; then
                    echo $server | sed 's/=.*//' > /tmp/myid.new
                fi
        done
done

diff /tmp/myid.new $MYID &> /dev/null
RETVAL=$?

if [ $RETVAL -eq 0 ]; then
        exit 0
fi

cp /tmp/myid.new $MYID
exit 1
