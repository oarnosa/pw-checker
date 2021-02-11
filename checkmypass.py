#!/usr/bin/env python3
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error Fetching: {res.status_code}, check api and try again')
    return res


def pwned_api_check(password):
    # check password if it exists in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first5_char)
    return res


# request_api_data('123')
print(pwned_api_check('123'))
