# there are no arguments for not; push(!pop)
import enum


# enumeration for our equality helper function which creates asm for eq, lt, gt
class EqualityType(enum.Enum):
    EQ = 1
    LT = 2
    GT = 3


class CodeWriter:
    """
    invoked with a VM command, .e.g 'push static 5' or 'add', to return a
    List[str] of Hack assembly commands that implement the VM command.
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')
        self.eqCounter = 0
        self.ltCounter = 0
        self.gtCounter = 0

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
            case 'sub':
                return self.__writeSub()
            case 'eq':
                return self.__writeEq()
            case 'lt':
                return self.__writeLt()
            case 'gt':
                return self.__writeGt()
            case 'not':
                return self.__writeNot()
            case 'and':
                return self.__writeAnd()
            case 'or':
                return self.__writeOr()
            case _:
                print(f'command not found: {command}')

    # noinspection PyMethodMayBeStatic
    def __writeEq(self) -> [str]:
        return self.__equalityHelper('EQ')

    # noinspection PyMethodMayBeStatic
    def __writeLt(self) -> [str]:
        return self.__equalityHelper('LT')

    # noinspection PyMethodMayBeStatic
    def __writeGt(self) -> [str]:
        return self.__equalityHelper('GT')

    # noinspection PyMethodMayBeStatic
    def __equalityHelper(self, equalityType: str) -> [str]:
        """
        :return: list of assembly instructions equivalent to one of the three
        equality vm commands, eq, lt, gt
        """

        self.eqCounter += 1  # we need unique labels in asm for each translation
        n = str(self.eqCounter)

        # flow of this command:
        # check equality of top to elements of the stack
        #   if they are equal, set *(SP-2) to true, SP++
        #   if they aren't, set *(SP-2) to false, SP++
        #

        # below, when SP-1 or SP-2 are mentioned, they refer to the top and 2nd
        # values of the stack, where SP-1 is the top
        return [
            '// [ VM COMMAND ] ' + equalityType,

            # decrement stack pointer. load *(SP-1) → register D
            '@SP',
            'AM=M-1',  # combination of M=M-1, A=M
            'D=M',  # *(SP-1) → register D

            # time to grab *(SP-2)! value of 2nd stack element
            '@SP',
            'AM=M-1',
            'D=M-D',  # store *(SP-2) - *(SP-1) → register D

            # if top two elements of stack are equal, jump!
            #   i.e. if *(SP-1) == *(SP-2), jump
            '@PUSH_TRUE' + n,  # e.g. @PUSH_TRUE125
            'D;J' + equalityType,

            # we didn't jump, so top two elements of stack are not equal
            '@SP',
            'A=M',  # *(SP-2) = 0
            'M=0',  # 0 is false because it's 16 0's
            '@SP',  # SP++; stack pointer always points to next available
            # memory location on the stack
            'M=M+1',

            # go to END label; we want to skip the 'they were equal' part below
            '@END' + n,
            'D;JMP',  # D still stores *(SP-2) - *(SP-1)
                      # can optimize to JMP instead of JNE for eq ← cody

            # otherwise the elements were equal!
            '(PUSH_TRUE' + n + ')',  # if *(SP-1) == *(SP-2), *(SP-1)←true, SP++
            '@SP',  # *(SP-1)←true
            'A=M',
            'M=-1',  # -1 is true because it's 16 1's in two's complement
            '@SP',  # SP++
            'M=M+1',

            '(END' + n + ')'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeOr(self) -> [str]:  # same as 'and' but with one change
        """
        translates a vm 'or' command into its asm equivalent.
        pseudocode:
            a=pop()
            b=pop()
            push(a|b)
        :return:
        """
        return [        # when SP is mentioned, it refers to the original SP
            '// [ VM COMMAND ] or',
            '@SP',      # SP--
            'AM=M-1',
            'D=M',      # D ← RAM[RAM[SP-1]], top of stack
            '@SP',      # SP--
            'AM=M-1',
            'M=D|M',    # RAM[RAM[SP-2]] ← RAM[RAM[SP-1]] | RAM[RAM[SP-2]]
            '@SP',
            'M=M+1'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeAnd(self) -> [str]:
        """
        translates a vm 'and' command into its asm equivalent.
        pseudocode:
            a=pop()
            b=pop()
            push(a&b)
        :return:
        """
        return [        # when SP is mentioned, it refers to the original SP
            '// [ VM COMMAND ] and',
            '@SP',      # SP--
            'AM=M-1',
            'D=M',      # D ← RAM[RAM[SP-1]], top of stack
            '@SP',      # SP--
            'AM=M-1',
            'M=D&M',    # RAM[RAM[SP-2]] ← RAM[RAM[SP-1]] & RAM[RAM[SP-2]]
            '@SP',
            'M=M+1'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeAdd(self) -> [str]:
        return [
            '// [ VM COMMAND ] add',
            '@SP',
            'AM=M-1',   # SP--
            'D=M',      # D ← RAM[ RAM[SP-1] ], top of stack
            '@SP',
            'AM=M-1',
            'M=D+M',
            '@SP',
            'M=M+1'
        ]

    # noinspection PyMethodMayBeStatic
    def __writeSub(self) -> [str]:
        return [
            '// [ VM COMMAND ] sub',
            '@SP',
            'AM=M-1',
            'D=M',      # D ← RAM[ RAM[SP-1] ], top of stack
            '@SP',
            'AM=M-1',
            'M=M-D',    # RAM[SP-2] - RAM[SP-1]
            '@SP',
            'M=M+1'
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
        translates a vm 'push segment n' command to its equivalent asm
        :param command:
        :param seg_location:
        :param n:
        :return:
        """
        return [
            '// [ VM COMMAND ] ' + command,
            '@'+str(n),
            'D=A',
            '@'+str(seg_location),  # all segments are pointers to some RAM addr
            'D=D+M',    # D=i+RAM[seg]

            '@addr',
            'M=D',       # put RAM[seg]+i into addr variable
            'A=M',
            'D=M',      # D ← RAM[addr]

            '@SP',
            'A=M',      # RAM[SP]→A
            'M=D',      # *SP = *addr, i.e. RAM[RAM[SP]]=RAM[addr]

            '@SP',      # SP++
            'M=M+1'
        ]

    # noinspection PyMethodMayBeStatic
    def __writePop(self, command: str, seg_location: int, n: int) -> [str]:
        """
        translates a vm 'pop segment n' command to its equivalent asm
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
            'M=D',       # put RAM[seg]+i into popDest variable
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

        # segDict = {
        #     'SP': 0,
        #     'LCL': 1,
        #     'ARG': 2,
        #     'THIS': 3,
        #     'THAT': 4,
        #     'TEMP': 5,
        #     'STATIC': 16
        # }

        segDict = {
            'SP': 0,
            'local': 1,
            'argument': 2,
            'this': 3,
            'that': 4,
            'temp': 5,
            'static': 16
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

                        # *SP=i, SP++
                        '@'+str(n),
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
