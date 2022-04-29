// [ VM COMMAND ] push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] pop pointer 0
@SP
M=M-1
A=M
D=M
@3
M=D
// [ VM COMMAND ] push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] pop pointer 1
@SP
M=M-1
A=M
D=M
@4
M=D
// [ VM COMMAND ] push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] pop this 2
@2
D=A
@3
D=D+M
@popDest
M=D
@SP
M=M-1
A=M
D=M
@popDest
A=M
M=D
// [ VM COMMAND ] push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] pop that 6
@6
D=A
@4
D=D+M
@popDest
M=D
@SP
M=M-1
A=M
D=M
@popDest
A=M
M=D
// [ VM COMMAND ] push pointer 0
@0
D=A
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// [ VM COMMAND ] push pointer 1
@1
D=A
@3
A=D+A
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
// [ VM COMMAND ] push this 2
@2
D=A
@3
D=D+M
@addr
M=D
A=M
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
// [ VM COMMAND ] push that 6
@6
D=A
@4
D=D+M
@addr
M=D
A=M
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
