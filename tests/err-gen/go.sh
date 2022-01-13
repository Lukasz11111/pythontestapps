#/bin/bash

 for test in $(seq 0 1 100); do
export REVDEBUG_RELEASE=$(echo $RANDOM | md5sum | head -c 20; echo;)
export REVDEBUG_VERSION=$(echo $RANDOM | md5sum | head -c 20; echo;)
 for test in $(seq 0 1 20); do
python & echo raise "errr"
# python version.py
done
done