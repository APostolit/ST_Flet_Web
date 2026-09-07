# Icon_1
from typing import cast
import flet as ft

def main(page: ft.Page):
    page.title = "Иконки Icon"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    # material
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK),
                            ft.Icon(ft.Icons.AUDIOTRACK,
                                    color=ft.Colors.GREEN_400,
                                    size=30,),
                            ft.Icon(ft.Icons.BEACH_ACCESS,
                                    color=ft.Colors.BLUE,
                                    size=50,),
                            ft.Icon(ft.Icons.SETTINGS, color="#c1c1c1"),]),
                    # cupertino
                    ft.Row(
                        controls=[
                            ft.Icon(ft.CupertinoIcons.PROFILE_CIRCLED,
                                    color=ft.Colors.PINK,),
                            ft.Icon(icon=ft.CupertinoIcons.BOOK,
                                    color=ft.Colors.GREEN_400,
                                    size=30,),
                            ft.Icon(icon=ft.CupertinoIcons.PHONE,
                                    color=ft.Colors.BLUE,
                                    size=50,),
                            ft.Icon(icon=ft.CupertinoIcons.ALARM,
                                    color="#c1c1c1",),
                            ]
                        ),
                    ],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)