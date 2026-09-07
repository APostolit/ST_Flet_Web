# BottomSheet_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "Нижний лист"
    sheet = ft.BottomSheet(
        content=ft.Column(
            width=300,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ft.Text("Выберите опцию"),
                      ft.TextButton("Выйти"),],
            )
        )
    page.show_dialog(sheet)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)