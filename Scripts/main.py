import pygame
import settings

pygame.init()

screen = pygame.display.set_mode([settings.Weight, settings.Height])
pygame.display.set_caption(settings.caption)

pygame.quit()