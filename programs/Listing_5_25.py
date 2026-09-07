# SnackBar_1
import flet as ft

def main(page: ft.Page):
    page.title = "SnackBar"
    def on_click(e: ft.Event[ft.Button]):
        page.show_dialog(ft.SnackBar(ft.Text("Привет! Это текст сообщения!")))

    page.add(ft.SafeArea(content=ft.Button("Открыть сообщение",
                                           on_click=on_click)))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)