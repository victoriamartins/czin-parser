from parser_gerado.GrammarParser import GrammarParser
from parser_gerado.GrammarLexer import GrammarLexer
from antlr4 import *

input_stream = FileStream('input.txt')

lexer = GrammarLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GrammarParser(stream)

tree = parser.start()