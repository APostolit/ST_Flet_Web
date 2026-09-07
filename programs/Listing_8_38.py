# Stack_1
import flet as ft

def main(page: ft.Page):
    page.title = "Stack"
    d = ft.Stack(
        width=300,
        height=300,
        controls=[ft.Image(src="images/fox.jpg",
                           width=300,
                           height=300,
                           fit=ft.BoxFit.CONTAIN,),
                  ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                         controls=[ft.Text(value="Лиса",
                                           color=ft.Colors.SURFACE_BRIGHT,
                                           size=30,
                                           weight=ft.FontWeight.BOLD,
                                           opacity=0.7,)],),],
        )
    page.add(d)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)