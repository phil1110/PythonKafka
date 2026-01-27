from confluent_kafka import Producer
import socket
from conf.server_conf import conf
from datetime import datetime

# conf = {'bootstrap.servers': '192.168.8.254:9092',
 #       'client.id': socket.gethostname(),
  #      'auto.offset.reset': 'earliest'}

#producer = Producer(conf)

def test():
        print(conf)
        
def acked(err, msg):
        if err is not None:
                print("ERROR!\nMSG -> " + str(msg) + "ERR -> " + str(err))
        else:
                print("MSG PRODUCED -> " + str(msg))
        
def test_msg():
        msg = "TEST MESSAGE from " + str(socket.gethostname()) + " at " + str(datetime.now())
        
        with Producer(conf) as producer_2:
                producer_2.produce(topic="test", value="msg", key="test", callback=acked)
                producer_2.poll(1)                
        
        print("FOLLOWING MSG WAS PRODUCED:\n" + msg)