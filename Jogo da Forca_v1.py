# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Lista com o status do Board (tabuleiro)
# Obs.: As três aspas servem para fazer uma string de mais de uma linha.
board = ['''

+---+
|   |
    |
    |
    |
    |
========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.correct = []
        self.incorrect = [] # Servirá como index do board

    # Método para adivinhar a letra
    def guess(self, letter):
        # Se a palavra contém a letra, adiciona à lista das palavras corretas, senão adiciona às incorretas
        if (letter in self.word ):
            if not(letter in self.correct):
                self.correct.append(letter)
                self.correct.sort()
            return True
        else:
            if not (letter in self.incorrect):
                self.incorrect.append(letter)
                self.incorrect.sort()
            return False

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        # O jogo termina quando o jogador venceu
        # Ou quando chega ao fim da lista do board
        return (self.hangman_won() or (len(self.incorrect) == len(board) - 1))

    # Método para verificar se o jogador venceu
    # Verifica se acertou todas as letras da palavra
    def hangman_won(self):
        return (all(item in self.correct for item in self.word))

    # Método para não mostrar a letra no board
    # Para cada letra da palavra oculta, retorna a letra se ela estiver na lista de letras corretas
    # Senão, retorna '_'
    def hide_word(self):
        return [x if x in self.correct else '_' for x in self.word]

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.incorrect)])
        print('\nPalavra:', *self.hide_word())
        # Printing the list using * and sep operator (separa os itens da lista por vírgula, ou outro caracter).
        # Se não colocar o sep operator, usa o default, que é o espaço
        print('\nLetras erradas:', *self.incorrect)
        print('\nPalavras corretas:', *self.correct)



# Função para ler uma palavra de forma aleatória do banco de palavras
# t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default.
# Documented here: https://docs.python.org/3/library/functions.html#open
# The default mode is 'r'(open for reading text, synonym of 'rt').
def rand_word():
    with open("Banco de palavras.txt", "rt") as f:
        bank = f.readlines()

    # A função strip() remove os espaços em branco
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Cria um objeto enviando uma palavra aleatória do arquivo de texto
    game = Hangman(rand_word())

    print('\n\n******************* Jogo da Forca *******************')

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while (not game.hangman_over()):
        game.print_game_status()
        letter = input('\nDigite uma letra: ')
        game.guess(letter[0].lower())

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\n\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()