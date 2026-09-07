# CupertinoNavigationBar_2
import flet as ft

def main(page: ft.Page):
    page.title = "Панель CupertinoNavigationBar"
    body_text = ft.Text("Страница приложения - Карта")

    def change_page(e: ft.Event[ft.CupertinoNavigationBar]):
        if e.control.selected_index == 0:
            body_text.value = "Страница приложения - Карта"
        elif e.control.selected_index == 1:
            body_text.value = "Страница приложения - Доставка"
        else:
            body_text.value = "Страница приложения - Избранное"

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.BLUE_400,
        inactive_color=ft.Colors.WHITE_70,
        active_color=ft.Colors.BLACK,
        on_change=change_page,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.EXPLORE_OUTLINED,
                selected_icon=ft.Icons.EXPLORE,
                label="Карта",),
            ft.NavigationBarDestination(
                icon=ft.Icons.COMMUTE_OUTLINED,
                selected_icon=ft.Icons.COMMUTE,
                label="Доставка",),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Избранное",),],
    )

    page.add(ft.SafeArea(content=body_text,))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)