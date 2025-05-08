import random

def roll_dice(roll_quantity: int, face_count: int, advantage: int):

    dice_results = []
    if advantage == 0:
        texto = f"Rolagem de {roll_quantity}d{face_count}\n"
    else:
        texto = f"Rolagem de {roll_quantity}d{face_count}+{advantage}\n"

    for i in range( roll_quantity):
        dice_results.append(random.randint(1, face_count))

    for i, result in enumerate(dice_results):
        texto += f"Dado {i+1}: {result}\n"
    
    if advantage == 0:
        texto += f"Total: {sum(dice_results)}"
    else:
       texto += f"Total: {sum(dice_results)}\nTotal com vantagem: {sum(dice_results) + advantage}" 
    
    return texto



