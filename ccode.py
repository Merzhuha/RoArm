import serial
import keyboard
import json
import time

# Подключение к роботу
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Исходные значения — крупные, как в твоём примере
positions = {
    "T": 1041,  # суставы выключены
    "x": 235,   # начальная позиция по оси X
    "y": 0,     # начальная позиция по оси Y
    "z": 234,   # начальная позиция по оси Z
    "t": 0.0    # степень сжатия клешни (открыта)
}

STEP = 5  # шаг перемещения, можно уменьшить или увеличить

def send_command():
    cmd = json.dumps(positions) + "\n"
    ser.write(cmd.encode())
    print(f"→ {cmd.strip()}")

print("Управление RoArm-M2-S:")
print("  w/s - вперёд / назад (x)")
print("  a/d - влево / вправо (y)")
print("  q/e - вверх / вниз (z)")
print("  r/f - увеличить / уменьшить степень сжатия клешни (t)")
print("  z   - активация / деактивация суставов (T)")
print("  x   - выход")

try:
    while True:
        if keyboard.is_pressed('w'):
            positions["x"] += STEP
            send_command()
            time.sleep(0.1)
        elif keyboard.is_pressed('s'):
            positions["x"] -= STEP
            send_command()
            time.sleep(0.1)

        elif keyboard.is_pressed('a'):
            positions["y"] -= STEP
            send_command()
            time.sleep(0.1)
        elif keyboard.is_pressed('d'):
            positions["y"] += STEP
            send_command()
            time.sleep(0.1)

        elif keyboard.is_pressed('q'):
            positions["z"] += STEP
            send_command()
            time.sleep(0.1)
        elif keyboard.is_pressed('e'):
            positions["z"] -= STEP
            send_command()
            time.sleep(0.1)

        elif keyboard.is_pressed('r'):  # Увеличение сжатия клешни
            positions["t"] = min(3.14, positions["t"] + 0.1)  # Максимальное сжатие клешни
            send_command()
            time.sleep(0.1)
        elif keyboard.is_pressed('f'):  # Уменьшение сжатия клешни
            positions["t"] = max(0.0, positions["t"] - 0.1)  # Минимальное сжатие клешни
            send_command()
            time.sleep(0.1)

        elif keyboard.is_pressed('z'):  # Активация/деактивация суставов
            positions["T"] = 1042 if positions["T"] == 1041 else 1041
            send_command()
            time.sleep(0.2)

        elif keyboard.is_pressed('x'):
            print("Выход.")
            break

except KeyboardInterrupt:
    pass
finally:
    ser.close()
