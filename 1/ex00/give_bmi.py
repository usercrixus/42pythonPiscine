def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [x > limit for x in bmi]