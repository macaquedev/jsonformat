import json
import argparse


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename for formatting")
    parser.add_argument("-q", "--quiet", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if not args.quiet:
        print("Parsing and outputting file:")

    with open(args.filename) as f:
        data = json.load(f)

    with open(args.filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    if not args.quiet:
        print("Done.")
