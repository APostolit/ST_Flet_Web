# AutofillGroup.py
import flet as ft

def main(page: ft.Page):
    page.title = "Автозаполнение для группы"
    page.add(
        ft.SafeArea(
            content=ft.AutofillGroup(
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            label="Имя",
                            autofill_hints=ft.AutofillHint.NAME,
                        ),
                        ft.TextField(
                            label="Email",
                            autofill_hints=[ft.AutofillHint.EMAIL],
                        ),
                        ft.TextField(
                            label="Номер телефона",
                            autofill_hints=[ft.AutofillHint.TELEPHONE_NUMBER],
                        ),
                        ft.TextField(
                            label="Адрес",
                            autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,
                        ),
                        ft.TextField(
                            label="Почтовый код",
                            autofill_hints=ft.AutofillHint.POSTAL_CODE,
                        ),
                    ]
                )
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)