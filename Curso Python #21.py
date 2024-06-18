import pygame
pygame.init()
file1 = open("E:\\Backup\\Desktop\\244650023_263457539005560_6438936383667695999_n.mp4", "r")
pygame.mixer.music.load(file1)
pygame.mixer.music.play()
pygame.event.wait()
