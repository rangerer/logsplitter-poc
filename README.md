# Logsplitter PoC

Proof of Concept for a Log-Splitter using Kafka and KFL

## Usage

    docker-compose up -d

## Kafka Testing

Start an interactive container for Kafka

    docker-compose run kafka bash

Check the started installation

    $KAFKA_HOME/bin/kafka-topics.sh --bootstrap-server kafka:9092 --list
    $KAFKA_HOME/bin/kafka-topics.sh --bootstrap-server kafka:9092 --describe test

Produce a couple of messages for the `test` topic with

     $KAFKA_HOME/bin/kafka-console-producer.sh --broker-list="kafka:9092" --topic test

Consume the messages from the `test` topic with

     $KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test --from-beginning

## Links

* [Kafka Docker Tutorial](http://wurstmeister.github.io/kafka-docker/)
* [Kafka Docker on Docker Hub](https://hub.docker.com/r/wurstmeister/kafka/)
* [Kafka Docker on Github](https://github.com/wurstmeister/kafka-docker/)
* [Kafka Docker - Connectivity Wiki article](https://github.com/wurstmeister/kafka-docker/wiki/Connectivity)
* [Kafka Quickstart](https://kafka.apache.org/quickstart)
