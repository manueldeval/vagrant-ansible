# /bin/bash
if [ $# -eq 0 ]; then
    INFRA=$playbook_path
else
	INFRA=$1
fi

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
OLDDIR=`pwd`


cd $DIR/..
export PYTHONPATH=$PYTHONPATH:./python/
python -m pytest -s ./${INFRA}/pytest/test.py 
cd $OLDDIR

