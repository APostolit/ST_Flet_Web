# SnackBar_2
import flet as ft

class Data:
    def __init__(self) -> None:
        self.counter = 0
    def increment(self):
        self.counter += 1
    def decrement(self):
        self.counter -= 1

data = Data()

def main(page: ft.Page):
    page.title = "SnackBar"

    snack_bar = ft.SnackBar(
        content=ft.Text("Вы открыли сообщение!"),
        action="Закрыть",)

    def handle_button_click(e: ft.Event[ft.Button]):
        data.increment()
        snack_bar.content.value = f"Сообщение открыто {data.counter} раз(а)"
        if not snack_bar.open:
            page.show_dialog(snack_bar)
        page.update()

    page.add(
        ft.SafeArea(content=ft.Button("Открыть сообщение",
                                      on_click=handle_button_click)))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)