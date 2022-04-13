import enum


class Command(enum.Enum):
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9


class Parser:
    def __init__(self, filename):
        vm_file = open(filename, 'r')
        lines = vm_file.readlines()
        self.vm_commands = []
        self.commandIndex = 0  # current command index

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

            self.vm_commands.append(line)


    def getCurrentCommand(self) -> str:
        return self.vm_commands[self.commandIndex]


    def hasMoreCommands(self) -> bool:
        return self.commandIndex < len(self.vm_commands) - 1


    def advance(self) -> None:
        self.commandIndex += 1


    def getCommandType(self) -> Command:
        # arithmetic+logical: [add sub neg, eq gt lt, and or not]
        current = self.getCurrentCommand()
        tokens = current.split()

        command_name = tokens[0]
        arithmetic = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']

        if command_name in arithmetic:
            return Command.C_ARITHMETIC

        if command_name == 'pop':
            return Command.C_POP

        if command_name == 'push':
            return Command.C_PUSH

        raise ValueError(f'VM command not recognized: {self.getCurrentCommand()}')



    def test(self):
        current = self.getCurrentCommand()
        tokens = current.split()

        for t in tokens:
            print(f'{t}')


    def arg1(self) -> str:
        # TODO check: don't call if c_return
        #  return command (add, sub, etc) if c_arithmetic
        return self.getCurrentCommand().split()[1]


    def arg2(self) -> str:
        # TODO check: call only if current command is push, pop, function, call
        return self.getCurrentCommand().split()[2]