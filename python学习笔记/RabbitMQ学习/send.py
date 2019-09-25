# 安装pika：python -m pip install pika --upgrade

# 参考网址：https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

# 有密码方式
credit = pika.PlainCredentials("admin","admin")
cp = pika.ConnectionParameters(host="172.100.10.202",credentials=credit)
# 无密码方式
# cp = pika.ConnectionParameters(host="172.100.10.202")

connection = pika.BlockingConnection(cp)
channel = connection.channel()

# create a hello queue
channel.queue_declare(queue="hello")

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange. 
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ.
connection.close()