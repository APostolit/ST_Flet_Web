# Container_6
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер - анимированное меню"
    def show_menu(e: ft.Event[ft.Button]):
        container.offset = ft.Offset(0, 0)
        container.update()

    def hide_menu(e: ft.Event[ft.IconButton]):
        container.offset = ft.Offset(-2, 0)
        container.update()

    col_menu = ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.IconButton(icon=ft.Icons.CLOSE, on_click=hide_menu)],),
                    ft.ListTile(
                        title=ft.Text("Опция 1"),
                        on_click=lambda _: print("Выбрана опция 1"),),
                    ft.ListTile(
                        title=ft.Text("Опция 2"),
                        on_click=lambda _: print("Выбрана опция 2"),),])

    page.overlay.append(
        container := ft.Container(
            left=10,
            top=10,
            width=200,
            height=300,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            border_radius=5,
            offset=ft.Offset(-2, 0),
            animate_offset=ft.Animation(300, ft.AnimationCurve.EASE_IN),
            content=col_menu))

    page.add(ft.SafeArea(content=ft.Button("Показать меню", on_click=show_menu)))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)