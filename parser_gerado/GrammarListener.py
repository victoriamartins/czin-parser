# Generated from Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#functions.
    def enterFunctions(self, ctx:GrammarParser.FunctionsContext):
        pass

    # Exit a parse tree produced by GrammarParser#functions.
    def exitFunctions(self, ctx:GrammarParser.FunctionsContext):
        pass


    # Enter a parse tree produced by GrammarParser#global_.
    def enterGlobal_(self, ctx:GrammarParser.Global_Context):
        pass

    # Exit a parse tree produced by GrammarParser#global_.
    def exitGlobal_(self, ctx:GrammarParser.Global_Context):
        pass


    # Enter a parse tree produced by GrammarParser#main_.
    def enterMain_(self, ctx:GrammarParser.Main_Context):
        pass

    # Exit a parse tree produced by GrammarParser#main_.
    def exitMain_(self, ctx:GrammarParser.Main_Context):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#scan.
    def enterScan(self, ctx:GrammarParser.ScanContext):
        pass

    # Exit a parse tree produced by GrammarParser#scan.
    def exitScan(self, ctx:GrammarParser.ScanContext):
        pass


    # Enter a parse tree produced by GrammarParser#prt.
    def enterPrt(self, ctx:GrammarParser.PrtContext):
        pass

    # Exit a parse tree produced by GrammarParser#prt.
    def exitPrt(self, ctx:GrammarParser.PrtContext):
        pass


    # Enter a parse tree produced by GrammarParser#rept.
    def enterRept(self, ctx:GrammarParser.ReptContext):
        pass

    # Exit a parse tree produced by GrammarParser#rept.
    def exitRept(self, ctx:GrammarParser.ReptContext):
        pass


    # Enter a parse tree produced by GrammarParser#decl.
    def enterDecl(self, ctx:GrammarParser.DeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#decl.
    def exitDecl(self, ctx:GrammarParser.DeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#atr.
    def enterAtr(self, ctx:GrammarParser.AtrContext):
        pass

    # Exit a parse tree produced by GrammarParser#atr.
    def exitAtr(self, ctx:GrammarParser.AtrContext):
        pass


    # Enter a parse tree produced by GrammarParser#dec.
    def enterDec(self, ctx:GrammarParser.DecContext):
        pass

    # Exit a parse tree produced by GrammarParser#dec.
    def exitDec(self, ctx:GrammarParser.DecContext):
        pass


    # Enter a parse tree produced by GrammarParser#rest.
    def enterRest(self, ctx:GrammarParser.RestContext):
        pass

    # Exit a parse tree produced by GrammarParser#rest.
    def exitRest(self, ctx:GrammarParser.RestContext):
        pass


    # Enter a parse tree produced by GrammarParser#exp_dec.
    def enterExp_dec(self, ctx:GrammarParser.Exp_decContext):
        pass

    # Exit a parse tree produced by GrammarParser#exp_dec.
    def exitExp_dec(self, ctx:GrammarParser.Exp_decContext):
        pass


    # Enter a parse tree produced by GrammarParser#rel_op.
    def enterRel_op(self, ctx:GrammarParser.Rel_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#rel_op.
    def exitRel_op(self, ctx:GrammarParser.Rel_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#fact.
    def enterFact(self, ctx:GrammarParser.FactContext):
        pass

    # Exit a parse tree produced by GrammarParser#fact.
    def exitFact(self, ctx:GrammarParser.FactContext):
        pass



del GrammarParser