import argparse
#Python Distilled page 255

def main(argv):
    p = argparse.ArgumentParser(description="Some Hoobergram")

    p.add_argument("infile")
    p.add_argument("-o", "--output", action="store")
    p.add_argument("-d", "--debug", action="store_true", default=False)
    

    args = p.parse_args(args=argv)

    infile = args.infile
    output = args.output
    debugmode = args.debug


    print(infile, output, debugmode)



if __name__ == '__main__':
    import sys
    main(sys.argv)
