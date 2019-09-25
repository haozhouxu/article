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

# Creating a queue using queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created.
channel.queue_declare(queue="hello")

# It works by subscribing a callback function to a queue
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

# And finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()