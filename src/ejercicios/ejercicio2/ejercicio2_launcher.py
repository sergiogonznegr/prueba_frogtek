import argparse
import logging
import sys

from ejercicios.ejercicio2.ejercicio2 import delete_zeros, is_correct_ip_format, make_new_ip, split_ip
from logging_custom.settings import setup_logging

log_level = getattr(logging, "Ejercicio 2", logging.INFO)
setup_logging(log_level)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--ip", type=str, help="IP de la que quitar los 0 a la izquierda", required=True)
    args = arg_parser.parse_args()

    logging.info(f"La ip que se ha pasado es: '{args.ip}'")
    if not is_correct_ip_format(ip=args.ip):
        logging.error("La IP introducida no tiene el formato correcto. El formato deber ser XXX.XXX.XXX.XXX")
        sys.exit(1)

    logging.debug("La ip es tiene el formato correcto")
    ip_splitted = split_ip(args.ip)
    ip_splitted = delete_zeros(splitted_ip=ip_splitted)
    new_ip = make_new_ip(elements_ip=ip_splitted)

    logging.info(f"La nueva IP formada es: '{new_ip}'")
