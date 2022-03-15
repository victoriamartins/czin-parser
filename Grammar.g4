grammar Grammar;

/*
DONE: Variáveis locais e globais
DONE: Comandos de entrada e saída: printf e scanf
DONE: Controle de fluxo: if, if/else e switch
DONE: Laços de Repetição: while, do/while e for
DONE: Funções com passagem de parâmetro por valor e referência
*/

start: 
    (global_)* functions* main_
    ;
functions:
        NAMEF OP decl* CL BEGIN_B block* END_B
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
    | prt // print
    | scan
    ;
scan:
    'scan' OP VAR CL ';'
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

SCAN    : 'scan';
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
NAMEF   : '_'[a-z]+('_')?('-')?[a-z]+;
NUM     : [0-9]+('.'[0-9]+)?;
ARQ     : [a-zA-Z]+'.'[a-z]+;
VAR     : '$'[a-z]+;
WS      : [ \n\t\r] -> skip;
PRT     : 'print';
