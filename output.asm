// [ VM COMMAND ] push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] pop static 8
@SP
AM=M-1
D=M
@Kiwi.8
M=D
// [ VM COMMAND ] pop static 3
@SP
AM=M-1
D=M
@Kiwi.3
M=D
// [ VM COMMAND ] pop static 1
@SP
AM=M-1
D=M
@Kiwi.1
M=D
// [ VM COMMAND ] push static 3
@Kiwi.3
D=M
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] push static 1
@Kiwi.1
D=M
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
// [ VM COMMAND ] push static 8
@Kiwi.8
D=M
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
