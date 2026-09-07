# Container_9
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер - темы"
    page.theme_mode = ft.ThemeMode.DARK

    def handle_switch_change(e: ft.Event[ft.Switch]):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            switch.thumb_icon = ft.Icons.LIGHT_MODE
        else:
            switch.thumb_icon = ft.Icons.DARK_MODE
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    # Тема "Желтая страница" (по умолчанию)
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.YELLOW)

    switch = ft.Switch(thumb_icon=ft.Icons.DARK_MODE, on_change=handle_switch_change)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    # Тема страницы (по умолчанию)
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                bgcolor=ft.Colors.SURFACE_TINT,
                                padding=20,
                                width=300,
                                content=ft.Button("Кнопка в текущей теме"),),
                            ft.Container(
                                padding=ft.Padding.only(bottom=50),
                                alignment=ft.Alignment.TOP_RIGHT,
                                content=switch,),],),
                    # Унаследованная тема с переопределенным основным цветом
                    ft.Container(
                        theme=ft.Theme(
                            color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
                        bgcolor=ft.Colors.SURFACE_TINT,
                        padding=20,
                        width=300,
                        content=ft.Button("Унаследованная тема"),),
                    # Заданная всегда ТЕМНАЯ тема
                    ft.Container(
                        theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
                        theme_mode=ft.ThemeMode.DARK,
                        bgcolor=ft.Colors.SURFACE_TINT,
                        padding=20,
                        width=300,
                        content=ft.Button("Новая тема"),),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)