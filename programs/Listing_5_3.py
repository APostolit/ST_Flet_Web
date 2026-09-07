# Banner_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Banner"
    banner = ft.Banner(
        leading=ft.Icon(ft.Icons.INFO_OUTLINED, color=ft.Colors.PRIMARY),
        content=ft.Text("Резервное копирование успешно завершено."),
        actions=[ft.TextButton("Закрыть")],
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        open=True,
    )
    page.show_dialog(banner)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)