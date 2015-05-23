#!/bin/bash
#Defining program variables

DC="/data/dead_characters.txt"
IP="/data/characters"
OP="/data/output"
HADOOP_JAR_PATH="/opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.5.0.jar"
MAPPER="got_living_m.py"
REDUCER="got_living_r.py"

hadoop fs -rmr -skipTrash $OP

hadoop jar  $HADOOP_JAR_PATH \
-file $MAPPER -mapper "python got_living_m.py" \
-file $REDUCER -reducer "python got_living_r.py" \
-cacheFile $DC#ref \
-input $IP -output $OP