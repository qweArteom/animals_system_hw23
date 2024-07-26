import json

from app.data import list_files, open_files


def add_review(review: str) -> str:
    reviews = open_files.get_reviews()
    reviews.append(review)

    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump(reviews, file)

    msg = f"Відгук '{review}' успішно додано."
    return msg