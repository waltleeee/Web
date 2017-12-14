
import sys
import hashlib

def main():
    argv = list(sys.argv)
    argv.pop(0)

    filepath = argv.pop(0)

    print filepath

    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        md5.update(f.read())

    print md5.hexdigest()
    raw_input()



if __name__ == "__main__":
    main()
