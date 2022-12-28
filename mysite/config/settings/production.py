from .base import *

import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False

ALLOWED_HOSTS = ["clarifyit.com"]

DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
    }
}
