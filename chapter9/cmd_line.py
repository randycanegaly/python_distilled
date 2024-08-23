def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage : python {argv[0]} inputfile outputfile \n')
    inputfile = argv[1]
    outputfile = argv[2]
    print(f'I\'m hoobin\' a jabber {inputfile}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
