# ExpansionTile_6
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionTile"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.ExpansionTile(
                title=ft.Text(
                    value="Это плитка с выделенной границей",
                    text_align=ft.TextAlign.CENTER,),
                subtitle=ft.Text(
                    value="Граница изменится при расширении плитки",
                    text_align=ft.TextAlign.CENTER,),
                bgcolor=ft.Colors.BLUE_GREY_200,
                controls_padding=ft.Padding.symmetric(horizontal=10),
                collapsed_bgcolor=ft.Colors.BLUE_GREY_200,
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                shape=ft.RoundedRectangleBorder(radius=20),
                collapsed_shape=ft.StadiumBorder(side=ft.BorderSide(width=2)),
                collapsed_text_color=ft.Colors.GREY_800,
                text_color=ft.Colors.GREY_800,
                controls=[
                    ft.ListTile(
                        title=ft.Text("Это строка 1"),
                        bgcolor=ft.Colors.BLUE_GREY_200,
                        shape=ft.RoundedRectangleBorder(radius=20),),
                    ft.ListTile(
                        title=ft.Text("Это строка 2"),
                        bgcolor=ft.Colors.BLUE_GREY_200,
                        shape=ft.RoundedRectangleBorder(radius=20),),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)