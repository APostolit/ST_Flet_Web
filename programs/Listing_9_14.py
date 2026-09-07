# TransparentPointer_1
import flet as ft

def main(page: ft.Page):
    page.title = "TransparentPointer"

    def button_clicked(e):
       page.show_dialog(ft.SnackBar(ft.Text("Нажата Кнопка 1")))

    def detector_clicked(e):
       page.show_dialog(ft.SnackBar(ft.Text("Касание детектора")))

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Stack(
                expand=True,
                controls=[
                    ft.GestureDetector(
                        on_tap=detector_clicked,),
                    ft.TransparentPointer(
                        content=ft.Container(padding=50,
                                             content=ft.Button("Кнопка 1",
                                                               on_click=button_clicked,),)
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)