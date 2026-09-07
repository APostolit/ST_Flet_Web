# RotatedBox_1
import flet as ft

def _demo_control(content: ft.Control) -> ft.Container:
    return ft.Container(
        padding=10,
        border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
        border_radius=8,
        content=content,)

def _lane(title: str, controls: list[ft.Control]) -> ft.Container:
    return ft.Container(
        width=540,
        padding=12,
        border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
        border_radius=12,
        content=ft.Column(
            spacing=8,
            controls=[
                ft.Text(title, size=16, weight=ft.FontWeight.BOLD),
                ft.Divider(height=1),
                ft.Row(spacing=14,
                       vertical_alignment=ft.CrossAxisAlignment.START,
                       controls=controls,),
                ],
            ),
        )

def main(page: ft.Page):
    page.title = "RotatedBox"
    page.padding = 24
    page.scroll = ft.ScrollMode.AUTO

    box_1 = _lane(
        "Обычные элементы управления",
        [_demo_control(ft.Text("Текст", size=26)),
         _demo_control(ft.ProgressBar(width=170, value=0.65, color=ft.Colors.GREEN)),
         _demo_control(ft.Button("Кнопка")),],)
    box_2 = _lane(
        "Повернутые элементы управления quarter_turns=1",
        [_demo_control(ft.RotatedBox(
            quarter_turns=1,
            content=ft.Text("Текст", size=26),)),
            _demo_control(ft.RotatedBox(
                quarter_turns=1,
                content=ft.ProgressBar(width=170, value=0.65, color=ft.Colors.GREEN,),)),
            _demo_control(ft.RotatedBox(
                quarter_turns=1,
                content=ft.Button("Кнопка"),)),],)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("RotatedBox поворачивается раньше, чем макет. "
                            "Сравните занимаемое пространство ниже:",
                            size=16,
                            weight=ft.FontWeight.W_500,),
                    ft.Column(
                        spacing=16,
                        controls=[box_1, box_2,],),]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)