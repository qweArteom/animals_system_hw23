import json

from app.data import list_files, open_files


def remove_animal(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animal, file)

    msg = f"Тварину '{animal}' успішно видалено."
    return msg


def cured_animals(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    cured_animals = open_files.get_cured_animal()
    cured_animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.CURED_ANIMAL, "w", encoding="utf-8") as file:
        json.dump(cured_animals, file)

    msg = f"Тварину '{animal}' успішно вилікувано. Дякую за співпрацю."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тварина '{animal}' вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тварину '{animal}' успішно додано."
    return msg