package kafka

import com.google.gson.Gson
import models.StreamIndividual


object KafkaController {
    val kafka = Kafka("kafka-server:9