# Tabs_2
import flet as ft

def main(page: ft.Page):
    page.title = "Tabs"

    tabs_2 = ft.Tabs(
        length=2,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[ft.TabBar(
                secondary=True,
                tabs=[ft.Tab(label=ft.Text("Вложенная вкладка 1")),
                      ft.Tab(label=ft.Text("Вложенная вкладка 2")),],),
                ft.TabBarView(
                    expand=True,
                    controls=[ft.Text("Содержимое вложенной вкладки 1"),
                              ft.Text("Содержимое вложенной вкладки 2"),],),],),)

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Tabs(
                length=2,
                selected_index=1,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[ft.TabBar(
                        tabs=[ft.Tab(label=ft.Text("Главная вкладка 1")),
                              ft.Tab(label=ft.Text("Главная вкладка 2")),],),
                        ft.TabBarView(expand=True,
                            controls=[ft.Text("Содержимое главной вкладки 1"),
                                      tabs_2,],),],),),))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)