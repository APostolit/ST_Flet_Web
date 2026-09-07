# Checkbox_1
import flet as ft

def main(page: ft.Page):
    page.title = "Флажок Checkbox"
    def handle_button_click(e: ft.Event[ft.Button]):
        message.value = (
            f"Состояние флажков:  {c1.value}, {c2.value}, {c3.value}, "
            f"{c4.value}, {c5.value}.")

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    c1 := ft.Checkbox(
                        label="Флажок отключен по умолчанию", value=False,),
                    c2 := ft.Checkbox(
                        label="Флажок с тремя состояниями", tristate=True),
                    c3 := ft.Checkbox(label="Флажок включен по умолчанию", value=True),
                    c4 := ft.Checkbox(label="Отключенный флажок", disabled=True),
                    c5 := ft.Checkbox(
                        label="Флажок с меткой в левой позиции",
                        label_position=ft.LabelPosition.LEFT,),
                    ft.Button(content="Принять", on_click=handle_button_click),
                    message := ft.Text(),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)