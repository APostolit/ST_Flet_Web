# SelectionArea_1
import flet as ft

def main(page: ft.Page):
    page.title = "SelectionArea"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.SelectionArea(
                    content=ft.Column(
                        controls=[ft.Text("Выбираемый текст",
                                          color=ft.Colors.GREEN,
                                          key="selectable",),
                                  ft.Text("то же выбираемый текст",
                                          color=ft.Colors.GREEN,),])),
                    ft.Text("Не выбираемый текст",
                            color=ft.Colors.RED,
                            key="non-selectable",),
                    ]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)