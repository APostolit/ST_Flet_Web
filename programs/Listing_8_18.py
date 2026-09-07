# ExpansionPanel_1
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionPanel"
    p = ft.ExpansionPanelList(
        width=400,
        controls=[
            ft.ExpansionPanel(
                header=ft.Text("Адрес магазина"),
                content=ft.Text("Шоссе Энтузиастов, д. 31"),
                expanded=True,),
            ft.ExpansionPanel(
                header=ft.Text("Адрес пункта выдачи"),
                content=ft.Column(controls=[ft.Text("Ул. Петровская, д.35"),
                                            ft.Image('images/win_c.png'),
                                            ft.Divider(),],
                                  spacing=5),
                expanded=True,)
            ],
        )

    page.add(p)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)