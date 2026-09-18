from pyspark.sql.functions import *
from pyspark.sql.types import *
# Event Hubs configuration
EH_NAMESPACE                    = "uberrealevents"
EH_NAME                         = "ubertopic"

import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("EVENTHUB_CONNECTION_STRING")
#EH_CONN_STR= spark.config.get("connection_string")
EH_CONN_STR = CONNECTION_STRING
KAFKA_OPTIONS = {
  "kafka.bootstrap.servers"  : f"{EH_NAMESPACE}.servicebus.windows.net:9093",
  "subscribe"                : EH_NAME,
  "kafka.sasl.mechanism"     : "PLAIN",
  "kafka.security.protocol"  : "SASL_SSL",
  "kafka.sasl.jaas.config"   : f"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username=\"$ConnectionString\" password=\"{EH_CONN_STR}\";",
  "kafka.request.timeout.ms" : 10000,
  "kafka.session.timeout.ms" : 10000,
  "maxOffsetsPerTrigger"     : 10000,
  "failOnDataLoss"           : 'true',
  "startingOffsets"          : 'earliest'
}

df=spark.readStream.format("kafka")\
            .options(**KAFKA_OPTIONS)\
            .load()
display(df,checkpointLocation="/Volumes/uber/bronze/my_volume/volume_folder/")
