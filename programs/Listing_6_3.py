# CupertinoContextMenu_1
import flet as ft

def main(page: ft.Page):
    page.title = "Контекстное меню CupertinoContextMenu"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                actions=[
                    ft.CupertinoContextMenuAction(
                        default=True,
                        trailing_icon=ft.Icons.CHECK,
                        on_click=lambda _: print("Опция 1"),
                        content="Опция 1",),
                    ft.CupertinoContextMenuAction(
                        trailing_icon=ft.Icons.MORE,
                        on_click=lambda _: print("Опция 2"),
                        content="Опция 2",),
                    ft.CupertinoContextMenuAction(
                        destructive=True,
                        trailing_icon=ft.Icons.CANCEL,
                        on_click=lambda _: print("Опция 3"),
                        content="Опция 3",),
                ],
                content=ft.Image("https://picsum.photos/200/200"),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)