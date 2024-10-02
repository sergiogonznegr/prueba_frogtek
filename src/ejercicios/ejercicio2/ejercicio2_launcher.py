import argparse
import logging
import sys

from ejercicios.ejercicio2.ejercicio2 import delete_zeros, ip_has_left_zeros, make_new_ip, split_ip
from logging_custom.settings import setup_logging

log_level = getattr(logging, "Ejercicio 2", logging.INFO)
setup_logging(log_level)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--ip", type=str, help="IP de la que quitar los 0 a la izquierda", required=True)
    args = arg_parser.parse_args()
    ip = args.ip

    logging.info(f"La ip que se ha pasado es: '{ip}'")

    if not ip_has_left_zeros(ip=ip):
        logging.info("La IP tiene el formato correcto")
        sys.exit(1)

    logging.info("Se han encontrado ceros a la izquierda de algún subgrupo. Se van a eliminar")

    ip_splitted = split_ip(ip)
    ip_splitted = delete_zeros(splitted_ip=ip_splitted)
    new_ip = make_new_ip(elements_ip=ip_splitted)

    logging.info(f"La nueva IP formada es: '{new_ip}'")
