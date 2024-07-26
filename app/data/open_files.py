import os
import json

from app.data import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.CURED_ANIMAL):
    with open(list_files.CURED_ANIMAL, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_animals(path: str = list_files.ANIMALS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals


def get_animal(anim_index: int) -> str:
    animals = get_animals()
    return animals[anim_index]


def get_cured_animal(path: str = list_files.CURED_ANIMAL) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        cured_animal = json.load(file)

    return cured_animal


def get_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
