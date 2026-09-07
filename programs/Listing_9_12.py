# Shimmer_1
import flet as ft

def main(page: ft.Page):
    page.title = "Shimmer"
    page.add(
        ft.SafeArea(
            content=ft.Shimmer(
                base_color=ft.Colors.with_opacity(0.3, ft.Colors.GREY_800),
                highlight_color=ft.Colors.WHITE,
                content=ft.Container(height=80, bgcolor=ft.Colors.GREY_300),
                ),
            )
        )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)