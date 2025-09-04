import pyautogui
import time
import keyboard
import pyperclip
from random import randint

# Configurações
pyautogui.PAUSE = 0.3
LARGURA_TEXTO = 80  # Número de colunas antes de quebrar linha
pyautogui.FAILSAFE = False

print("=== TEXTO HORIZONTAL ===")
print("1. Posicione no canto esquerdo")
print("2. Pressione 'Q' para iniciar")
print("3. Pressione F2 para cancelar\n")

def get_position():
    try:
        return pyautogui.position()
    except:
        return (500, 500)  # Fallback

pyperclip.copy("█")
start_x, start_y = get_position()
current_x, current_y = start_x, start_y

while True:
    if keyboard.is_pressed('q'):
        try:
            for i in range(230):
                if keyboard.is_pressed('F2'):
                    raise Exception("Cancelado")
                
                # Colagem com micro-ajustes
                pyautogui.click(
                    current_x + randint(0, 1),
                    clicks=2
                )
                pyautogui.hotkey('ctrl', 'v')
                
                # Avança para direita e gerencia quebras de linha
                current_x += 10  # Incremento horizontal
                if (i+1) % LARGURA_TEXTO == 0:
                    current_x = start_x
                    current_y += 15  # Quebra linha
                    pyautogui.scroll(-20)
                
                print(f" {i+1}/230 | Pos: ({current_x},{current_y})", end='\r')
                time.sleep(0.1)
                
        except Exception as e:
            print(f"\nInterrompido: {str(e)}")
            break
            
        print("\nConcluído!")
        break

    time.sleep(0.01)