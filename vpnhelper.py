import platform
import os
from pprint import pprint


SERVERS = {'Russia': [{'Russia': 'ru.asn247.net'}],
           'UK': [{'London 1': 'uk1.asn247.net'},
                  {'London 2': 'ukm11.asn247.net'}]}


def check_platform():
    current_platform = platform.system()
    result = False
    if current_platform == 'Linux':
        print(f"{current_platform} not supported yet")
    else:
        print(f"{current_platform} supported")
        result = True
    return result


def main():
    os.system('dir')


if __name__ == '__main__':
    pprint(SERVERS)
    print(platform.system())
    if check_platform():
        main()
