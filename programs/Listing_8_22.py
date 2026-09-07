# ExpansionTile_2
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionTile"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.spacing = 0
    page.padding = 0

    def handle_tile_change(e: ft.Event[ft.ExpansionTile]):
        if e.data:
            v = "развернут"
        else:
            v = "свернут"

        page.show_dialog(
            ft.SnackBar(duration=1000,
                        content=ft.Text(value=f"ExpansionTile: {v}"),))

        if e.control.trailing:
            e.control.trailing.icon = (
                ft.Icons.ARROW_DROP_DOWN
                if e.control.trailing.icon == ft.Icons.ARROW_DROP_DOWN_CIRCLE
                else ft.Icons.ARROW_DROP_DOWN_CIRCLE)
            e.control.trailing.update()

    et_1 = ft.ExpansionTile(
        expanded=True,
        title=ft.Text("Заголовок плитки 1"),
        subtitle=ft.Text("Подзаголовок со стрелкой"),
        affinity=ft.TileAffinity.PLATFORM,
        maintain_state=True,
        collapsed_text_color=ft.Colors.RED,
        text_color=ft.Colors.RED,
        controls=[ft.ListTile(title=ft.Text("Это строка с содержимым плитки 1.1")),
                  ft.ListTile(title=ft.Text("Это строка с содержимым плитки 1.2")),],)
    et_2 = ft.ExpansionTile(
        expanded=True,
        title=ft.Text("Заголовок плитки 2"),
        subtitle=ft.Text("Подзаголовок со стрелкой icon"),
        trailing=ft.Icon(ft.Icons.ARROW_DROP_DOWN),
        collapsed_text_color=ft.Colors.GREEN,
        text_color=ft.Colors.GREEN,
        on_change=handle_tile_change,
        controls=[ft.ListTile(title=ft.Text("Это строка с содержимым плитки 2.1")),
                  ft.ListTile(title=ft.Text("Это строка с содержимым плитки 2.2")),],)
    et_3 = ft.ExpansionTile(
        expanded=True,
        title=ft.Text("Заголовок плитки 3"),
        subtitle=ft.Text("Подзаголовок стрелка справа"),
        affinity=ft.TileAffinity.LEADING,
        collapsed_text_color=ft.Colors.BLUE_800,
        text_color=ft.Colors.BLUE_200,
        controls=[ft.ListTile(title=ft.Text("Это строка с содержимым плитки 3.1")),
                  ft.ListTile(title=ft.Text("Это строка с содержимым плитки 3.2")),],)
    page.add(ft.SafeArea(
        content=ft.Column(spacing=0,
                          controls=[et_1, et_2, et_3,],),),)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)