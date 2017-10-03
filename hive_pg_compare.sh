#/bin/bash

scp -i ~/Downloads/openstack-keypair.pem.txt root@172.27.52.141:/tmp/pg.query.result /tmp/pg.query.result

scp -i ~/Downloads/openstack-keypair.pem.txt root@172.27.30.12:/tmp/hive.query.result /tmp/hive.query.result.tmp
#sed "s/'//g" /tmp/hive.query.result.tmp | sed "s/NULL//g" > /tmp/hive.query.result
sed "s/'//g" /tmp/hive.query.result.tmp  > /tmp/hive.query.result

gvimdiff /tmp/hive.query.result /tmp/pg.query.result
