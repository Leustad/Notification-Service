import logging

from infisical import InfisicalClient

from config import INFISICAL_TOKEN


client = InfisicalClient(
    site_url='https://infisical.snowy.land',
    token=INFISICAL_TOKEN,
    # site_url='http://192.168.1.247:8070'
)

try:
    GIST_URL = client.get_secret(secret_name="GIST_URL", environment="local_dev", path="/").secret_value
except Exception as e:
    logging.error(f'Error while getting GIST_URL from Infisical: {e}')
