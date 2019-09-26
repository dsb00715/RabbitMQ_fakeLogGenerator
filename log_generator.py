import datetime
import numpy
import random
from faker import Faker
from tzlocal import get_localzone

local = get_localzone()


class LogApp:
    def __init__(self, sleep):
        self.sleep = sleep

    def generate_logs(self):
        global message
        faker = Faker()

        org_time = datetime.datetime.now()

        _response = ["200", "404", "500", "301"]

        _verb = ["GET", "POST", "DELETE", "PUT"]

        _level = ["alert", "critical", "error", "warning", "info"]
        # level = ["alert", "critical", "error", "warning"]

        resources = ["/list", "/wp-content", "/wp-admin", "/explore", "/search/tag/list", "/app/main/posts",
                     "/posts/posts/explore", "/apps/cart.jsp?appID="]

        faker_list = [faker.firefox, faker.chrome, faker.safari, faker.internet_explorer, faker.opera]

        flag = True
        while flag:
            if self.sleep:
                inc_time = datetime.timedelta(seconds=self.sleep)
            else:
                inc_time = datetime.timedelta(seconds=random.randint(30, 300))
            org_time += inc_time

            ip = faker.ipv4()
            da_ti = org_time.strftime('%d/%b/%Y:%H:%M:%S')
            timezone = datetime.datetime.now(local).strftime('%z')
            verb = numpy.random.choice(_verb, p=[0.6, 0.1, 0.1, 0.2])
            level = random.choice(_level)
            uri = random.choice(resources)
            if uri.find("apps") > 0:
                uri += str(random.randint(1000, 10000))

            response = numpy.random.choice(_response, p=[0.9, 0.04, 0.02, 0.04])
            byte = int(random.gauss(5000, 50))
            referer = faker.uri()
            user_agent = numpy.random.choice(faker_list, p=[0.5, 0.3, 0.1, 0.05, 0.05])()

            message = f"{ip} - - [{da_ti} {timezone}] [level:{level}] \"{verb} {uri} HTTP/1.0\" {response} {byte} " \
                      f"\"{referer}\" \"{user_agent}\" "
            flag = False

        return message
