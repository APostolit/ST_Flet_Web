# ContextMenu_2
import flet as ft

def main(page: ft.Page):
    page.title = "Контекстное меню"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handle_select(e: ft.ContextMenuSelectEvent):
        action = e.item.content
        page.show_dialog(ft.SnackBar(f"Выбрано: '{action}'"))

    async def open_menu(e: ft.Event[ft.Button]):
        await menu.open()

    menu = ft.ContextMenu(
        on_select=handle_select,
        items=[
            ft.PopupMenuItem(
                content="Опция 1",
                on_click=lambda e: print(f"{e.control.content}"),),
            ft.PopupMenuItem(
                content="Опция 2",
                on_click=lambda e: print(f"{e.control.content}"),),
            ft.PopupMenuItem(
                content="Опция 3",
                on_click=lambda e: print(f"{e.control.content}"),),
        ],
        content=ft.Button("Открыть контекстное меню", on_click=open_menu),
    )

    page.add(ft.SafeArea(content=menu,),)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)