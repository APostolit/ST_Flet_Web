# Lottie_1
import flet as ft
import flet_lottie as ftl

def main(page: ft.Page):
    page.title = "Lottie"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ftl.Lottie(
                        src="https://raw.githubusercontent.com/"
                            "xvrh/lottie-flutter/master/example/assets/Mobilo/A.json",
                        scale=ft.Scale(1, 1),
                        reverse=False,
                        animate=True,
                        error_content=ft.Placeholder(ft.Text("Error loading Lottie")),
                        on_error=lambda e: print(f"Error loading Lottie: {e.data}"),),
                    ],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)