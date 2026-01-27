from producer import producer


def run(entries, timeout):
    producer.produce("orders.incoming") 