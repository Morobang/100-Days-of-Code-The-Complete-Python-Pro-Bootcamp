# Day 010 — *args, **kwargs & Returns — REFERENCE SOLUTION

def total(*args) -> float:
    # sum() works on any iterable; default=0 handles empty args
    return sum(args)


def describe(**kwargs) -> str:
    # Sort by key for deterministic output
    return " ".join(f"{k}={v}" for k, v in sorted(kwargs.items()))


def flexible(required, *args, **kwargs) -> dict:
    return {
        "required": required,
        "extras": list(args),
        "options": kwargs,
    }


def bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in metres.

    Returns:
        BMI rounded to 1 decimal place.
    """
    return round(weight_kg / height_m ** 2, 1)
