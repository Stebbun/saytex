import sys
import os

def play_script(out_dir):
    filename = os.path.join(out_dir, "command_sequence")
    file = open(filename, "r")
    for line in file:
        os.system(line)

def main():
    play_script(sys.argv[1])

if __name__== "__main__":
    main()
