# AppBar_3.py
import flet as ft

LIGHT_SEED_COLOR = ft.Colors.DEEP_ORANGE
DARK_SEED_COLOR = ft.Colors.DEEP_PURPLE

def main(page: ft.Page):
    page.title = "Пример смены темы приложения"

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=LIGHT_SEED_COLOR)
    page.dark_theme = ft.Theme(color_scheme_seed=DARK_SEED_COLOR)

    def toggle_theme_mode(e: ft.Event[ft.IconButton]):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT)
        theme_mode_toggle.icon = (
            ft.Icons.WB_SUNNY_OUTLINED
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.WB_SUNNY)

    theme_mode_toggle = ft.IconButton(
        key="theme_mode_toggle",
        icon=(ft.Icons.WB_SUNNY_OUTLINED
        if page.theme_mode == ft.ThemeMode.LIGHT
        else ft.Icons.WB_SUNNY),
        on_click=toggle_theme_mode,)

    page.padding = 50
    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.SECONDARY_CONTAINER,
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("Панель AppBar"),
        center_title=False,
        actions=[theme_mode_toggle,],)
    txt = ("Flet - это фреймворк, который позволяет создавать веб, десктопные "
           "и мобильные приложения на Python без опыта в разработке интерфейсов."
           "Вы можете создать пользовательский интерфейс для своей программы "
           "с помощью элементов управления Flet, которые основаны на Flutter от Google."
           "Flet выходит за рамки простого оформления виджетов Flutter. Он добавляет "
           "свои особенности, объединяя виджеты меньшего размера, упрощая "
           "сложности, внедряя лучшие практики пользовательского интерфейса и применяя "
           "разумных настроек по умолчанию. Это гарантирует, что ваши приложения будут"
           " выглядеть стильными и безупречными, не требующими дополнительного изменения"
           " дизайна")
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.Text(value=txt,
                                  text_align=ft.TextAlign.START,),
                          ft.Button("Кнопка"),]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)