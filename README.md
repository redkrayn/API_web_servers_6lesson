# Загрузка xckd комиксов в тг

Этот проект позволяет загружать рандомные комиксы в вашу группу тг.

## Как установить

 - Python 3.7 или выше: Убедитесь, что у вас установлен Python. Вы можете скачать его с официального сайта.
 
### 1. Скачайте код
 - Перейдите на страницу репозитория проекта.
 - Нажмите на кнопку "Code" и выберите "Download ZIP".
 
 ### 2. Настройка переменных окружения
Создайте файл .env в корневой директории проекта и добавьте в него следующие переменные:
```
TELEGRAM_BOT_TOKEN="ваш_токен_бота"
TELEGRAM_CHAT_ID="@название_группы_в_тг"
```
 
### 3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 2. Запустите скрипт:
 - Запустите скрипт командой:
```bash
python main.py
```

### Пример работы бота:
 ![](https://cdn.picloud.cc/25db5451b4c8b483ca7377a28c59564c.png)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.