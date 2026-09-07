# Page_1
import flet as ft

def main(page: ft.Page):
    page.title = "Page"
    page.window.width = 300
    page.window.height = 200
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Главное окно приложения!"),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)