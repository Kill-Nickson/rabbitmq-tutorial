# rabbitmq-tutorial

### Project's structure consists of 6 directories that describe  different topics about RabbitMQ
#### Here you can find next topics:
 * ** part1 ** - shows creating of 2 scripts for sending(sender.py)/receiving(worker.py) simple message via AMQP.
 * ** part2 ** - shows how to create the worker script allowing it to process the message (running simple function based on 
                 message as a parameter) and optimize the worker.
 * ** part3 ** - describes a way of creating a worker script that allows receiving a message by each of run workers.
 * ** part4 ** - explain how you can implement routing among several workers by criteria.
 * ** part5 ** - shows how to create a worker script implementing routing among several workers by several criteria.
 * ** part6 ** - demonstrates two scripts. The first one is implemented as a server receiving clients' requests to process the Fibonacci number.
                 While the second implements the client's side sending a request to calculate the Fibonacci number for 30.

The info shown through the tutorial is a combination composed of a full Python adaptation of official documentation and 
info provided by a @zTrue (habr.com's user) that explained all the topics in Russian but using PHP.
