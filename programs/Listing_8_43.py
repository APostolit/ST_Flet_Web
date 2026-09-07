# Tabs_4
import flet as ft

def main(page: ft.Page):
    page.title = "Tabs"
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Tabs(
                length=2,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.TabBar(
                            tab_alignment=ft.TabAlignment.START,
                            indicator_animation=ft.TabIndicatorAnimation.ELASTIC,
                            indicator_size=ft.TabBarIndicatorSize.LABEL,
                            indicator=ft.UnderlineTabIndicator(
                                border_side=ft.BorderSide(5, color=ft.Colors.RED),
                                border_radius=ft.BorderRadius.all(1),
                                insets=ft.Padding.only(bottom=5),),
                            tabs=[ft.Tab(label=ft.Text("Домашняя")),
                                  ft.Tab(label=ft.Text("О компании")),],),
                        ft.TabBarView(
                            expand=True,
                            controls=[ft.Text("Содержимое домашней страницы"),
                                      ft.Text("Содержимое страницы о компании"),],),
                    ],
                ),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)