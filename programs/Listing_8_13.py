# Container_7
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер - смена темы"
    # Тема "Желтая страница" (по умолчанию)
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.YELLOW,)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    # Тема страницы
                    ft.Container(
                        bgcolor=ft.Colors.SURFACE_TINT,
                        padding=20,
                        width=300,
                        content=ft.Button("Кнопка с темой страницы"),),
                    # Унаследованная тема
                    ft.Container(
                        bgcolor=ft.Colors.SURFACE_TINT,
                        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.BLUE)),
                        padding=20,
                        width=300,
                        content=ft.Button("Унаследованная тема"),
                    ),
                    # Новая DARK тема
                    ft.Container(
                        bgcolor=ft.Colors.SURFACE_TINT,
                        theme=ft.Theme(color_scheme_seed=ft.Colors.RED),
                        theme_mode=ft.ThemeMode.DARK,
                        padding=20,
                        width=300,
                        content=ft.Button("Кнопка с темной темой"),
                    ),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)