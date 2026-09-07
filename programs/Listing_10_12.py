# Router_5
import flet as ft

@ft.component
def Home():
    return ft.Text("Домашняя страница", size=24)

@ft.component
def Products():
    return ft.Text("Страница с продуктами", size=24)

@ft.component
def Settings():
    return ft.Text("Страница с настройками", size=24)

@ft.component
def NavLink(label, path):
    """Подсвеченная активная навигационная ссылка функцией is_route_active()"""
    active = ft.is_route_active(path)
    return ft.Container(
        content=ft.Text(
            label,
            weight=ft.FontWeight.BOLD if active else ft.FontWeight.NORMAL,
            color=ft.Colors.BLUE if active else ft.Colors.ON_SURFACE,),
        bgcolor=ft.Colors.BLUE_50 if active else None,
        padding=ft.Padding.symmetric(horizontal=16, vertical=8),
        border_radius=8,
        on_click=lambda: ft.context.page.navigate(path),)

@ft.component
def AppLayout():
    """Навигационные ссылки на маршруты"""
    outlet = ft.use_route_outlet()
    return ft.Column([
        ft.Row([ft.Image('SIS.jpg',  width=50, height=50),
                NavLink("Домашняя", "/"),
                NavLink("Продукты", "/products"),
                NavLink("Настройки", "/settings"),]),
        ft.Divider(),
        outlet,])

@ft.component
def App():
    return ft.SafeArea(
        content=ft.Router(
            [ft.Route(
                component=AppLayout,
                children=[ft.Route(index=True, component=Home),
                          ft.Route(path="products", component=Products),
                          ft.Route(path="settings", component=Settings),],),
                ]
            )
        )

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))