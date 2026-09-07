# Pagelet_1
import asyncio
import flet as ft

def main(page: ft.Page):
    page.title = "Pagelet"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=(
                ft.Pagelet(
                    width=400,
                    height=600,

                    # Верхняя панель
                    appbar=ft.AppBar(
                        title=ft.Text("Pagelet - верхняя панель"),
                        center_title=True,
                        bgcolor=ft.Colors.RED_500,),
                    content=ft.Text("Тело элемента Pagelet"),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,

                    # Нижняя панель
                    bottom_appbar=ft.BottomAppBar(
                        bgcolor=ft.Colors.BLUE,
                        shape=ft.CircularRectangleNotchShape(),
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                                ft.Container(expand=True),
                                ft.IconButton(
                                    icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                                ft.IconButton(
                                    icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
                            ],
                        ),
                    ),

                    # Навигационная панель
                    drawer=ft.NavigationDrawer(
                        on_dismiss=lambda e: print("Левый Drawer освобожден"),
                        controls=[
                            ft.NavigationDrawerDestination(
                                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP,
                                label="Левый элемент 1",),
                            ft.NavigationDrawerDestination(
                                icon=ft.Icons.ADD_COMMENT,
                                label="Левый элемент 2",),],),
                    end_drawer=ft.NavigationDrawer(
                        on_dismiss=lambda e: print("Правый Drawer освобожден"),
                        controls=[
                            ft.NavigationDrawerDestination(
                                icon=ft.Icons.SLOW_MOTION_VIDEO,
                                label="Правый элемент 3",),
                            ft.NavigationDrawerDestination(
                                icon=ft.Icons.INSERT_CHART,
                                label="Правый элемент 4",),],),

                    # Нижняя плавающая кнопка
                    floating_action_button=ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        shape=ft.CircleBorder(),),
                    floating_action_button_location=
                    ft.FloatingActionButtonLocation.CENTER_DOCKED,
                )
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)