# ExpansionTile_4
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionTile"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 20

    tile = ft.ExpansionTile(
        expanded=True,
        title=ft.Text("Открытие\закрытие с анимацией!"),
        controls=[ft.ListTile(title=ft.Text("Строка 1")),
                  ft.ListTile(title=ft.Text("Строка 2")),
                  ft.ListTile(title=ft.Text("Строка 3")),],)

    def switch_animation(e: ft.Event[ft.CupertinoSlidingSegmentedButton]):
        if e.control.selected_index == 0:
            tile.animation_style = None
        elif e.control.selected_index == 1:
            tile.animation_style = ft.AnimationStyle(
                curve=ft.AnimationCurve.BOUNCE_OUT,
                duration=ft.Duration(seconds=5),)
        else:
            tile.animation_style = ft.AnimationStyle.no_animation()
        tile.update()
    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.CupertinoSlidingSegmentedButton(
                        selected_index=0,
                        thumb_color=ft.Colors.BLUE_400,
                        on_change=switch_animation,
                        controls=[ft.Text("По умолчанию"),
                                  ft.Text("Пользовательская"),
                                  ft.Text("без анимации"),],),
                    tile,
                ],
            ),
        )
    )
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)