grammar Grammar;

/*
TODO: Tipos de dados: int, double, boolean, string
DONE: Variáveis locais e globais
TODO: Comandos de entrada e saída: printf e TODO: scanf
DONE: Controle de fluxo: if, if/else e switch
DONE: Laços de Repetição: while, do/while e for
TODO: Funções com passagem de parâmetro por valor e referência
TODO: Criação de bibliotecas externas e disponibilização de bibliotecas internas
*/

start: 
    INC_SIGN (include_)? (global_)* main_
    ;
include_:
    'include' ARQ ';'
    ;
global_:
    GB decl
    ;
main_:
    'main' OP CL 'begin' block* 'end'
    ;
block : 
    decl // no escopo das funções pode ter so atribuição
    | dec // decisao. começa com if
    | rept // repetição: while, do/while e for
    | prt
    ;
prt:
    'print' OP fact CL ';'
    ;
rept :
    WHL OP exp_dec CL 'begin' block+ 'end'
    | DOWL 'begin' block+ 'end' WHL OP exp_dec CL ';'
    | FOR OP decl exp_dec ';' VAR atr CL 'begin' block+ 'end' // isso ta horrivel. TODO: deixar bonito
    ;
decl :
    VAR (';'| atr ';')
    ;
atr :
    '=' fact
    ;
dec :
    'if' '(' exp_dec ')' 'begin' block+ 'end' rest*
    ;
rest : 
    'else' (dec | 'begin' block 'end') // dec --> else if. block --> else
    ;
exp_dec :
    fact rel_op fact
    ;
rel_op:
    EQ
    | DIF
    | PL
    | PL ATB // porquice, talvez tenha que mudar
    | MN
    | MN ATB // porquice, talvez tenha que mudar
    ;
fact:
    NUM 
    | VAR
    ;

INC_SIGN: '#';
ATB     : '=';
SMCL    : ';';
EQ      : '==';
DIF     : '!=';
PL      : '>';
MN      : '<';
INC     : 'include';
GB      : 'global';
VAR_B   : 'var';
BEGIN_B : 'begin';
END_B   : 'end';
MAIN    : 'main';
IF      : 'if';
ELSE    : 'else';
WHL     : 'while';
DOWL    : 'do';
FOR     : 'for';
OP      : '(';
CL      : ')';
NUM     : [0-9]+('.'[0-9]+)?;
ARQ     : [a-zA-Z]+'.'[a-z]+;
VAR     : '$'[a-z]+;
WS      : [ \n\t\r] -> skip;
PRT: 'print';