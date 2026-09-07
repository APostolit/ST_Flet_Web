# CupertinoNavigationBar_1
import flet as ft

def main(page: ft.Page):
    page.title = "Панель CupertinoNavigationBar"

    def clicked(e: ft.Event[ft.CupertinoNavigationBar]):
        page.show_dialog(ft.SnackBar(
            ft.Text(f"Выбрано {e.control.selected_index}")))

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.AMBER_100,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=clicked,
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
                label="Избранное",),],)

    page.add(
        ft.SafeArea(
            content=ft.Text("Содержимое окна приложения!"),))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)