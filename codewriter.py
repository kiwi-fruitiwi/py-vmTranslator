class CodeWriter:
    def __init__(self, filename):
        self.output = open(filename, 'w')

    # writes to output file the asm commands that implement the vm command given
    def writeArithmetic(self, command):
        self.output.write(f'writing asm code that implements {command}\n')
        # try output.writelines! writes an array of strings

    def writePushPop(self, command):
        """
        general solution for pop segment i
            @i
            D=M
            @seg
            D=D+M       D=RAM[seg]+i

            @popDest
            M=D         put RAM[seg]+i into popDest variable

            @SP
            M=M-1       popping from the stack means decrementing SP

            A=M
            D=M         pattern for de-referencing: 'value at this RAM location'
                        D ← RAM[value of SP]
                        this is what we are popping

            @popDest
            M=D         put popped value into RAM[seg]+i


        general solution for push segment i
            @i
            D=M
            @seg        seg is a value in some RAM location pointing to an addr
            D=D+M       D ← segmentPointer + i

            @addr
            M=D         addr ← segmentPointer + i
            A=M
            D=M         D ← RAM[addr]

            @SP
            A=M         put RAM[SP] → A

            M=D         RAM[RAM[SP]] = RAM[addr], i.e. *SP=*addr
            @SP
            M=M+1       SP++; move the stack pointer forward one slot

        :param command:
        :return:
        """
        self.output.write(f'writing asm code that implements {command}\n')

    def close(self):
        self.output.close()