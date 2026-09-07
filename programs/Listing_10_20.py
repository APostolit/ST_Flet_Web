# Listing_10_20
import flet as ft
from Listing_10_18 import create_col as home_page
from Listing_10_19 import create_col as set_page

async def main(page: ft.Page):
    # Переход на домашнюю страницу
    def open_home():
        # Создаем главный контейнер
        main_container = ft.Container(
            content=ft.Column(controls=[appbar, home_page()]),
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_100,  # фон
            expand=True)
        # Добавляем основной контейнер в защищенную область
        sa = ft.SafeArea(expand=True, content=main_container)
        # Очищаем главную страницу приложения
        page.controls.clear()
        # Загружаем новое содержание
        page.controls.append(sa)

    # Переход на страницу настроек
    def open_set():
        # Создаем главный контейнер
        main_container = ft.Container(
            content=ft.Column(controls=[appbar, set_page()]),
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_100,  #  фон
            expand=True)
        # Добавляем основной контейнер в защищенную область
        sa = ft.SafeArea(expand=True, content=main_container)
        # Очищаем главную страницу приложения
        page.controls.clear()
        # Загружаем новое содержание
        page.add(sa)

    # Выход из программы
    async def exit_program(e):
        await page.window.close()

    # Левая кнопка для верхней панели
    app_menu = ft.PopupMenuButton(
        icon=ft.Icon(ft.Icons.MENU),  # Иконка кнопки
        items=[
            ft.PopupMenuItem(content="Домашняя", on_click=open_home),
            ft.PopupMenuItem(content="Настройки", on_click=open_set),
            ft.PopupMenuItem(),  # Разделительная линия
            ft.PopupMenuItem(content="Выход", on_click=exit_program),
        ],
    )

    # Верхняя панель
    appbar = ft.AppBar(
        leading=app_menu,
        title=ft.Text("Верхняя панель", color=ft.Colors.WHITE),
        center_title=True,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_400,
        actions=[
            ft.PopupMenuButton(key="popup",
                               icon=ft.IconButton(ft.Icons.EXIT_TO_APP,
                                                  on_click=exit_program),),
            ],
        )

    # Загружаем главную страницу
    open_home()

if __name__ == "__main__":
    ft.run(main)