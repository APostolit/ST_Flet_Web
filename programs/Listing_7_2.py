# Badge_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "Badge"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icon(
                    ft.Icons.EXPLORE,
                    badge=ft.Badge(small_size=10),
                ),
                label="Посмотреть где!",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(
                    ft.Icons.COMMUTE,
                    badge=ft.Badge(label='M'),
                ),
                label="Как доехать!",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(ft.Icons.PHONE,
                              badge="Контакты",
                ),
                label="Как позвонить!"
            ),
        ]
    )

    page.add(ft.SafeArea(content=ft.Column(
        controls=[ft.Text("Главное окно!")])))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)