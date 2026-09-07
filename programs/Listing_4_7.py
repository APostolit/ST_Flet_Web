# CupertinoCheckbox_2
import flet as ft

def main(page: ft.Page):
    page.title = "Флажок CupertinoCheckbox со стилем"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.CupertinoCheckbox(
                        label="Флажок Cupertino с тремя состояниями",
                        value=True,
                        tristate=True,
                        check_color=ft.Colors.GREY_900,
                        fill_color={
                            ft.ControlState.HOVERED: ft.Colors.PINK_200,
                            ft.ControlState.PRESSED: ft.Colors.LIME_ACCENT_200,
                            ft.ControlState.SELECTED: ft.Colors.DEEP_ORANGE_200,
                            ft.ControlState.DEFAULT: ft.Colors.TEAL_200,},),
                    ft.CupertinoCheckbox(label="Флажок Cupertino в кружке",
                                         value=True,
                                         shape=ft.CircleBorder(),),
                    ft.CupertinoCheckbox(label="Флажок Cupertino в квадрате",
                                         value=True,),
                    ft.CupertinoCheckbox(label="Флажок Cupertino с меткой слева",
                                         value=True,
                                         label_position=ft.LabelPosition.LEFT,),
                    ],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)