# Text_3
import flet as ft

def main(page: ft.Page):
    page.title = "Text theme styles"
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/"
                      "RobotoSlab%5Bwght%5D.ttf"
    }

    def handle_slider_change(e):
        text.weight = f"w{int(e.control.value)}"  # noqa
        text.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    text := ft.Text(
                        "Это визуализируется шрифтом Roboto Slab",
                        size=30,
                        font_family="RobotoSlab",
                        weight=ft.FontWeight.W_100,
                    ),
                    ft.Slider(
                        min=100,
                        max=900,
                        divisions=8,
                        label="weight = {value}",
                        width=500,
                        on_change=handle_slider_change,
                    ),
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)