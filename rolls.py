import random

def roll_dice(roll_quantity: int, face_count: int, advantage: int) -> str:

    """
    Simula a rolagem de dados e retorna uma string com os resultados.

    Args:
        roll_quantity: Quantidade de dados a serem rolados.
        face_count: Número de faces de cada dado.
        advantage: Um valor a ser somado ao total dos dados (modificador).

    Return:
        Uma string com os detalhes da rolagem, resultados individuais e o total.
    """

    dice_results = [random.randint(1, face_count) for n in range(roll_quantity)]
    dices_sum = sum(dice_results)

    if advantage == 0:
        texto = [f"Rolagem de {roll_quantity}d{face_count}\n\n"]
    else:
        texto = [f"Rolagem de {roll_quantity}d{face_count}+{advantage}\n\n"]

    for i, result in enumerate(dice_results):
        texto.append(f"Dado {i+1}: {result}\n")
    
    if advantage == 0:
        texto.append(f"\nTotal: {dices_sum}")
    else:
       texto.append(f"\nTotal: {dices_sum}\nTotal com vantagem: {dices_sum + advantage}")
    
    return "".join(texto)

print(roll_dice(2,6,0))
