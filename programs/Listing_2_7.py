# Canvas_6.py
import math
import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    page.title = "Текст"
    page.add(
        ft.SafeArea(
            content=cv.Canvas(
                width=float("inf"),
                expand=True,
                shapes=[
                    cv.Text(x=0, y=0, value="Обычный текст"),
                    cv.Circle(
                        x=200, y=100, radius=2, paint=ft.Paint(color=ft.Colors.RED)
                    ),
                    cv.Text(
                        x=200,
                        y=100,
                        style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=30),
                        alignment=ft.Alignment.TOP_CENTER,
                        rotate=math.pi * 0.15,
                        value="Поворот",
                        spans=[
                            ft.TextSpan(
                                text="вокруг верхнего центра",
                                style=ft.TextStyle(
                                    italic=True, color=ft.Colors.GREEN, size=20
                                ),
                            )
                        ],
                    ),
                    cv.Circle(
                        x=400, y=100, radius=2, paint=ft.Paint(color=ft.Colors.RED)
                    ),
                    cv.Text(
                        x=400,
                        y=100,
                        value="Поворот вокруг левого угла",
                        style=ft.TextStyle(size=20),
                        alignment=ft.Alignment.TOP_LEFT,
                        rotate=math.pi * -0.15,
                    ),
                    cv.Circle(
                        x=600, y=200, radius=2, paint=ft.Paint(color=ft.Colors.RED)
                    ),
                    cv.Text(
                        x=600,
                        y=200,
                        value="Поворот вокруг центра",
                        style=ft.TextStyle(size=20),
                        alignment=ft.Alignment.CENTER,
                        rotate=math.pi / 2,
                    ),
                    cv.Text(
                        x=300,
                        y=400,
                        value=(
                            "Ограничено значением max_width и выровнено по левому краю.\n"
                            "Приветствуем ваше стремление изучать Python. "
                            "Эти знания очень пригодятся в вашей будущей профессии. "
                            "Вы сможете получить работу, которая вам принесет не только"
                            "материальное благополучие, но и моральное удовлетворение. "
                            "Успехов вам в преодолении возможных трудностей на этом пути!"
                        ),
                        text_align=ft.TextAlign.LEFT,
                        max_width=500,
                    ),
                    cv.Text(
                        x=200,
                        y=200,
                        value="Привет!",
                        style=ft.TextStyle(
                            weight=ft.FontWeight.BOLD,
                            size=100,
                            foreground=ft.Paint(
                                color=ft.Colors.PINK,
                                stroke_width=6,
                                style=ft.PaintingStyle.STROKE,
                                stroke_join=ft.StrokeJoin.ROUND,
                                stroke_cap=ft.StrokeCap.ROUND,
                            ),
                        ),
                    ),
                    cv.Text(
                        x=200,
                        y=200,
                        value="Привет!",
                        style=ft.TextStyle(
                            weight=ft.FontWeight.BOLD,
                            size=100,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=(200, 200),
                                    end=(300, 300),
                                    colors=[ft.Colors.YELLOW, ft.Colors.RED],
                                ),
                                stroke_join=ft.StrokeJoin.ROUND,
                                stroke_cap=ft.StrokeCap.ROUND,
                            ),
                        ),
                    ),
                ],
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)