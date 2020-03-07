# Logsplitter PoC

Proof of Concept for a Log-Splitter using Kafka and KSQL

## Usage

    docker-compose up -d

### Confluent

     cd confluent
     docker-compose up -d --build

Note: Check if all containers are running w/ `docker-compose ps`!

Navigate to http://localhost:9021 and follow [Confluent KSQL Docker Guide][confluent-ksql-docker-guide].

Example KSQL query to filter Stream on specific attribute

     CREATE STREAM test_user1 AS SELECT * FROM test WHERE userid = 'User_1';

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

* [Kafka Quickstart](https://kafka.apache.org/quickstart)

* [Kafka Docker Tutorial](http://wurstmeister.github.io/kafka-docker/)
* [Kafka Docker on Docker Hub](https://hub.docker.com/r/wurstmeister/kafka/)
* [Kafka Docker on Github](https://github.com/wurstmeister/kafka-docker/)
* [Kafka Docker - Connectivity Wiki article](https://github.com/wurstmeister/kafka-docker/wiki/Connectivity)

* [Confluent KSQL](https://www.confluent.io/product/ksql/)

[confluent-ksql-docker-guide]: https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html