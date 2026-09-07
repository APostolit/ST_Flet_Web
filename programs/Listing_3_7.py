# Button_7.py
import flet as ft

bt = ft.Button(
    content="Стиль кнопки",
    style=ft.ButtonStyle(
    color={ft.ControlState.HOVERED: ft.Colors.BLUE,
           ft.ControlState.FOCUSED: ft.Colors.BLUE,
           ft.ControlState.DEFAULT: ft.Colors.BLACK,},
    bgcolor={ft.ControlState.FOCUSED: ft.Colors.PINK_200,
             ft.ControlState.DEFAULT: ft.Colors.YELLOW,},
    padding={ft.ControlState.HOVERED: 20},
    overlay_color=ft.Colors.TRANSPARENT,
    elevation={ft.ControlState.DEFAULT: 0,
                ft.ControlState.HOVERED: 5,
                ft.ControlState.PRESSED: 10,},
    animation_duration=500,
    side={ft.ControlState.DEFAULT: ft.BorderSide(1, color=ft.Colors.BLUE_100),
          ft.ControlState.HOVERED: ft.BorderSide(3, color=ft.Colors.BLUE_400),
          ft.ControlState.PRESSED: ft.BorderSide(6, color=ft.Colors.BLUE_600),},
    shape={ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
           ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),},
        ),
    )

def main(page: ft.Page):
    page.title = "Стили кнопок"
    page.add(ft.SafeArea(content=ft.Column(controls=[bt])))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)