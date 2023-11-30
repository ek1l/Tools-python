#!/usr/bin/python3

import urllib.request

site = urllib.request.urlopen("http://businesscorp.com.br")
server = site.info()
print("O servidor web está rodando:")
print(f"{server['server']}")
