# Radio_2
import flet as ft

def main(page: ft.Page):
    page.title = "Radio"
    page.add(
        ft.SafeArea(
            content=ft.RadioGroup(
                ft.Column(
                    controls=[
                        ft.Radio(key="styled_radio_default",
                                 label="Стиль по умолчанию",
                                 value="1",),
                        ft.Radio(key="styled_radio_constant",
                                 label="Статичный цвет",
                                 value="2",
                                 fill_color=ft.Colors.RED,),
                        ft.Radio(key="styled_radio_dynamic",
                                 label="Динамичный цвет",
                                 value="3",
                                 fill_color={ft.ControlState.HOVERED: ft.Colors.BLUE,
                                             ft.ControlState.SELECTED: ft.Colors.GREEN,
                                             ft.ControlState.DEFAULT: ft.Colors.RED,},),
                    ]
                )
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)