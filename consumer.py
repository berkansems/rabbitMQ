import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue='authorized',durable=True)
channel.queue_declare(queue='notauthorized',durable=True)
#channel.queue_declare(queue='queue3', durable=True)
#
#
def callback(ch, method, properties, body):
    print("recieved data %r" % body)
    #hannel.basic_publish(exchange='exchange', routing_key='queue1', body=body)
    #hannel.basic_publish(exchange='exchange', routing_key='queue2', body=body)

channel.basic_consume('authorized',callback, auto_ack=True)
channel.basic_consume('notauthorized',callback, auto_ack=True)
#channel.basic_consume('queue2', callback,auto_ack=True)
#
channel.start_consuming()