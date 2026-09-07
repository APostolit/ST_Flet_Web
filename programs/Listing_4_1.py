# AutoComplete_1.py
import flet as ft

numbers = [("Один 1", "Один"),
           ("Два 2", "Два"),
           ("Три 3", "Три"),
           ("Четыре 4", "Четыре"),
           ("Пять 5", "Пять"),]

# Список из вторых элементов кортежа
lv = ft.ListView(expand=True,)
for tuple_item in numbers:
    lv.controls.append(ft.Text(f"{tuple_item[1]}"))

# Стартовый модуль
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "Поле выбора по символу"

    def handle_change(e: ft.Event[ft.AutoComplete]):
        info.value = f"Текущий ввод:👉 {e.data!r} \n"

    def handle_select(e: ft.AutoCompleteSelectEvent):
        info.value = (
            f"Текущий ввод:👉 {e.control.value!r} \n"
            f"Ваш выбор:👍 {e.selection.value}"
        )

    txt1 = ft.Text('👇🏻Варианты выбора:')

    # Создание страницы
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[txt1, lv, ft.Divider(),
                    ft.AutoComplete(value="",
                                    width=200,
                                    on_change=handle_change,
                                    on_select=handle_select,
                                    suggestions=[
                            ft.AutoCompleteSuggestion(key=key, value=value)
                            for key, value in numbers],),
                    info := ft.Text(
                        "Введите номер (словом или цифрой), чтобы сделать выбор."
                    ),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)