from lexer import Lexer, Token

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        if self.current_token.type == 'NUMBER':
            result = self.current_token.value
            self.eat('NUMBER')
            if self.current_token.type == 'PLUS':
                self.eat('PLUS')
                result += self.parse()
            elif self.current_token.type == 'MINUS':
                self.eat('MINUS')
                result -= self.parse()
            return result
        else:
            self.error()

# Example usage
if __name__ == "__main__":
    text = "3 + 5 - 2"
    lexer = Lexer(text)
    parser = Parser(lexer)
    result = parser.parse()
    print(result)  # Output should be 6