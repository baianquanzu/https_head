# -*- coding: utf-8 -*-
import sys
import getopt

def add_https_to_urls(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for line in lines:
            new_line = "https://www.{}\n".format(line.strip())
            file.write(new_line)
            

def main(argv):
    input_file = ''
    output_file = 'output.txt'
    try:
        opts, args = getopt.getopt(argv, "hw:o:", ["input_file=", "output_file="])
    except getopt.GetoptError:
        print('Usage: script.py -w <inputfile> [-o <outputfile>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: script.py -w <inputfile> [-o <outputfile>]')
            sys.exit()
        elif opt in ("-w", "--input_file"):
            input_file = arg
        elif opt in ("-o", "--output_file"):
            output_file = arg
    if input_file == '':
        print('输入-w选择你的txt文件，-o设置你需要输出的文件名')
        sys.exit(2)
    
    add_https_to_urls(input_file, output_file)
    print("it is OK")

if __name__ == "__main__":
    main(sys.argv[1:])
