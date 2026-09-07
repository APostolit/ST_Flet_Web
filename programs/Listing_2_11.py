# Card_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "Карточка"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.Card(
                shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                content=ft.Container(
                    width=400,
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                bgcolor=ft.Colors.BLUE_200,
                                leading=ft.Icon(ft.Icons.ALBUM),
                                title=ft.Text("Заголовок карточки"),
                                subtitle=ft.Text(
                                    "Содержимое карточки"
                                ),
                            ),
                            ft.Image('images/win_c.png'),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                controls=[
                                    ft.TextButton("Кнопка 1"),
                                    ft.TextButton("Кнопка 2"),
                                ],
                            ),
                        ]
                    ),
                ),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)