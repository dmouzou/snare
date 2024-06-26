import string
import random
import os


def directory_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def generate_unique_path():
    path = "/home/ec2-user/snare/logs/" + directory_generator()
    while os.path.exists(path):
        path = "/home/ec2-user/snare/logs/" + directory_generator()
    return path
