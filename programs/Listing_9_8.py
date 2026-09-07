# InteractiveViewer_2
import flet as ft

def main(page: ft.Page):
    page.title = "InteractiveViewer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    async def handle_zoom_in(e: ft.Event[ft.Button]):
        await i.zoom(1.2)
    async def handle_zoom_out(e: ft.Event[ft.Button]):
        await i.zoom(0.8)
    async def handle_pan(e: ft.Event[ft.Button]):
        await i.pan(dx=50, dy=50)
    async def handle_reset(e: ft.Event[ft.Button]):
        await i.reset()
    async def handle_reset_slow(e: ft.Event[ft.Button]):
        await i.reset(animation_duration=ft.Duration(seconds=2))
    async def handle_save_state(e: ft.Event[ft.Button]):
        await i.save_state()
    async def handle_restore_state(e: ft.Event[ft.Button]):
        await i.restore_state()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    i := ft.InteractiveViewer(
                        min_scale=0.1,
                        max_scale=5,
                        boundary_margin=ft.Margin.all(20),
                        content=ft.Image(src="https://picsum.photos/500/500"),),
                    ft.Row(wrap=True,
                           controls=[
                               ft.Button("Увеличить", on_click=handle_zoom_in),
                               ft.Button("Уменьшить", on_click=handle_zoom_out),
                               ft.Button("Панорама", on_click=handle_pan),
                               ft.Button("Сохранить", on_click=handle_save_state),
                               ft.Button("Восстановить", on_click=handle_restore_state),
                               ft.Button("Перегрузить (быстро)", on_click=handle_reset),
                               ft.Button("Перегрузить (медленно)",
                                         on_click=handle_reset_slow),
                        ],
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)