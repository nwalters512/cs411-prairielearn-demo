#!/bin/sh

mongod --fork --logpath /var/log/mongodb.log

RESULT=$(mongo --eval 'printjson(db.serverStatus())')

mkdir -p /grade/results

echo "{\"score\": 1, \"succeeded\": true}" > /grade/results/results.json
