# MenuItemButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопки меню"
    d = ft.Row(
        controls=[
            ft.MenuItemButton(
                content=ft.Text("Опция 1"),
                on_click=lambda e: print("Опция 1"),),
            ft.MenuItemButton(
                content=ft.Text("Опция 2"),
                on_click=lambda e: print("Опция 2"),),
            ft.MenuItemButton(
                content=ft.Text("Опция 3"),
                on_click=lambda e: print("Опция 3"),),
        ],
    )
    page.add(d)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)