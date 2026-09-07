# PopupMenuButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "PopupMenuButton"
    def handle_check_item_click(e: ft.Event[ft.PopupMenuItem]):
        e.control.checked = not e.control.checked

    page.add(
        ft.SafeArea(
            content=ft.PopupMenuButton(
                key="popup",
                items=[
                    ft.PopupMenuItem(content="Элемент 1"),
                    ft.PopupMenuItem(icon=ft.Icons.POWER_INPUT, content="Элемент 2"),
                    ft.PopupMenuItem(content=ft.Row(
                        controls=[ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                                  ft.Text("Элемент 3"),]),
                        on_click=lambda _: print("Нажата кнопка с элементом 3!"),),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(content="Отметить элемент",
                                     checked=False,
                                     on_click=handle_check_item_click,),
                ],
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)