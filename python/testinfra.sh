# /bin/bash
if [ $# -eq 0 ]; then
    INFRA=$playbook_path
else
	INFRA=$1
fi

if [ "x$INFRA" == "x" ]; then
	INFRA=`cat .config | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["playbook_path"]';`
fi

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
OLDDIR=`pwd`


cd $DIR/..
export PYTHONPATH=$PYTHONPATH:./python/
python -m pytest -s ./${INFRA}/pytest/test.py 
cd $OLDDIR

