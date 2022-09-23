# import pygame
from fileinput import close
import time
import gtts
from playsound import playsound

with open('frase.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')
        time.sleep(2)
        playsound('frase.mp3')
    

# pygame.init()
# windowsSize = pygame.display.set_mode((800,600)) 

# for variavel in range(10):
#     pygame.mixer.music.load('notas/fa-stretched.wav')
#     time.sleep(2)
#     pygame.mixer.music.play()
#     pygame.event.wait()


# for variavel in range(10):
#     pygame.mixer.music.load('notas/mi-stretched.wav')
#     time.sleep(2)
#     pygame.mixer.music.play()
#     pygame.event.wait()
