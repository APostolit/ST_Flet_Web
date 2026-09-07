# ExpansionPanelList_3
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionPanelList"
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.ExpansionPanelList(
                expand=True,
                scroll=ft.ScrollMode.ALWAYS,
                spacing=8,
                controls=[
                    ft.ExpansionPanel(
                        can_tap_header=True,
                        header=ft.ListTile(title=ft.Text(f"Панель {i}")),
                        content=ft.ListTile(
                            title=ft.Text(f"Заголовок панели {i}"),
                            subtitle=ft.Text(
                                "Это содержимое может быть развернуто или свернуто."),),)
                    for i in range(1, 41)
                ],
            ),
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)