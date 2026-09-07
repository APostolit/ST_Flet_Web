# Divider_1
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент Divider"
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                spacing=0,
                expand=True,
                controls=[
                    ft.Container(expand=True,
                                 bgcolor=ft.Colors.AMBER,
                                 alignment=ft.Alignment.CENTER,),
                    ft.Divider(),
                    ft.Container(expand=True,
                                 bgcolor=ft.Colors.PINK,
                                 alignment=ft.Alignment.CENTER,),
                    ft.Divider(height=20, color=ft.Colors.BLUE),
                    ft.Container(expand=True,
                                 bgcolor=ft.Colors.BLUE_300,
                                 alignment=ft.Alignment.CENTER,),
                    ft.Divider(height=9, thickness=10, color=ft.Colors.BLACK),
                    ft.Container(expand=True,
                                 bgcolor=ft.Colors.DEEP_PURPLE_200,
                                 alignment=ft.Alignment.CENTER,),
                    ],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)