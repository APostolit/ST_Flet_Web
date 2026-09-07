# Card_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Карточки"
    c = ft.Card(
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        content=ft.Container(
            width=400,
            padding=10,
            content=ft.ListTile(
                bgcolor=ft.Colors.GREY_400,
                leading=ft.Icon(ft.Icons.FOREST),
                title=ft.Text("Заголовок карточки"),
            ),
        ),
    )
    page.add(c)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)