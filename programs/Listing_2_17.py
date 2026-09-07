# ListTil_1
import flet as ft

def main(page: ft.Page):
    page.title = "ListTile"

    page.add(
        ft.SafeArea(
            content=ft.Card(
                content=ft.Container(
                    width=500,
                    padding=ft.Padding.symmetric(vertical=10),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            ft.ListTile(title=ft.Text("Плитка в одну строку")),
                            ft.ListTile(
                                title=ft.Text("Плотная плитка в одну строку"),
                                dense=True,
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SETTINGS),
                                title=ft.Text("Выбранная плитка в одну строку с иконкой"),
                                selected=True,
                            ),
                            ft.ListTile(
                                leading=ft.Image(
                                    src="images/fox.jpg",
                                    fit=ft.BoxFit.CONTAIN,
                                ),
                                title=ft.Text("Плитка в одну строку с картинкой"),
                            ),
                            ft.ListTile(
                                title=ft.Text("Плитка во дну строку с меню"),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Опция 1"),
                                        ft.PopupMenuItem(content="Опция 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ALBUM),
                                title=ft.Text(
                                    value=(
                                        "Строка с меню и с иконкой"
                                    )
                                ),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Опция 1"),
                                        ft.PopupMenuItem(content="Опция 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SNOOZE),
                                title=ft.Text(
                                    value=(
                                        "Первая строка, есть иконка"
                                    )
                                ),
                                subtitle=ft.Text("Вторая строка, есть меню."),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.Icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(content="Опция 1"),
                                        ft.PopupMenuItem(content="Опция 2"),
                                    ],
                                ),
                            ),
                        ],
                    ),
                )
            ),
        )
    )
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)