# NavigationDrawer_2
import flet as ft

def main(page: ft.Page):
    page.title = "NavigationDrawer"
    async def handle_show_drawer():
        await page.show_end_drawer()

    async def handle_change(e: ft.Event[ft.NavigationDrawer]):
        print(f"Выбрана страница: {e.control.selected_index}")
        await page.close_end_drawer()

    page.end_drawer = ft.NavigationDrawer(
        on_change=handle_change,
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP,
                label="Страница 0",),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ADD_COMMENT),
                label="Страница 1",),],)

    page.add(
        ft.SafeArea(content=ft.Button(content="Показать панель",
                                      on_click=handle_show_drawer,)))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)