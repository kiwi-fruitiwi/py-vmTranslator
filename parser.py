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


    def showCommands(self) -> None:
        for line in self.vm_commands:
            print(f'{line}')


    def getCurrentCommand(self) -> str:
        return self.vm_commands[self.commandIndex]


    def hasMoreCommands(self) -> bool:
        return self.commandIndex < len(self.vm_commands) - 1


    def advance(self) -> None:
        self.commandIndex += 1


    def getCommandType(self) -> Command:
        # TODO stub file; fix this later
        return Command.C_ARITHMETIC