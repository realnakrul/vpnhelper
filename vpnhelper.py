#!/usr/bin/env python3


import platform
from pprint import pprint
import subprocess


SERVERS = {'Russia': [{'Russia': 'ru.asn247.net'}],
           'UK': [{'London 1': 'uk1.asn247.net'},
                  {'London 2': 'ukm11.asn247.net'}]}


def check_platform():
    current_platform = platform.system()
    result = False
    if current_platform != 'Linux':
        print(f"{current_platform} not supported yet")
    else:
        print(f"{current_platform} supported")
        result = True
    return result


def main():
    user, password = get_credentials()
    print(user, password)
    subprocess.run('dir')


def get_credentials():
    user = 'A'
    password = 'B'
    try:
        pass  #TODO: Read credentials from file
    except Exception as e:
        print(type(e))
    #TODO: if file not found request credentials
    return user, password


if __name__ == '__main__':
    pprint(SERVERS)
    if check_platform():
        main()
