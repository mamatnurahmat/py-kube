#!/usr/bin/env bash
NS=$1
if [[ ! -z $2 ]]
DEPLOY=$2
else
DEPLOY=""
fi
ns $NS > /dev/null 2>&1
docker run -v "$HOME/.kube/config:/root/.kube/config" -v "$(pwd):/play" -w /play newrahmat/py-kube python /app/main.py $NS $DEPLOY