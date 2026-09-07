# OutlinedButton_4
import flet as ft

def main(page: ft.Page):
    page.title = "OutlinedButton"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.OutlinedButton(
                        width=150,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.Icon(ft.Icons.FAX, color=ft.Colors.PINK),
                                ft.Icon(ft.Icons.ALBUM, color=ft.Colors.GREEN),
                                ft.Icon(ft.Icons.BOOK, color=ft.Colors.BLUE),],),),
                    ft.OutlinedButton(
                        content=ft.Container(
                            padding=ft.Padding.all(10),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                                controls=[ft.Text(value="Комбинированная кнопка", size=20),
                                          ft.Text(value="с дополнительным текстом"),],),
                        ),
                    ),
                ],
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)