class CodeWriter:
    def __init__(self, filename):
        self.output = open(filename, 'w')

    # writes to output file the asm commands that implement the vm command given
    def writeArithmetic(self, command):
        self.output.write(f'writing asm code that implements {command}\n')
        # try output.writelines! writes an array of strings

    def writePushPop(self, command):
        self.output.write(f'writing asm code that implements {command}\n')

    def close(self):
        self.output.close()