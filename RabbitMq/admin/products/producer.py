import pika, json

params = pika.URLParameters('amqps://vyoqndfg:Ntm9vJDjbkpSUmzYHaLuJRuuXMuW6Zjj@cow.rmq2.cloudamqp.com/vyoqndfg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)