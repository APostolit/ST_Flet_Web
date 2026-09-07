# Markdown_1
import flet as ft

sample = """
# Примеры текста формата Markdown
Markdown позволяет вам легко включать в свое приложение форматированный текст, 
изображения и даже форматированный программный код приложения.
## Заголовок
Задания стиля
Это заголовок H1
=============
Это заголовок H2
-------------
Atx-стиль
# Это текст H1
## Это текст H2
###### Это текст H6
Выберите допустимые заголовки:
- [x] `# опция 1`
- [ ] `#опция 2`
## Ссылка
[Сайт google](https://www.google.com)
## Изображения
![Image from Flet assets](images/fl.png)
![Test image](https://picsum.photos/200/300)
## Таблица
|Синтаксис                              |Результат                            |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

## Стилизация
Style text as _italic_, __bold__, ~~strikethrough~~, or `inline code`.
- Маркированный список 1
- Маркированный список 2
- Маркированный список 3
## Программный код
Отформатированный код в силе Dart выглядит достаточно привлекательно:
~~~dart
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: ft.Markdown(data: markdownData),
    ),
  ));
}
~~~
"""

def main(page: ft.Page):
    page.title = "Текст в формате Markdown"
    page.scroll = ft.ScrollMode.AUTO

    async def handle_link_tap(e: ft.Event[ft.Markdown]):
        await page.launch_url(e.data)

    page.add(
        ft.SafeArea(
            content=ft.Markdown(
                value=sample,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link=handle_link_tap,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)