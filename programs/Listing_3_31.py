# TextButton_4
import flet as ft

def main(page: ft.Page):
    page.title = "TextButtons с контентом"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        width=150,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.Icon(ft.Icons.MOVIE, color=ft.Colors.PINK),
                                ft.Icon(ft.Icons.CHAT, color=ft.Colors.GREEN),
                                ft.Icon(ft.Icons.REPORT, color=ft.Colors.BLUE),
                            ],
                        ),
                    ),
                    ft.TextButton(
                        content=ft.Container(
                            padding=ft.Padding.all(10),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Text(value="Текстовая кнопка", size=20),
                                    ft.Text(value="Это вторая строка кнопки"),
                                ],
                            ),
                        ),
                    ),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)