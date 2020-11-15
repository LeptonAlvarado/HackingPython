#!/usr/bin/env python
#_*_ coding: utf8 _*_

#Este programa hace consultad para obtener informacion del dns

import dns.resolver

def main():
    consultas = ['A', 'AAAA', 'NS', 'SOA', 'MX', 'MF', 'MD', 'TXT']
    for c in consultas:
        try:
            a = dns.resolver.query("google.com", c) # Se puede poner ANY dependiendo del sitio web
            for q in a:
                print(q)
        except:
            print("No es posible realizar esta consulta")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()