import pika

#Create a new instance of the Connection object
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


#Create a new channel with the next available channel number or pass in a channel number to use
channel = connection.channel()


# Declare queue, create if needed. This method creates or checks a queue. \
# When creating a new queue the client can specify various properties that control the durability of the queue and its contents,\
# and the level of sharing for the queue.
channel.queue_declare(queue='authorized', durable=True)
channel.queue_declare(queue='not_authorized', durable=True)



channel.basic_publish(exchange='authentication', routing_key='permited', body='send to queue1  4')
print("[x] Sent 'producer.py sent!'")

channel.basic_publish(exchange='authentication', routing_key='notpermited', body='send to queue2   5')
print("[x] Sent 'producer.py sent!'")


