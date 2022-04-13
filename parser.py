class Parser:
    def __init__(self, filename):
        vm = open(filename, 'r')
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
