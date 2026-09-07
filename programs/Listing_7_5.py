# CupertinoActivityIndicator_1
import flet as ft

def main(page: ft.Page):
    page.title = "Индикатор активности CupertinoActivityIndicator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=ft.CupertinoActivityIndicator(
                animating=True,
                color=ft.Colors.RED,
                radius=50,
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)