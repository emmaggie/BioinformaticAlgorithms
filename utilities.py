import unittest, argparse, os, re

class CliParser:

    @staticmethod
    def parseTheCli():
        parser = argparse.ArgumentParser()
        parser.add_argument('input_file', help="full path to the input file")
        args = parser.parse_args()
        return args.input_file

class FileParser:
    """"Parses the content of the input file.
        It is assumed the input file has structure:
            line 1: input
            line 2: output

        Input: file path.

    """
    def __init__(self, fn=None):
        self.file_name = fn
        self.input_line1 = None
        self.input_line2 = None

        if self.file_name != None:
            self.parseTheFile()

    def parseTheFile(self):
        with open(self.file_name, 'r') as rfh:
            content = rfh.readlines()
            self.input_line1 = content[0].strip()
            self.input_line2 = content[1].strip()


    def getInputLine1(self):
        return self.input_line1

    def getInputLine2(self):
        return self.input_line2

def main():
    #print(FileParser(r"C:\Users\StrzeleM\Downloads\rosalind_ba1a.txt").file_name)
    testInstance = FileParser(CliParser().parseTheCli())
    print(testInstance.getInputLine1())

if __name__ == "__main__":
    main()