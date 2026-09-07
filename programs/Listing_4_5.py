# Checkbox_3
import flet as ft

def main(page: ft.Page):
    page.title = "Стилизация флажков"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.Checkbox(label="Стиль по умолчанию"),
                          ft.Checkbox(
                              label="Статичный цвет",
                              fill_color=ft.Colors.RED,
                              check_color=ft.Colors.YELLOW,),
                          ft.Row(controls=[
                              ft.Checkbox(
                                  key="dynamic_fill_checkbox",
                                  fill_color={
                                      ft.ControlState.HOVERED: ft.Colors.BLUE,
                                      ft.ControlState.SELECTED: ft.Colors.GREEN,
                                      ft.ControlState.DEFAULT: ft.Colors.RED,},),
                              ft.Text("Динамичный цвет"),],
                              ),
                          ]
                )
            ),
        )
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)