# Listing_10_17
import flet as ft
from Listing_10_15 import create_v as home_view
from Listing_10_16 import create_v as settings_view

async def main(page: ft.Page):
    # Переход на страницу настроек
    def open_set():
        # Очищаем главную страницу приложения
        page.views.clear()
        # Загружаем новое содержание
        page.views.append(settings_view())
        # Добавляем верхнюю панель
        page.appbar = appbar

    # Переход на домашнюю страницу
    def open_home():
        # Очищаем главную страницу приложения
        page.views.clear()
        # Загружаем новое содержание
        page.views.append(home_view())
        # Добавляем верхнюю панель
        page.appbar = appbar

    # Выход из программы
    async def exit_program(e):
        await page.window.close()

    # Левая кнопка для верхней панели
    app_menu = ft.PopupMenuButton(
        icon=ft.Icon(ft.Icons.MENU),  # Иконка кнопки
        items=[ft.PopupMenuItem(content="Домашняя", on_click=open_home),
               ft.PopupMenuItem(content="Настройки", on_click=open_set),
               ft.PopupMenuItem(),  # Разделительная линия
               ft.PopupMenuItem(content="Выход", on_click=exit_program),], )

    # Создаем верхнюю панель
    appbar = ft.AppBar(
        leading=app_menu,
        leading_width=40,
        title=ft.Text("Многостраничное приложение", color=ft.Colors.WHITE),
        center_title=False,
        bgcolor=ft.Colors.BLUE_300,
        actions=[ft.PopupMenuButton(key="popup",
                                    icon=ft.IconButton(ft.Icons.EXIT_TO_APP,
                                                       on_click=exit_program),),
            ],
        )

    # Очищаем главную страницу приложения
    page.views.clear()
    # Добавляем на главную страницу элементы с начальной страницы
    page.views.append(home_view())
    # Добавляем верхнюю панель
    page.appbar = appbar

if __name__ == "__main__":
    ft.run(main)