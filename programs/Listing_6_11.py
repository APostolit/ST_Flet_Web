# AppBar_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "Панель AppBar"

    def handle_checked_item_click(e: ft.Event[ft.PopupMenuItem]):
        e.control.checked = not e.control.checked

    def click(e: ft.Event[ft.PopupMenuItem]):
        action = e.control.content
        page.show_dialog(ft.SnackBar(content=f"Выбрана опция: '{action}'"))

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("Панель AppBar"),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_400,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                key="popup",
                items=[
                    ft.PopupMenuItem(content="Элемент 1", on_click=click),
                    ft.PopupMenuItem(content="Элемент 2", on_click=click),
                    ft.PopupMenuItem(content="Элемент 3", on_click=click),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        content="Выбор элемента",
                        checked=False,
                        on_click=handle_checked_item_click,
                    ),
                ],
            ),
        ],
    )
    page.add(ft.SafeArea(content=ft.Column(
        controls=[ft.Text("Основное окно приложения!")])))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)