"""
@author kiwi 🥝
@date 2022.04.10

⊼².📹 Unit 1.8: VM Translator: Proposed Implementation

parser: parses each vm command into its lexical elements
    ☒ ignores all whitespace, full-line comments, midline comments
    hasMoreCommands() → boolean
    advance

    arg1 → string. returns 1st argument of current command
        not called for return
    arg2 → int. returns second argument of current command
        only called with push, pop, function, call

    commandType → arith, push, pop, label, goto, if, function, ret, call
        commands needed for project 7
            arithmetic+logical: [add sub neg, eq gt lt, and or not]
            memory access: pop segment i, push segment i

        commands needed for project 8
            branching: label, goto, if-goto
            function: function name nVars, call name nArgs, return

codeWriter: writes the assembly code that implements the parsed command
    opens file in constructor
    writeArithmetic
    writePushPop
    close

main: drives the process. input: fileName.vm, output: fileName.asm
    → iterate through fileName.vm, parse and output with comment
    more routines added in project 8


"""


from parser import Parser


def processLine():
    result = ''
    # push constant i assembly
    #   set SP to i
    #   SP++

    # parse push/pop memorySegmentName value

    # basic commands: add,

    print(result)


def main(file: str) -> None:
    parser = Parser(file)



main('vm/StackTest.vm')