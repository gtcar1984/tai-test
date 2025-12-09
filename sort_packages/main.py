def sort(width, height, length, mass) -> str:
    volume = width * height * length
    bulky = False
    heavy = False
    if (volume > 1000000) or (width >= 150) or (height >= 150) or (length >= 150):
        bulky = True
    if mass >= 20:
        heavy = True
    if bulky and heavy:
        return "Rejected"
    elif bulky or heavy:
        return "Special"
    else:
        return "Standard"
