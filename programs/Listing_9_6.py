# GestureDetector_2
import random
import flet as ft

def main(page: ft.Page):
    page.title = "Обработка событий GestureDetector"
    def on_pan_update(event: ft.DragUpdateEvent[ft.GestureDetector]):
        container.top = max(0.0, container.top + event.local_delta.y)
        container.left = max(0.0, container.left + event.local_delta.x)
        container.update()

    gesture_detector = ft.GestureDetector(mouse_cursor=ft.MouseCursor.BASIC,
                                          drag_interval=50,
                                          on_pan_update=on_pan_update,)
    container = ft.Container(bgcolor=ft.Colors.AMBER,
                             width=150, height=150, left=0, top=0,
                             content=gesture_detector,)

    def handle_button_click(e: ft.Event[ft.Button]):
        gesture_detector.mouse_cursor = random.choice(list(ft.MouseCursor))
        text.value = f"Курсор мыши:  {gesture_detector.mouse_cursor}"
        gesture_detector.update()
        text.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.Stack(width=500,height=250,
                                   controls=[container],),
                          ft.Button("Сменить курсор мыши",
                                    on_click=handle_button_click),
                          text := ft.Text(f"Выбран курсор:"
                                          f"  {gesture_detector.mouse_cursor}"),],
                ),
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)