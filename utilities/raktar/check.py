import yaml
import os
import sys
import glob
import argparse


def main():
    parameters = parse_args_or_die()
    sys.exit(
        check_storage_syntax(parameters, sys.stdout)
    )


def parse_args_or_die():
    parser = argparse.ArgumentParser(
        description="Check syntax of repository files"
    )
    parser.add_argument('root', help="Root of the repository")

    return parser.parse_args()


def check_storage_syntax(parameters, out):
    problems_found = False
    for filename in get_all_filenames(parameters.root):
        data = get_data_from(filename)
        problems = problems_with_data(data)
        for problem in problems:
            out.write("FAIL: {filename}:{problem}\n".format(
                filename=filename,
                problem=problem
            ))
            problems_found = True

    if problems_found:
        return 1
    else:
        out.write("OK\n")
        return 0


def get_all_filenames(root):
    search_pattern = os.path.join(root, "**", "*.yaml")
    return glob.iglob(search_pattern, recursive=True)


def get_data_from(filename):
    with open(filename, "rb") as fh:
        raw_data = fh.read()

    return yaml.load(raw_data.decode('utf-8'))


def problems_with_data(data):
    if 'items' not in data:
        yield 'Data dictionary must contain an items key'
    else:
        for idx, item in enumerate(data['items']):
            if 'name' not in item:
                yield 'No name key found within data item {0}'.format(idx)
            if 'url' not in item:
                yield 'No url key found within data item {0}'.format(idx)


if __name__ == "__main__":
    main()
