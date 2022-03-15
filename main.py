from parser_gerado.GrammarParser import GrammarParser
from parser_gerado.GrammarLexer import GrammarLexer
from antlr4 import *

'''
def upload_include(entrada):
    arq_compilar = open(entrada, 'r').readlines()
    arq_compilar_writable = open(entrada, 'w')

    for linha in arq_compilar:
        if linha[0] == '#':
            nome_include = ''
            for caracter in linha:
                if caracter != ';' and caracter != '#' and caracter != '\n':
                    nome_include += caracter
            print(nome_include)

            #abrir arquivo
            #injetar conteúdo do arquivo deletando a linha do include
        else:
            break'''
    

entrada = 'input.txt';
# upload_include(entrada)


input_stream = FileStream(entrada)

lexer = GrammarLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GrammarParser(stream)

tree = parser.start()