# /bin/bash

INFRA=$1
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
OLDDIR=`pwd`


cd $DIR/..
export PYTHONPATH=$PYTHONPATH:./python/
python -m pytest -s ./infrastructures/${INFRA}/pytest/test.py 
cd $OLDDIR

