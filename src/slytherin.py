import os
import argparse
import re
import regex_cases


args = None


def is_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file {} does not exist. Please provide a valid file.".format(arg))
    else:
        return arg


def apply_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = lambda arg: is_file(parser, arg))
    args = parser.parse_args()


def get_file():
    global args
    f = open(args.filename, 'r')
    val = f.read()
    f.close()
    return val


def camel_to_snake(val):
    tmp = filter(None, re.split('([A-Z][a-z]+)', val.group(0)))
    tmp = "_".join(tmp)
    return tmp.lower()


def alter_filename(name):
    directoryList = name.split('/')
    name = directoryList.pop()
    name = "converted-" + name.lower()
    directoryList.append(name)
    return "/".join(directoryList)


def convert_file(val):
    global args
    val = re.sub(regex_cases.camel_case, camel_to_snake, val)
    f = open(alter_filename(args.filename), 'w')
    f.write(val)
    f.close()


def run():
    apply_args()
    file_string = get_file()
    convert_file(file_string)

if __name__ == "__main__":
    run()
