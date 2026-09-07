# CupertinoCheckbox_1
import flet as ft

def main(page: ft.Page):
    page.title = "Флажок CupertinoCheckbox"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.CupertinoCheckbox(label="Флажок Cupertino", value=True),
                    ft.Checkbox(label="Флажок Material", value=True),
                    ft.Text(value=("Адаптивный флажок отображается как "
                                   "флажок Cupertino на macOS и iOS, а "
                                   "также как флажок на других платформах:")),
                    ft.Checkbox(adaptive=True,
                                label="Адаптивный флажок",
                                value=True,),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)