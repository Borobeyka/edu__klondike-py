import pygame
import json

with open("config.json", encoding="utf-8") as file:
    config = json.loads(file.read())

window = pygame.display.set_mode((config["app"]["width"], config["app"]["height"]))