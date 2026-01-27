from confluent_kafka import Producer
import socket
from conf.server_conf import conf

# conf = {'bootstrap.servers': '192.168.8.254:9092',
 #       'client.id': socket.gethostname(),
  #      'auto.offset.reset': 'earliest'}
  
def test():
        print(conf)

producer = Producer(conf)