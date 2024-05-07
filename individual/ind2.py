import os
import argparse

def tree(directory, indent='', last=True):
    contents = os.listdir(directory)
    for i, item in enumerate(contents):
        path = os.path.join(directory, item)
        if i == len(contents) - 1:
            print(indent + '└── ' + item)
            if os.path.isdir(path):
                tree(path, indent + '    ', last=True)
            else:
                tree(path, indent + '    ', last=False)
        else:
            print(indent + '├── ' + item)
            if os.path.isdir(path):
                tree(path, indent + '│   ', last=True)
            else:
                tree(path, indent + '│   ', last=False)

def main():
    parser = argparse.ArgumentParser(description='Analog of the "tree" utility in Linux.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(), help='Directory to display tree structure (default: current directory)')
    parser.add_argument('-d', '--directories-only', action='store_true', help='Display only directories')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: '{}' is not a directory.".format(args.directory))
        return

    if args.directories_only:
        tree(args.directory)
    else:
        print(args.directory)
        tree(args.directory)

if __name__ == '__main__':
    main()
