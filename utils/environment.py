import os

from dotenv import load_dotenv, find_dotenv


def get_environment_variable(name):
    load_dotenv(find_dotenv())
    env_var = os.getenv(name)
    return env_var
