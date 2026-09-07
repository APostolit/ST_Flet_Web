# SnackBar_3
import flet as ft

def main(page: ft.Page):
    page.title = "SnackBar"
    def open_simple_action(e: ft.Event[ft.Button]):
        page.show_dialog(
            ft.SnackBar(ft.Text("Файл был удален."),
                        action="Отменить",
                        on_action=lambda e: print("Отмена удаления файла"),))

    def open_custom_action(e: ft.Event[ft.Button]):
        page.show_dialog(
            ft.SnackBar(ft.Text("Каталог был удален."),
                        persist=False,
                        action=ft.SnackBarAction(
                            label="Отменить удаление",
                            text_color=ft.Colors.YELLOW,
                            bgcolor=ft.Colors.BLUE,
                            on_click=lambda e: print("Отмена удаления каталога"),),)
            )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button("Открыть SnackBar с простым действием",
                              on_click=open_simple_action,),
                    ft.Button("Открыть SnackBar с заданным действием",
                              on_click=open_custom_action,),
                    ]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)