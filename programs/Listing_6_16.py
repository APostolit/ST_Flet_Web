# CupertinoBottomSheet_1
import flet as ft

def main(page: ft.Page):
    page.title = "Нижний лист"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    messages = ft.Column(tight=True)

    def handle_click(e: ft.Event[ft.CupertinoActionSheetAction]):
        messages.controls.append(ft.Text(f"Выбрано действие: {e.control.content.value}"))
        page.update()
        page.pop_dialog()

    action_sheet = ft.CupertinoActionSheet(
        title=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ft.Text("Заголовок"), ft.Icon(ft.Icons.BEDTIME)],),
        message=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ft.Text("Описание"), ft.Icon(ft.Icons.AUTO_AWESOME)],),
        cancel=ft.CupertinoActionSheetAction(
            on_click=handle_click,
            content=ft.Text("Выход"),),
        actions=[
            ft.CupertinoActionSheetAction(
                default=True,
                on_click=handle_click,
                content=ft.Text("Действие 1"),),
            ft.CupertinoActionSheetAction(
                on_click=handle_click,
                content=ft.Text("Действие 2"),),
            ft.CupertinoActionSheetAction(
                destructive=True,
                on_click=handle_click,
                content=ft.Text("Действие 3"),),
        ],
    )
    bottom_sheet = ft.CupertinoBottomSheet(action_sheet)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.CupertinoFilledButton(
                        on_click=lambda _: page.show_dialog(bottom_sheet),
                        content="Открыть нижний лист",),
                    messages,
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)