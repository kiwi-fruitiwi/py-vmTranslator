"""
@author kiwi 🥝
@date 2022.04.10

⊼².📹 Unit 1.8: VM Translator: Proposed Implementation

parser: parses each vm command into its lexical elements
    ignores all whitespace, full-line comments, midline comments
    hasMoreCommands() → boolean
    advance
    commandType → arith, push, pop, label, goto, if, function, ret, call
    arg1 → string. returns 1st argument of current command
        not called for return
    arg2 → int. returns second argument of current command
        only called with push, pop, function, call

codeWriter: writes the assembly code that implements the parsed command
    opens file in constructor
    writeArithmetic
    writePushPop
    close

main: drives the process. input: fileName.vm, output: fileName.asm
    → iterate through fileName.vm, parse and output with comment
    more routines added in project 8
"""


def test(file: str) -> None:
    vm = open(file, 'r')
    lines = vm.readlines()


    for line in lines:
        # ignore whitespace
        if line == '\n':
            continue

        # ignore entire-line comments
        if line[0] == '/' and line[1] == '/':
            continue

        # ignore mid-line comments
        try:
            index = line.index('//')
            line = line[0:index]
        except ValueError:
            # '//' wasn't found!
            pass

        # strip whitespace
        line = line.strip()

        print(f'{line}')


test('vm/StackTest.vm')