from parser import Parser
from lexer import Lexer

class Compiler:
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.parser = Parser(self.lexer)

    def compile(self):
        return self.parser.parse()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python compiler.py <source_code>")
        sys.exit(1)

    source_code = sys.argv[1]
    compiler = Compiler(source_code)
    result = compiler.compile()
    print(f"Compiled result: {result}")