import re
import os

script_dir = os.path.dirname(__file__)

def format(log_folder, plot_folder):

    in_file = os.path.join(script_dir, "..", log_folder, "pidstat.log")
    out_file = os.path.join(script_dir, "..", plot_folder, "pidstat.dat")

    with open(in_file) as fp_in, \
            open(out_file, "w") as fp_out:
        lines = fp_in.read().splitlines()
        idx = 3 # skipping headers
        while idx < len(lines):
            if len(lines[idx]) > 0 and lines[idx].find('#') == -1:
                line_tokens = lines[idx].split()
                del line_tokens[len(line_tokens) - 1]
                line_out = ' '.join(line_tokens) # getting rid of extra spaces
                fp_out.write(line_out + '\n')
            idx = idx + 1
    return
