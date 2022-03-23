import pygame
import json

with open("config.json", encoding="utf-8") as file:
    config = json.loads(file.read())

pygame.font.init()
window = pygame.display.set_mode((config["app"]["width"], config["app"]["height"]))

card_nominal = pygame.font.SysFont("ebrima", config["card"]["icon"]["fontSize"], True)

cards_icon = {
    "clover": pygame.image.load("./assets/clover.png"),
    "diamond": pygame.image.load("./assets/diamond.png"),
    "heart": pygame.image.load("./assets/heart.png"),
    "spade": pygame.image.load("./assets/spade.png"),
}
cards = []