# NavigationDrawer_3
import flet as ft

def main(page: ft.Page):
    page.title = "NavigationDrawer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.INDIGO,
        navigation_drawer_theme=ft.NavigationDrawerTheme(
            bgcolor=ft.Colors.RED_300,
            indicator_color=ft.Colors.INDIGO_100,
            icon_theme={
                ft.ControlState.DEFAULT: ft.IconTheme(
                    color=ft.Colors.INDIGO_900,
                    size=22,),
                ft.ControlState.SELECTED: ft.IconTheme(
                    color=ft.Colors.YELLOW,
                    size=28,),},
            label_text_style={
                ft.ControlState.DEFAULT: ft.TextStyle(
                    color=ft.Colors.YELLOW,
                    size=11,
                    italic=True,),
                ft.ControlState.SELECTED: ft.TextStyle(
                    color=ft.Colors.INDIGO_900,
                    size=15,
                    weight=ft.FontWeight.BOLD,),},
            ),
        )

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(
                padding=ft.Padding.only(left=28, top=20, bottom=12),
                content=ft.Text(
                    "Рабочее место", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.DASHBOARD,
                label="Панель инструментов",),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                selected_icon=ft.Icons.NOTIFICATIONS,
                label="Уведомления",),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Настройки",),
        ],
    )

    async def handle_show_drawer(e: ft.Event[ft.Button]):
        await page.show_drawer()

    page.add(
        ft.SafeArea(content=ft.Button("Показать панель",
                                      icon=ft.Icons.MENU,
                                      on_click=handle_show_drawer,),
                    )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)