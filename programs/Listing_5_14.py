# CupertinoAlertDialog_1
import flet as ft

def main(page: ft.Page):
    page.title = "Диалог CupertinoAlertDialog"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    messages = ft.Column(tight=True)

    def handle_dialog_dismissal(_: ft.Event[ft.DialogControl]):
        messages.controls.append(ft.Text("Диалог закрыт"))
        page.update()

    def handle_action_click(e: ft.Event[ft.CupertinoDialogAction]):
        messages.controls.append(ft.Text(f"Выбрана опция: {e.control.content}"))
        page.pop_dialog()

    dialog = ft.CupertinoAlertDialog(
        modal=True,
        title=ft.Text("Удалить файл"),
        content=ft.Text("Вы подтверждаете удаление файла?"),
        on_dismiss=handle_dialog_dismissal,
        actions=[
            ft.CupertinoDialogAction(destructive=True,
                                     on_click=handle_action_click,
                                     content="Да",),
            ft.CupertinoDialogAction(default=True,
                                     on_click=handle_action_click,
                                     content="Нет",),],)
    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.CupertinoFilledButton(
                        on_click=lambda _: page.show_dialog(dialog),
                        content="Открыть диалог", ),
                    messages,],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)