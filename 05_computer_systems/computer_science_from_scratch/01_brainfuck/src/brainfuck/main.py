from argparse import ArgumentParser
from .brainfuck import Brainfuck


def execute():
    file_parser = ArgumentParser("Brainfuck")
    file_parser.add_argument(
        "brainfuck_file", help="A file containing Brainfuck source code."
    )
    arguments = file_parser.parse_args()
    Brainfuck(arguments.brainfuck_file).execute()


if __name__ == "__main__":
    execute()
