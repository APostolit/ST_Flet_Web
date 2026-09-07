# Text_1
import flet as ft

def main(page: ft.Page):
    page.title = "Text пользовательские стили"
    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(
        ft.SafeArea(
            content=ft.Column(
                adaptive=True,
                controls=[
                    ft.Text("Size 10", size=10),
                    ft.Text(
                        "Size 30, Italic",
                        size=30,
                        color=ft.Colors.PINK_600,
                        italic=True,
                    ),
                    ft.Text(
                        value="Size 40, w100",
                        size=40,
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.BLUE_600,
                        weight=ft.FontWeight.W_100,
                    ),
                    ft.Text(
                        value="Size 50, Normal",
                        size=50,
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.ORANGE_800,
                        weight=ft.FontWeight.NORMAL,
                    ),
                    ft.Text(
                        value="Size 60, Bold, Italic",
                        size=50,
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.GREEN_700,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                    ),
                    ft.Text(
                        value="Size 70, w900, selectable",
                        size=70,
                        weight=ft.FontWeight.W_900,
                        selectable=True,
                    ),
                    ft.Text(
                        value="Ограничение длины текста 1 строкой с многоточием",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                    ),
                    ft.Text(
                        value=(
                            "Длинный текст, состоящий из нескольких строк."
                            "Здесь несколько предложений, которые разнесены "
                            "по разным строкам."
                            "Здесь несколько предложений, которые разнесены "
                            "по разным строкам."
                        ),
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    ft.Text(
                        value="Ограничение длины текста до 2 строк и затемнение",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                    ),
                    ft.Text(
                        value=(
                            "Длинный текст, состоящий из нескольких строк и затемнение."
                            "Здесь несколько предложений, которые разнесены "
                            "по разным строкам и затемнение."
                            "Здесь несколько предложений, которые разнесены "
                            "по разным строкам и затемнение."
                        ),
                        max_lines=2,
                    ),
                    ft.Text(
                        value="Ограничение ширины и высоты длинного текста",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                    ),
                    ft.Text(
                        value=(
                            "Это длинный текст с ограничением по ширине и высоте."
                            "Это длинный текст с ограничением по ширине и высоте."
                            "Это длинный текст с ограничением по ширине и высоте."
                            "Это длинный текст с ограничением по ширине и высоте."
                            "Это длинный текст с ограничением по ширине и высоте."
                        ),
                        width=300,
                        height=100,
                    ),
                ],
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)