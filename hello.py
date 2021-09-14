import argparse


def hello(name):
    print(f"Hello, {name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", action="store", nargs="?", help="Your name")
    args = parser.parse_args()
    hello(args.name)


if __name__ == "__main__":
    main()
