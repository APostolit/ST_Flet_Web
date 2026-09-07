# Checkbox_2
import flet as ft

def main(page: ft.Page):
    page.title = "Смена состояния флажка"
    events = ft.Column()

    def handle_checkbox_change(e: ft.Event[ft.Checkbox]):
        events.controls.append(ft.Text(f"Текущее состояние флажка {e.control.value}"))

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[ft.Checkbox(label="Флажок",
                                      on_change=handle_checkbox_change,),
                          events,]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)