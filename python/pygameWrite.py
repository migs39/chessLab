import pygame
import sys

def receive_input(font):
    # Inicializando o Pygame
    pygame.init()

    # Definindo as cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Definindo as configurações da janela
    WIDTH, HEIGHT = 400, 300
    WINDOW_SIZE = (WIDTH, HEIGHT)
    WINDOW_CENTER = (WIDTH // 2, HEIGHT // 2)

    # Configurando a janela
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Recebendo Entrada do Teclado")

    # Texto para mostrar os caracteres digitados
    typed_text = ""

    # Loop principal
    running = True
    while running:
        # Loop principal
        running = True
        while running:
            # Lidando com eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        # Apaga o último caractere digitado
                        typed_text = typed_text[:-1]
                    elif len(typed_text) == 0 and event.key >= pygame.K_a and event.key <= pygame.K_h56:
                        # Verifica se o primeiro caractere é uma letra do alfabeto
                        typed_text += chr(event.key).lower()
                    elif len(typed_text) == 1 and event.key >= pygame.K_1 and event.key <= pygame.K_8:
                        # Verifica se o segundo caractere é um número de 1 a 8
                        typed_text += chr(event.key)
                    elif event.key == pygame.K_RETURN and len(typed_text) == 2:
                        # Se a tecla Enter for pressionada e o texto tiver dois caracteres, retorna a string
                        input_string = typed_text
                        typed_text = ""  # Limpa o texto digitado para a próxima entrada
                        return input_string

            # Limpando a tela
            screen.fill(WHITE)

            # Desenhando o texto na tela
            text_surface = font.render("Texto digitado: " + typed_text, True, BLACK)
            text_rect = text_surface.get_rect(center=WINDOW_CENTER)
            screen.blit(text_surface, text_rect)

            # Atualizando a tela
            pygame.display.flip()

        # Encerrando o Pygame
        pygame.quit()
        sys.exit()



# Exemplo de uso
pygame.font.init()  # Inicializa o módulo de fontes do Pygame
font = pygame.font.Font(None, 36)  # Define a fonte a ser usada

# Chama a função para receber entrada do usuário
typed_string = receive_input(font)
print("String digitada:", typed_string)
