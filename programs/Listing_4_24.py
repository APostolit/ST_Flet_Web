# Switch_2
import flet as ft

def main(page: ft.Page):
    page.title = "Switch"
    def handle_switch_change(e: ft.Event[ft.Switch]):
        page.theme_mode = ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT
        e.control.label = (
            "Светлая тема"
            if page.theme_mode == ft.ThemeMode.LIGHT
            else "Темная тема"
        )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.SafeArea(
            content=ft.Switch(
                key="theme_mode_switch",
                label="Переключатель темы",
                on_change=handle_switch_change,
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)