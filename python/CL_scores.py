import os

current_dir = os.getcwd()
scores_dir = os.path.join(current_dir, '..', '..', 'scores')
scores_file = os.path.join(scores_dir, 'scores.bin')
names_file = os.path.join(scores_dir, 'names.txt')



def init():
    # Verifica se a pasta "scores" já existe, se não existir, cria
    if not os.path.exists(scores_dir):
        os.makedirs(scores_dir)

    # Verifica se o arquivo "scores.bin" existe na pasta "scores"
    if not os.path.exists(scores_file):
        # Se não existir, cria o arquivo com 1440 bits nulos
        with open(scores_file, 'wb') as file:
            file.write(b'\x00' * 180)  # 1440 bits (180 bytes)

    # Verifica se o arquivo "names.txt" existe na pasta "scores"
    if not os.path.exists(names_file):
        # Se não existir, cria o arquivo com 90 linhas vazias
        with open(names_file, 'w') as file:
            for _ in range(90):
                file.write('\n')


def readNames(path):
    with open(path, 'r') as file:
        names_list = file.readlines()

    return names_list

def readScores(path):
    """
    Lê o conteúdo de um arquivo binário e retorna uma lista
    em que cada elemento é um inteiro representando dois bytes do arquivo.

    Argumentos:
    path (str): O caminho do arquivo binário.

    Retorna:
    list: Uma lista contendo os inteiros representando os bytes do arquivo binário.
    """
    scores_list = []

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
                scores_list.append(score)
    except FileNotFoundError:
        print("O arquivo binário não foi encontrado em:", path)

    return scores_list



init()
names = readNames(names_file)
scores = readScores(scores_file)
print((scores))


