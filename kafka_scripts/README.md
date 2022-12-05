
# Kafka

Kafka was chosen as the mediator between the GGP(application that gonna create possible machine learning pipelines) and the consumers (applications
that gonna evaluate the created pipelines)

This project deployed Kafka using Docker, so, the first step is to install Docker on your machine to make it work.

## 1. Setup

It's necessary to change your IP address on the kafka container to your machine ip.
For unix based SO just run the command 

```bash
ifconfig |grep inet
```

to discover your machine IP. 

Open your file "/etc/hosts" with admin permission and your favorite editor.
Add the following line to the final of this file:

```bash
<YOUR_IP> kafka_server
```

To test if everything worked just use the command

```bash
ping kafka-server
```