# Router_9
import flet as ft

# ---------------------------------------------------------------------------
# Домашняя страница
# ---------------------------------------------------------------------------
@ft.component
def HomeContent():
    return ft.Column(
        [ft.Text("Домашняя", size=28, weight=ft.FontWeight.BOLD),
         ft.Text("Это главная страница приложения!", size=16),])

# ---------------------------------------------------------------------------
# Страницы с проектами
# ---------------------------------------------------------------------------
PROJECTS = {"1": "Настольные приложения",
            "2": "Мобильные приложения",
            "3": "Web - приложения",}

@ft.component
def ProjectsList():
    return ft.Column(
        [
            ft.Text("Все проекты", size=24),
            *[
                ft.Button(name,
                          on_click=lambda _, pid=pid: ft.context.page.navigate
                              (f"/projects/{pid}"),)
                for pid, name in PROJECTS.items()
            ],
        ]
    )

@ft.component
def ProjectDetails():
    params = ft.use_route_params()
    pid = params.get("pid", "?")
    name = PROJECTS.get(pid, "Unknown")
    return ft.Column(
        [ft.Text(name, size=24, weight=ft.FontWeight.BOLD),
         ft.Text(f"Проект ID: {pid}", size=16),
         ft.Text(f"Проект: {name}", size=14),
         ft.Text("Здесь можно найти подробную информацию о данном проекте.",
                 size=14,),])

# ---------------------------------------------------------------------------
# Настройки
# ---------------------------------------------------------------------------
@ft.component
def GeneralSettings():
    return ft.Column(
        [ft.Text("Главные настройки", size=24),
         ft.Switch(label="Темная тема"),
         ft.Switch(label="Уведомления"),
         ft.Switch(label="Автосохранение"),])

@ft.component
def AccountSettings():
    return ft.Column(
        [ft.Text("Настройки доступа", size=24),
         ft.TextField(label="Имя пользователя", value="Михаил"),
         ft.TextField(label="Email", value="mix@example.com"),
         ft.Button("Сохранить изменения"),])

@ft.component
def SettingsLayout():
    """Навигация по вкладкам настроек — возвращает элементы управления,
     а не представление."""
    outlet = ft.use_route_outlet()
    return ft.Column(
        [
            ft.Text("Настройки", size=28, weight=ft.FontWeight.BOLD),
            ft.Row(
                [
                    ft.Button(
                        "Главные",
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.PRIMARY_CONTAINER
                            if ft.is_route_active("/settings/general", exact=True)
                            else None,
                        ),
                        on_click=lambda: ft.context.page.navigate("/settings/general"),
                    ),
                    ft.Button(
                        "Доступ",
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.PRIMARY_CONTAINER
                            if ft.is_route_active("/settings/account", exact=True)
                            else None,
                        ),
                        on_click=lambda: ft.context.page.navigate("/settings/account"),
                    ),
                ],
            ),
            ft.Divider(),
            ft.Container(content=outlet, expand=True),
        ],
        expand=True,
    )

# ---------------------------------------------------------------------------
# Корневая разметка с навигационной рейкой
# ---------------------------------------------------------------------------
NAV_ROUTES = ["/", "/projects", "/settings/general"]

@ft.component
def RootLayout():
    """Корневой макет — возвращает вид с навигационной рейкой + outlet."""
    outlet = ft.use_route_outlet()

    selected = 0
    if ft.is_route_active("/projects"):
        selected = 1
    elif ft.is_route_active("/settings"):
        selected = 2

    def on_nav_change(e):
        ft.context.page.navigate(NAV_ROUTES[e.control.selected_index])

    return ft.View(
        route="/",
        can_pop=False,
        controls=[
            ft.Row(
                [
                    ft.NavigationRail(
                        selected_index=selected,
                        label_type=ft.NavigationRailLabelType.ALL,
                        destinations=[
                            ft.NavigationRailDestination(
                                icon=ft.Icons.HOME_OUTLINED,
                                selected_icon=ft.Icons.HOME,
                                label="Домашняя",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.FOLDER_OUTLINED,
                                selected_icon=ft.Icons.FOLDER,
                                label="Проекты",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.SETTINGS_OUTLINED,
                                selected_icon=ft.Icons.SETTINGS,
                                label="Настройки",
                            ),
                        ],
                        on_change=on_nav_change,
                    ),
                    ft.VerticalDivider(width=1),
                    ft.Container(content=outlet, expand=True, padding=20),
                ],
                expand=True,
            ),
        ],
    )

# ---------------------------------------------------------------------------
# Приложение
# ---------------------------------------------------------------------------
@ft.component
def App():
    return ft.Router(
        [
            ft.Route(
                component=RootLayout,
                outlet=True,
                children=[
                    ft.Route(index=True, component=HomeContent),
                    ft.Route(path="projects",
                             component=ProjectsList,
                             children=[ft.Route(path=":pid",
                                                component=ProjectDetails),],),
                    ft.Route(path="settings",
                             component=SettingsLayout,
                             outlet=True,
                             children=[ft.Route(path="general",
                                                component=GeneralSettings),
                                       ft.Route(path="account",
                                                component=AccountSettings),],),
                ],
            ),
        ],
        manage_views=True,
    )

if __name__ == "__main__":
    ft.run(lambda page: page.render_views(App))