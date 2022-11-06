import random
from string import (
    digits,
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
)
from fastapi import APIRouter

router = APIRouter()


@router.get("/randomString")
async def read_root(
        include_ascii_lowercase: bool = True,
        include_ascii_uppercase: bool = True,
        include_digits: bool = True,
        enable_punctuation: bool = True,
        min_length: int = 8,
        max_length: int = 16,
):
    population = []
    if include_digits:
        population += digits
    if include_ascii_lowercase:
        population += ascii_lowercase
    if include_ascii_uppercase:
        population += ascii_uppercase
    if enable_punctuation:
        population += punctuation
    repeat = max(round(max_length / len(punctuation)), 1)
    population = repeat * population
    return "".join(
        random.sample(
            population=population,
            k=random.randint(min_length, max_length)
        )
    )

