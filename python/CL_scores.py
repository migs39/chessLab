import os

currentDir = os.getcwd()
path = os.path.join(currentDir, 'scores')
scoresFile = os.path.join(path, 'scores.bin')
namesFile = os.path.join(path, 'names.txt')



def init():
    # Verifica se a pasta "scores" já existe, se não existir, cria
    if not os.path.exists(path):
        os.makedirs(path)

    # Verifica se o arquivo "scores.bin" existe na pasta "scores"
    if not os.path.exists(scoresFile):
        # Se não existir, cria o arquivo com 1440 bits nulos
        with open(scoresFile, 'wb') as file:
            file.write(b'\x00' * 180)  # 1440 bits (180 bytes)

    # Verifica se o arquivo "names.txt" existe na pasta "scores"
    if not os.path.exists(namesFile):
        # Se não existir, cria o arquivo com 90 linhas vazias
        with open(namesFile, 'w') as file:
            for _ in range(90):
                file.write('\n')


def readNames(path):
    with open(path, 'r') as file:
        # Lê as linhas do arquivo e remove o caractere de nova linha (\n) de cada linha
        namesList = [line.rstrip('\n') for line in file.readlines()]

    return namesList

def readScores(path):
    """
    Lê o conteúdo de um arquivo binário e retorna uma lista
    em que cada elemento é um inteiro representando dois bytes do arquivo.

    Argumentos:
    path (str): O caminho do arquivo binário.

    Retorna:
    list: Uma lista contendo os inteiros representando os bytes do arquivo binário.
    """
    scoresList = []

    try:
        with open(path, 'rb') as file:
            # Lê os bytes do arquivo em pares e converte para inteiro
            while True:
                # Lê dois bytes do arquivo
                bytes_read = file.read(2)
                # Se não houver mais bytes para ler, encerra o loop
                if not bytes_read:
                    break
                # Converte os bytes para um inteiro e adiciona à lista
                score = int.from_bytes(bytes_read, byteorder='big')
                scoresList.append(score)
    except FileNotFoundError:
        print("O arquivo binário não foi encontrado em:", path)

    return scoresList

def writeNames(path, namesList):
    """
    Escreve a lista de nomes em um arquivo de texto.

    Argumentos:
    path (str): O caminho do arquivo de texto.
    namesList (list): A lista de nomes a ser escrita no arquivo.
    """
    with open(path, 'w') as file:
        for name in namesList:
            file.write(name + '\n')


def writeScores(path, scoresList):
    """
    Escreve a lista de pontuações em um arquivo binário.

    Argumentos:
    path (str): O caminho do arquivo binário.
    scoresList (list): A lista de pontuações a ser escrita no arquivo.
    """
    with open(path, 'wb') as file:
        for score in scoresList:
            # Converte o número em dois bytes e escreve no arquivo binário
            file.write(score.to_bytes(2, byteorder='big'))

def getHighscores(mode, time, decrease, scoresFile, namesFile):
    '''
    mode: 0 para clicar, 1 para escrever
    time: 0 para 15 s, 1 para 30 s e 2 para 45 s
    decrease: 0, 1 e 2
    '''
    n = 9*mode + 3*time + decrease
    Names = readNames(namesFile)[5*n:5*n+5]
    Scores = readScores(scoresFile)[5*n:5*n+5]
    return (Names, Scores)

def isHighscore(mode, time, decrease, scoresFile, namesFile, score):
    return score > getHighscores(mode, time, decrease, scoresFile, namesFile)[1][4]

def registerScore(mode, time, decrease, scoresFile, namesFile, score, name):
    highscores = getHighscores(mode, time, decrease, scoresFile, namesFile)
    for i in range(5):
        if score > highscores[1][i]:
            highscores[0].insert(i, name)
            highscores[0].pop()
            highscores[1].insert(i, score)
            highscores[1].pop()
            break
    n = 9*mode + 3*time + decrease
    names = readNames(namesFile)
    names[5*n:5*n+5] = highscores[0]
    scores = readScores(scoresFile)
    scores[5*n:5*n+5] = highscores[1]
    writeNames(namesFile, names)
    writeScores(scoresFile, scores)

def clear(path):
    # Clear the contents of the names.txt file
    namesPath = os.path.join(path, 'names.txt')
    with open(namesPath, 'w') as file:
        for _ in range(90):
            file.write('\n')
    
    # Clear the contents of the scores.bin file
    scoresPath = os.path.join(path, 'scores.bin')
    with open(scoresPath, 'wb') as file:
        file.write(b'\x00' * 180)  # 1440 bits (180 bytes)


init()
def test():
    #clear(path)
    registerScore(0, 0, 1, scoresFile, namesFile, 6, 'migs2')
    print((readScores(scoresFile)))
    print(getHighscores(0, 0, 1, scoresFile, namesFile))

if __name__ == '__main__':
    test()