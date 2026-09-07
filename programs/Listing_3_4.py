# Button_4.py
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопки, события"
    def button_clicked(e: ft.Event[ft.Button]):
        button.data += 1
        message.value = f"Кнопка нажата: {button.data} раз(а)"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    button := ft.Button(content="Кнопка",
                                        data=0,
                                        on_click=button_clicked,),
                    message := ft.Text(),]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)