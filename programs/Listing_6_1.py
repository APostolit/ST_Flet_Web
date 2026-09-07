# ContextMenu_1
import flet as ft

async def main(page: ft.Page):
    page.title = "Контекстное меню"
    # в web режиме нужно отключить контекстное меню браузера по умолчанию
    if page.web:
        await page.browser_context_menu.disable()

    def handle_item_click(e: ft.Event[ft.PopupMenuItem]):
        action = e.control.content
        page.show_dialog(ft.SnackBar(content=f"Выбрана опция '{action}'"))

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.ContextMenu(
                primary_items=[
                    ft.PopupMenuItem(content="Левая кнопка 1",
                                     on_click=handle_item_click),
                    ft.PopupMenuItem(content="Левая кнопка 2",
                                     on_click=handle_item_click),
                ],
                primary_trigger=ft.ContextMenuTrigger.DOWN,
                secondary_items=[
                    ft.PopupMenuItem(content="Правая кнопка 1",
                                     on_click=handle_item_click),
                    ft.PopupMenuItem(content="Правая кнопка 2",
                                     on_click=handle_item_click),
                ],
                secondary_trigger=ft.ContextMenuTrigger.DOWN,
                tertiary_items=[
                    ft.PopupMenuItem(content="Средняя кнопка 1",
                                     on_click=handle_item_click),
                    ft.PopupMenuItem(content="Средняя кнопка 2",
                                     on_click=handle_item_click),
                ],
                tertiary_trigger=ft.ContextMenuTrigger.DOWN,
                on_select=lambda e: print(f"Выбрана опция: {e.item.content}"),
                on_dismiss=lambda e: print("Меню закрыто"),
                expand=True,
                content=ft.Container(
                    key="context_menu_trigger_area",
                    expand=True,
                    bgcolor=ft.Colors.BLUE_200,
                    alignment=ft.Alignment.CENTER,
                    border_radius=ft.BorderRadius.all(12),
                    content=ft.Text("Открыть контекстное меню (любая кнопка мыши)."),
                ),
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)