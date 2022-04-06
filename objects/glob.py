import pygame
import time
import json

with open("config.json", encoding="utf-8") as file:
    config = json.loads(file.read())

def load_sound(path):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(config["app"]["volume"])
    return sound

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((config["app"]["width"], config["app"]["height"]))
card_nominal = pygame.font.SysFont("ebrima", config["card"]["icon"]["fontSize"], True)
cards_icon = {
    "clover": pygame.image.load("./assets/icons/clover.png"),
    "diamond": pygame.image.load("./assets/icons/diamond.png"),
    "heart": pygame.image.load("./assets/icons/heart.png"),
    "spade": pygame.image.load("./assets/icons/spade.png"),
}
sounds = {
    "background_music": pygame.mixer.music.load("./assets/sounds/background_music.mp3"),
    "deck_open": load_sound("./assets/sounds/deck_open.wav"),
    "stack_card_open": load_sound("./assets/sounds/stack_card_open.wav"),
    "stack_release": load_sound("./assets/sounds/stack_release.wav"),
    "stack_take": load_sound("./assets/sounds/stack_take.wav"),
    "storage": load_sound("./assets/sounds/storage.wav")
}
cards = []
stacks = []
storages = []
deck = None
game_loop = True
dragged_heap = None
dragged_stack = None
time_started = time.time()