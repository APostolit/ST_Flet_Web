# Router_1
"""Базовый маршрутизатор"""
import flet as ft

@ft.component
def Home():
    return ft.Text("Домашняя страница", size=24)

@ft.component
def About():
    return ft.Text("Сведения о компании", size=24)

@ft.component
def App():
    return ft.SafeArea(
        content=ft.Column(
            [ft.Row(
                [ft.Button("Домашняя",
                           on_click=lambda: ft.context.page.navigate("/"),),
                 ft.Button("О компании",
                           on_click=lambda: ft.context.page.navigate("/about"),),]
                ),
                ft.Router(
                    [ft.Route(index=True, component=Home),
                     ft.Route(path="about", component=About),]
                ),
            ]
        )
    )

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))