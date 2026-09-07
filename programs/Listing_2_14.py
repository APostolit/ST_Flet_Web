# CodeEditor_3
import flet_code_editor as fce
import flet as ft

CODE = """# Комментарий 1
# Комментарий 2
# Комментарий 3

import json
import textwrap

# Исходные данные
x = 1
y = 2
z = 3

# Результат
print("ИТОГО z=" , z)
"""

def main(page: ft.Page):
    page.title = "CodeEditor - редактор кода"
    editor = fce.CodeEditor(
        language=fce.CodeLanguage.PYTHON,
        value=CODE,
        selection=ft.TextSelection(base_offset=41, extent_offset=62),
        autofocus=True,
        expand=True,
        on_selection_change=lambda e: print("Selection:", e),
    )

    async def fold_imports():
        await editor.fold_imports()

    async def fold_comment():
        await editor.fold_comment_at_line_zero()

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Button("Свернуть импорт", on_click=fold_imports),
                            ft.Button("Свернуть верхний комментарий", on_click=fold_comment),
                        ]
                    ),
                    editor,
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)