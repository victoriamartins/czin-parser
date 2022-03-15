from parser_gerado.GrammarParser import GrammarParser
from parser_gerado.GrammarLexer import GrammarLexer
from antlr4 import *


def upload_include(entrada):
    arq_compilar = open(entrada, 'r').readlines()
    arq_compilar_writable = open(entrada, 'w')

    for linha in arq_compilar:
        if linha[0] == '#':
            nome_include = ''
            for caracter in linha:
                if caracter != ';' and caracter != '#' and caracter != '\n':
                    nome_include += caracter
            arq_incluir = open(nome_include, 'r').readlines()
            for linha_incluir in arq_incluir:
                arq_compilar_writable.write(linha_incluir)
        else:
            break

    for linha in arq_compilar:
        if linha[0] != '#':
            arq_compilar_writable.write(linha)
    

entrada = 'input.txt'
upload_include(entrada)

input_stream = FileStream(entrada)

lexer = GrammarLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GrammarParser(stream)

tree = parser.start()
