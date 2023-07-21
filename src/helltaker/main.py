import argparse

import pyxel

import game

def main():
    parser = argparse.ArgumentParser(
        "Helltaker",
        description="An implementation of Helltaker in Python"
    )
    parser.add_argument("-d", "--debug", action="store_true")

    debug = False
    args = parser.parse_args()

    if args.debug:
        debug = True

    game.App(debug)

if __name__ == "__main__":
    main()