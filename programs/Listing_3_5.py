# Button_5.py
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопки"

    bt_1 = ft.Button(
        width=150,
        content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,
                       controls=[ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK),
                                 ft.Icon(ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN),
                                 ft.Icon(ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE),],
                       ),
                    )
    bt_2 = ft.Button(
        content=ft.Container(
            padding=ft.Padding.all(10),
            content=ft.Column(alignment=ft.MainAxisAlignment.CENTER,
                              spacing=5,
                              controls=[ft.Text(value="Составная кнопка", size=20),
                                        ft.Text(value="Это вторая строка кнопки"),],),
                        ),
                    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[bt_1, bt_2])
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)