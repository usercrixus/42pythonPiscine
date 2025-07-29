def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    "calc the bmi"
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    "used to say if the bmi is superior to a certain value"
    return [x > limit for x in bmi]
