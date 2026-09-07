# Stack_2
import flet as ft

def main(page: ft.Page):
    page.title = "Stack"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ct_1 = ft.Container(width=20, height=20, bgcolor=ft.Colors.RED,
                        border_radius=5,)
    ct_2 = ft.Container(width=20, height=20, bgcolor=ft.Colors.YELLOW,
                        border_radius=5, right=0,)
    ct_3 = ft.Container(width=20, height=20, bgcolor=ft.Colors.BLUE,
                        border_radius=5, right=0, bottom=0,)
    ct_4 = ft.Container(width=20, height=20, bgcolor=ft.Colors.GREEN,
                        border_radius=5, left=0, bottom=0,)
    col = ft.Column(left=85, top=85,
                    controls=[ft.Container(width=20, height=20,
                                           bgcolor=ft.Colors.PURPLE,
                                           border_radius=5,)],
                    )
    page.add(
        ft.SafeArea(
            content=ft.Container(
                border_radius=8,
                padding=5,
                width=200,
                height=200,
                bgcolor=ft.Colors.BLACK,
                content=ft.Stack(
                    controls=[ct_1, ct_2, ct_3, ct_4, col,]
                    ),
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)