import pika
from log_generator import LogApp
import argparse
import re

parser = argparse.ArgumentParser(description="Fake Apache Log Generator")
parser.add_argument("--num", "-n", dest='num_lines', help="Number of lines to generate (0 for infinite)", type=int,
                    default=1)
parser.add_argument("--sleep", "-s", dest='time_sleep',
                    help="Sleep this long between lines (in seconds)", default=0.0, type=float)

args = parser.parse_args()

n_logs = args.num_lines
t_sleep = args.time_sleep

credentials = pika.PlainCredentials('Deep', '******')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', virtual_host='test_deep', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

for n in range(n_logs):
    _lg = LogApp(t_sleep)
    message = _lg.generate_logs()
    r_severity = re.search('level:(.*)]', message)
    severity = r_severity.group(1)
    # print(severity)
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))

connection.close()
