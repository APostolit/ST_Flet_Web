# MenuBar_1
import flet as ft

def submenu_open(e: ft.Event[ft.MenuItemButton]):
    print('Выбрана опция:', e.control.content.value)

def main(page: ft.Page):
    page.title = "Панель меню"
    d = ft.MenuBar(
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Открыть меню"),
                controls=[
                    ft.MenuItemButton(content=ft.Text("Опция 1"),
                                      on_click=submenu_open,),
                    ft.MenuItemButton(content=ft.Text("Опция 2"),
                                      on_click=submenu_open,),
                    ft.MenuItemButton(content=ft.Text("Опция 3"),
                                      on_click=submenu_open,),
                ],
            ),
        ],
    )
    page.add(d)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)