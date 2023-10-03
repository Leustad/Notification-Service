from dotenv import dotenv_values


def setup_config():
    return dotenv_values('.env')
