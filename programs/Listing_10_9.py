# Router_2
"""Компоновка маршрутов с общим макетом страницы"""
import flet as ft

@ft.component
def Home():
    return ft.Text("Главная страница!", size=24)

@ft.component
def About():
    return ft.Text("О компании", size=24)

@ft.component
def Contact():
    return ft.Text("Контакты", size=24)

@ft.component
def AppLayout():
    outlet = ft.use_route_outlet()
    return ft.Column(
        [
            ft.Container(
                content=ft.Row(
                    [ft.Image('SIS.jpg',  width=50, height=50),
                     ft.Button("Домашняя",
                               on_click=lambda: ft.context.page.navigate("/"), ),
                        ft.Button("О компании",
                                  on_click=lambda: ft.context.page.navigate("/about"),),
                        ft.Button("Контакты",
                                  on_click=lambda: ft.context.page.navigate("/contact"),),
                    ]),
                bgcolor=ft.Colors.SURFACE_BRIGHT,
                padding=10,),
            ft.Divider(),
            ft.Container(content=outlet, padding=20, bgcolor=ft.Colors.BLUE_100,
                         width=500, height=200),
            ft.Divider(),
            ft.Text("Подвал страницы - (c) 2026", text_align=ft.TextAlign.CENTER),
            ft.Divider(),
        ],
    )

@ft.component
def App():
    return ft.SafeArea(
        content=ft.Router(
            [ft.Route(
                component=AppLayout,
                children=[ft.Route(index=True, component=Home),
                          ft.Route(path="about", component=About),
                          ft.Route(path="contact", component=Contact),],),
                ]
            )
        )

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))