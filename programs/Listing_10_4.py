# NavigationDrawer_1
import flet as ft
from dateutil.utils import within_delta


def main(page: ft.Page):
    page.title = "NavigationDrawer"
    body_text = ft.Text("Главная страница")

    async def handle_show_drawer():
        await page.show_drawer()

    async def handle_change(e: ft.Event[ft.NavigationDrawer]):
        if e.control.selected_index == 0:
            body_text.value = "Главная страница"
        elif e.control.selected_index == 1:
            body_text.value = "Почтовый адрес"
        else:
            body_text.value = "Контакты"
        await page.close_drawer()

    page.drawer = ft.NavigationDrawer(
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Главная страница",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Почтовый адрес",),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Контакты",),],)

    page.add(ft.SafeArea(
        ft.Column(controls=[ft.Button(content="Показать панель",
                                      on_click=handle_show_drawer,),
                            ft.Stack(width=300,
                                     height=100,
                                     alignment=ft.Alignment.CENTER,
                                     controls=[body_text]),
                            ]
                  )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)