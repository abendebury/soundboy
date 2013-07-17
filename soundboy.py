#!/usr/bin/python2.7

"""Decide what to do, then run the relevant file."""

import sys
import autotag
import import_tracks
import yaml

config = "./config.yaml"

def manual():
    print("Soundboy - a program to manage your music. Usage:")
    print("soundboy [command] [flags]")
    print("Commands:")
    print("import - import the files to the music library")
    sys.exit(2)

def main(argv):
    conf = yaml.safe_load(open(config))
    if(argv[0] == "import"):
        print("Importing files in the current directory.")
        import_tracks.main(argv[1:], conf)
        
    else:
        manual()

if(__name__ == "__main__"):
    main(sys.argv[1:])