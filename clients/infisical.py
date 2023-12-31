import logging

from infisical import InfisicalClient

from routes import config


class Infisical(InfisicalClient):
    def __init__(self, token, site_url):
        self.token = token
        self.site_url = site_url

        super().__init__(self.token, self.site_url)


client = Infisical(
    token=config['INFISICAL_TOKEN'],
    site_url='https://infisical.snowy.land'
)

try:
    GIST_URL = client.get_secret(secret_name="GIST_URL", environment=f"{config['ENVIRONMENT']}", path="/").secret_value
except Exception as e:
    logging.error(f'Error while getting GIST_URL from Infisical: {e}')
