# AlertDialog_2.py
import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog пример 2"

    dialog = ft.AlertDialog(
        title=ft.Text("Заголовок окна"),
        content=ft.Text("Текст сообщения!"),
        alignment=ft.Alignment.CENTER,
        on_dismiss=lambda e: print("Диалоговое окно закрыто!"),
        title_padding=ft.Padding.all(25),)

    modal_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Заголовок окна"),
        content=ft.Text("Подтвердить действия?"),
        actions=[ft.TextButton("Да", on_click=lambda e: page.pop_dialog()),
                 ft.TextButton("Нет", on_click=lambda e: page.pop_dialog()),],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Модальное диалоговое окно закрыто!"),)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(content="Открыть обычное окно",
                              on_click=lambda e: page.show_dialog(dialog),),
                    ft.Button(content="Открыть модальное окно",
                              on_click=lambda e: page.show_dialog(modal_dialog),),
                    ]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)