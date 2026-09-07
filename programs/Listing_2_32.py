# TextField_3
import flet as ft

def main(page: ft.Page):
    page.title = "Text"

    def handle_selection_change(e: ft.TextSelectionChangeEvent[ft.TextField]):
        selection.value = (
            f"Выбрано: '{e.selected_text}'" if e.selected_text else "Нет выбора."
        )
        selection_details.value = f"start={e.selection.start}, end={e.selection.end}"
        caret.value = f"Текущая позиция: {e.selection.end}"

    async def select_characters(e: ft.Event[ft.Button]):
        await field.focus()
        field.selection = ft.TextSelection(
            base_offset=0, extent_offset=len(field.value)
        )

    async def move_caret(e: ft.Event[ft.Button]):
        await field.focus()
        field.selection = ft.TextSelection(base_offset=0, extent_offset=0)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                spacing=10,
                controls=[
                    field := ft.TextField(
                        value=(
                            "Благодарим вас за проявленный интерес к фреймворку flet. "
                            "Остается пожелать успехов в освоении данного инструментария."
                        ),
                        multiline=True,
                        min_lines=3,
                        autofocus=True,
                        on_selection_change=handle_selection_change,
                    ),
                    selection := ft.Text("Выберите фрагмент текста в поле."),
                    selection_details := ft.Text(),
                    caret := ft.Text("Текущая позиция указателя: -"),
                    ft.Button(
                        content="Выбрать весь текст",
                        on_click=select_characters,
                    ),
                    ft.Button(
                        content="Переметить указатель в начало",
                        on_click=move_caret,
                    ),
                ],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)