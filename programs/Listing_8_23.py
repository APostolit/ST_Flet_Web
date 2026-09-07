# ExpansionTile_3
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionTile"
    page.spacing = 20

    tile = ft.ExpansionTile(
        title=ft.Text("Это заголовок плитки.", weight=ft.FontWeight.BOLD),
        subtitle=ft.Text("Это подзаголовок."),
        affinity=ft.TileAffinity.LEADING,
        controls=[ft.Text("👻", size=80)],
        expanded=True,
        on_change=lambda e: print(f"Плитка была {'развернута' if e.data else 'свернута'}"),
    )

    def expand_tile(_: ft.Event[ft.FilledButton]):
        tile.expanded = True
        tile.update()

    def collapse_tile(_: ft.Event[ft.OutlinedButton]):
        tile.expanded = False
        tile.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton("Развернуть плитку", on_click=expand_tile),
                            ft.OutlinedButton("Свернуть плитку", on_click=collapse_tile),],
                    ),
                    tile,],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)