# there are no arguments for not; push(!pop)
import codewriter




class CodeWriter:
    """
    invoked with a VM command, .e.g 'push static 5' or 'add', to return a
    List[str] of Hack assembly commands that implement the VM command.
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')

    # writes to output file the asm commands that implement the vm command given
    def writeArithmetic(self, command) -> [str]:  # List[str] requires import
        # remember to add comments to each command!
        # arith = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        # self.output.write()

        self.output.write(f'writing asm code that implements {command}\n')
        # print(f'{command}→{command.split()[0]}')
        match command.split()[0]:
            case 'neg':
                return self.__writeNeg()
            case 'add':
                return self.__writeAdd()
            case 'not':
                return self.__writeNot()
            case _:
                print(f'command not found: {command}')

    # noinspection PyMethodMayBeStatic
    def __writeAdd(self) -> [str]:
        return [
            '// [ VM COMMAND ] add',
            '@SP',
            'AM=M-1',
            'D=M',      # D ← RAM[ RAM[SP-1] ], top of stack
            '@SP',
            'AM=M-1',
            'M=D+M',
            '@SP',
            'M=M-1'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeNeg(self) -> [str]:
        return [
            '// [ VM COMMAND ] neg',
            '@SP',
            'A=M-1',
            'M=-M'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeNot(self) -> [str]:
        return [
            '// [ VM COMMAND ] not',
            '@SP',
            'A=M-1',    # shortened from M=M-1; A=M
            'M=!M'      # don't need @SP; M=M+1
        ]

    # noinspection PyMethodMayBeStatic
    def __writePush(self, command: str, seg_location: int, n: int) -> [str]:
        """
        push segment i
            @i
            D=A
            @seg        all segments are pointers to some addr in RAM
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
        :param seg:
        :return:
        """
        return [
            '',
            ''
        ]

    # noinspection PyMethodMayBeStatic
    def __writePop(self, command: str, seg_location: int, n: int) -> [str]:
        """

        :param command:
        :param seg_location:
        :param n:
        :return:
        """
        return [
            '// [ VM COMMAND ] ' + command,
            '@'+str(n),
            'D=A',
            '@'+str(seg_location),
            'D=D+M',    # D=i+RAM[seg]
            '@popDest',
            'M=D'       # put RAM[seg]+i into popDest variable
            '@SP',
            'M=M-1',    # popping from the stack means decrementing SP
            'A=M',
            'D=M',      # pattern for de-referencing:
                        # equivalent to 'value at this RAM location'
                        # D ← RAM[value of SP]
                        # this is what we are popping
            '@popDest',
            'M=D'       # put popped value into RAM[seg]+i
        ]


    def writePushPop(self, command: str, segment: str, n: int) -> [str]:
        """
        remember to add comments to each command!
        pseudocode: all commands in format of push/pop segName i
            grab arg1 = seg, arg2 = i
            segment names need to be parsed and replaced with their values
                0   SP→256
                1   LCL
                2   ARG
                3   THIS
                4   THAT
                5   TEMP
                16  STATIC
                
                CONSTANT is only virtual
        """

        segDict = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'TEMP': 5,
            'STATIC': 16
        }

        self.output.write(f'writing asm code that implements {command}\n')

        match command.split()[0]:  # push or pop
            case 'pop':
                return self.__writePop(command, segDict[segment], n)
            case 'push':
                # take care of push constant i
                if segment == 'constant':
                    return [
                        '// [ VM COMMAND ] ' + command,
                        '@i',
                        'D=A',      # load value of i into register D
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1'
                    ]
                else:
                    return self.__writePush(command, segDict[segment], n)
            case _:
                raise ValueError(f'{command} is not valid in writePushPop')

    def close(self):
        self.output.close()
