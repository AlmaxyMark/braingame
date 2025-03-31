#!/usr/bin/env python
# pylint: disable=unused-argument
# Эта программа посвящена общественному достоянию по лицензии CC0.

"""
Простой пример Telegram WebApp, который отображает выбор цвета.
Статический веб-сайт для этого сайта размещен командой PTB для вашего удобства.
В настоящее время демонстрирует только запуск WebApp через кнопку клавиатуры, так как все другие методы требуют токен бота.
"""
import json
import logging

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Включить ведение журнала
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Установить более высокий уровень ведения журнала для httpx, чтобы избежать записи всех GET и POST запросов
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Определить обработчик команды `/start`.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправить сообщение с кнопкой, которая открывает веб-приложение."""
    await update.message.reply_text(
        "Пожалуйста, нажмите кнопку ниже, чтобы выбрать цвет через WebApp.",
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="Открыть выбор цвета!",
                web_app=WebAppInfo(url="https://mitover.github.io/hangmantest/"),
            )
        ),
    )
#https://mitover.github.io/hangmantest/
#https://python-telegram-bot.org/static/webappbot

# Обработать входящие WebAppData
async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Вывести полученные данные и удалить кнопку."""
    # Здесь мы используем `json.loads`, так как WebApp отправляет данные в виде сериализованной строки JSON
    # (см. webappbot.html)
    data = json.loads(update.effective_message.web_app_data.data)
    print(data)
    await update.message.reply_html(
        text=(
            f"Вы выбрали цвет с HEX значением {data['word']} Соответствующее "
        ),
        reply_markup=ReplyKeyboardRemove(),
    )
#     f"Вы выбрали цвет с HEX значением <code>{data['hex']}</code>. Соответствующее "
#     f"RGB значение <code>{tuple(data['rgb'].values())}</code>."
# ),

def main() -> None:
    """Запустить бота."""
    # Создать приложение и передать токен вашего бота.
    application = Application.builder().token("7914557615:AAF5d_uVUWaNWG7Fjz0l3nVdkBUo-P085iU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    # Запустить бота до тех пор, пока пользователь не нажмет Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    print("start")
    main()