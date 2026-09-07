# Container_8
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер - темы"

    cont_1 = ft.Container(
        height=100,
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
        content=ft.Row(controls=[
            ft.Button("Унаследованная тема с переопределенным основным цветом"),
            ft.TextButton("Кнопка 2"),]),)
    cont_2 = ft.Container(
        padding=20,
        bgcolor=ft.Colors.SURFACE_TINT,
        theme_mode=ft.ThemeMode.DARK,
        theme=ft.Theme(color_scheme_seed=ft.Colors.GREEN,
                       color_scheme=ft.ColorScheme(
                           primary_container=ft.Colors.BLUE),),
        content=ft.Row(
            controls=[
                ft.Button("Темная тема"),
                ft.TextButton("Текст кнопки"),
                ft.Text("Текст в основном цвете контейнера",
                        color=ft.Colors.PRIMARY_CONTAINER,),]),)
    cont_3 = ft.Container(
        padding=20,
        bgcolor=ft.Colors.SURFACE_TINT,
        border=ft.Border.all(3, ft.Colors.OUTLINE),
        theme_mode=ft.ThemeMode.LIGHT,
        theme=ft.Theme(),
        content=ft.Row(
            controls=[
                ft.Button("Светлая тема"),
                ft.TextButton("Текст кнопки"),
                ft.Text("Текст в основном цвете контейнера",
                        color=ft.Colors.PRIMARY_CONTAINER,),]),)
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Button("Тема страницы"),
                            ft.TextButton("Тема страницы текст кнопки"),
                            ft.Text("Текст в основном цвете контейнера",
                                    color=ft.Colors.PRIMARY_CONTAINER,),]),
                    cont_1, cont_2, cont_3,
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)