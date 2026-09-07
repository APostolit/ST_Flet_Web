# CupertinoSwitch_1
import flet as ft

def main(page: ft.Page):
    page.title = "Переключатель"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.CupertinoSwitch(label="Переключатель Cupertino", value=True),
                    ft.Switch(label="Переключатель Material",
                              value=True,
                              thumb_color={ft.ControlState.SELECTED: ft.Colors.BLUE},
                              track_color=ft.Colors.YELLOW,
                              focus_color=ft.Colors.PURPLE,),
                    ft.Text(value=("Адаптивный переключатель отображается как "
                                   "CupertinoSwitch на macOS и iOS, и как "
                                   "Switch на других платформах:")),
                    ft.Switch(adaptive=True, label="Адаптивный переключатель", value=True),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)