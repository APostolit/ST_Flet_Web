# Canvas_1.py
import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    page.title = "Холст"
    c = cv.Canvas(
        width=160,
        height=160,
        shapes=[
            cv.Rect(0, 0, 160, 160,
                paint=ft.Paint(
                    color=ft.Colors.BLUE_100,
                    style=ft.PaintingStyle.FILL,
                ),
            ),
            cv.Circle(80, 80, 50,
                paint=ft.Paint(
                    color=ft.Colors.BLUE_400,
                    style=ft.PaintingStyle.FILL,
                ),
            ),
        ],
    )
    page.add(c)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)