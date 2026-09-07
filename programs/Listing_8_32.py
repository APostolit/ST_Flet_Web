# ResponsiveRow_1
import flet as ft

def main(page: ft.Page):
    page.title = "ResponsiveRow_1"
    def handle_page_resize(e: ft.PageResizeEvent):
        pw.value = f"Ширина окна: {page.width} px"
        pw.update()

    page.on_resize = handle_page_resize
    pw = ft.Text(text_align=ft.TextAlign.END, style=ft.TextTheme.display_small)

    rr_1 = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=ft.Text("Поле 1"),
                padding=5,
                bgcolor=ft.Colors.YELLOW,
                col={ft.ResponsiveRowBreakpoint.XS: 12,
                     ft.ResponsiveRowBreakpoint.MD: 6,
                     ft.ResponsiveRowBreakpoint.LG: 3,},),
            ft.Container(
                content=ft.Text("Поле 2"),
                padding=5,
                bgcolor=ft.Colors.GREEN,
                col={ft.ResponsiveRowBreakpoint.XS: 12,
                     ft.ResponsiveRowBreakpoint.MD: 6,
                     ft.ResponsiveRowBreakpoint.LG: 3,},),
            ft.Container(
                content=ft.Text("Поле 3"),
                padding=5,
                bgcolor=ft.Colors.BLUE,
                col={ft.ResponsiveRowBreakpoint.XS: 12,
                     ft.ResponsiveRowBreakpoint.MD: 6,
                     ft.ResponsiveRowBreakpoint.LG: 3,},),
            ft.Container(
                content=ft.Text("Поле 4"),
                padding=5,
                bgcolor=ft.Colors.PINK_300,
                col={ft.ResponsiveRowBreakpoint.XS: 12,
                     ft.ResponsiveRowBreakpoint.MD: 6,
                     ft.ResponsiveRowBreakpoint.LG: 3,},),
            ],
        )

    rr_2 = ft.ResponsiveRow(
        run_spacing={ft.ResponsiveRowBreakpoint.XS: 10},
        controls=[ft.TextField(label="Текстовое поле 1",
                               col={ft.ResponsiveRowBreakpoint.MD: 4},),
                  ft.TextField(label="Текстовое поле 2",
                               col={ft.ResponsiveRowBreakpoint.MD: 4},),
                  ft.TextField(label="Текстовое поле 3",
                               col={ft.ResponsiveRowBreakpoint.MD: 4},),
                  ],)
    page.add(
        ft.SafeArea(content=ft.Column(
            controls=[rr_1, rr_2, pw,])
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)