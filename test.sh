#!/bin/bash

echo "feed message into test topic"
$KAFKA_HOME/bin/kafka-console-producer.sh \
    --broker-list="kafka:9092" \
    --topic test <<EOT
hello
world
test
hello world
awesome
why not
EOT

echo
echo "read messages from test_hello topic"
$KAFKA_HOME/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka:9092 \
    --topic test_hello \
    --from-beginning \
    --timeout-ms 5000