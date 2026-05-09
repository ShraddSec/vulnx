import validators
import ipaddress
from urllib.parse import urlparse


def validate_url(url):

    if not validators.url(url):
        return False

    parsed = urlparse(url)

    host = parsed.hostname

    try:
        ip = ipaddress.ip_address(host)

        if ip.is_private:
            return False

    except:
        pass

    return True