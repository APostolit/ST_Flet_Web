# Markdown_2
import flet as ft

sample = """
# Flet
Flet — это фреймворк для создания автономных веб-, мобильных и настольных приложений
## Первые шаги
### Установить Fleter
~~~bash
pip install flet
~~~
### Создать программу на Python
~~~python
import flet as ft

def main(page: ft.Page):
    txt = ft.Text("Привет, Это приложение Flet!🌍")
    page.add(txt)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
~~~
Запустить приложение:
~~~bash
ft.run(main, view=ft.AppView.WEB_BROWSER)
~~~
## Ссылки на ресурсы
* [Getting started for Python](https://flet.dev/docs/getting-started/installation/)
* [Controls reference](https://flet.dev/docs/controls)
* [Tutorials](https://flet.dev/docs/tutorials)
* [Examples](https://github.com/flet-dev/examples/tree/main/python)
## Сообщества Flet
* [Discussions](https://github.com/flet-dev/flet/discussions)
* [Discord](https://discord.gg/dzWXP8SHG8)
* [Twitter](https://twitter.com/fletdev)
* [Email](mailto:hello@flet.dev)
"""

def main(page: ft.Page):
    page.title = "Текст в формате Markdown"
    page.scroll = ft.ScrollMode.AUTO

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    async def navigate_md_link(e: ft.Event[ft.Markdown]):
        await page.launch_url(e.data)

    page.add(
        ft.SafeArea(
            content=ft.Markdown(
                value=sample,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme=ft.MarkdownCodeTheme.ATOM_ONE_DARK,
                code_style_sheet=ft.MarkdownStyleSheet(
                    code_text_style=ft.TextStyle(font_family="Roboto Mono")
                ),
                on_tap_link=navigate_md_link,
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)