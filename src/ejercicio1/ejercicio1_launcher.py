import argparse
import logging

from ejercicio1 import get_numbers, sum_numbers
from logging_custom.settings import setup_logging

log_level = getattr(logging, "Ejercicio 1", logging.INFO)
setup_logging(log_level)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--text_string", type=str, help="Cadena de la que se van a sacar los números", required=True
    )
    args = arg_parser.parse_args()

    logging.info(f"La string que se ha pasado es: '{args.text_string}'")

    numbers_list = get_numbers(args.text_string)
    logging.debug(f"El listado de números que se han extraído es: {numbers_list}")
    sum_result = sum_numbers(numbers_list=numbers_list)

    logging.info(f"La suma resultante de los números extraídos es: {sum_result}")
