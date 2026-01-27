import socket

conf = {'bootstrap.servers': '192.168.8.254:9092',
        'client.id': socket.gethostname(),
        'auto.offset.reset': 'earliest'}