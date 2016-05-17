#!/usr/bin/python3
import argparse
import logging

if __name__ == "__main__":
    # accept input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--listfile",help="a text FILE containing absolute paths of input files")
    parser.add_argument("-v","--verbose",help="increase output verbosity",action="store_true",dest="verbose",default=False)
    args = parser.parse_args()
    if args.verbose:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO

    # logging configurations
    logging.basicConfig(level=logging_level,\
                  filename="../run.log",\
                  format="%(asctime)s %(name)-10s %(levelname)-8s %(message)s",
                  mode="w")
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-10s %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    logging.info("logging configuration done")

    # pass command line configuration to main program
    confc = {"listfile":args.listfile}

    main(confc)
