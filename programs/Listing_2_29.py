# Text_6
import flet as ft

def main(page: ft.Page):
    page.title = "Text theme styles"
    page.add(
        ft.SafeArea(
            content=ft.Text(
                spans=[
                    ft.TextSpan(
                        text="Приложения на Python!",
                        style=ft.TextStyle(
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=(0, 100),
                                    end=(100, 180),
                                    colors=[ft.Colors.RED, ft.Colors.BLUE_800],
                                )
                            ),
                        ),
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)