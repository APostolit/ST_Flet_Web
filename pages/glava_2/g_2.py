# https://python-code-online.pages.dev/ru/
import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         "Листинг 2.5", "Листинг 2.6", "Листинг 2.7", "Листинг 2.8",
         "Листинг 2.9", "Листинг 2.10", "Листинг 2.11", "Листинг 2.12",
         "Листинг 2.13", "Листинг 2.14", "Листинг 2.15", "Листинг 2.16",
         "Листинг 2.17", "Листинг 2.18", "Листинг 2.19", "Листинг 2.20",
         "Листинг 2.21", "Листинг 2.22", "Листинг 2.23", "Листинг 2.24",
         "Листинг 2.25", "Листинг 2.26", "Листинг 2.27", "Листинг 2.28",
         "Листинг 2.29", "Листинг 2.30", "Листинг 2.31", "Листинг 2.32",
         "Листинг 2.33", "Листинг 2.34", "Листинг 2.35", "Листинг 2.36",
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=900)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 2.1":
        st.markdown('#### 📸 Элемент AutofillGroup👇')
        path = 'programs/Listing_2_1.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/autofillgroup', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.2":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_2.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)


    elif options == "Листинг 2.3":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_3.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)


    elif options == "Листинг 2.4":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_4.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.5":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_5.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.6":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_6.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.7":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_7.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.8":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_8.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.9":
        st.markdown('#### 📸 Элемент Canvas👇')
        path = 'programs/Listing_2_9.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/canvas', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.10":
        st.markdown('#### 📸 Элемент Card👇')
        path = 'programs/Listing_2_10.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/card', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.11":
        st.markdown('#### 📸 Элемент Card👇')
        path = 'programs/Listing_2_11.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/card', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.12":
        st.markdown('#### 📸 Элемент CodeEditor👇')
        path = 'programs/Listing_2_12.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://pypi.org/project/flet-code-editor/', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.13":
        st.markdown('#### 📸 Элемент CodeEditor👇')
        path = 'programs/Listing_2_13.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://pypi.org/project/flet-code-editor/', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.14":
        st.markdown('#### 📸 Элемент CodeEditor👇')
        path = 'programs/Listing_2_14.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://pypi.org/project/flet-code-editor/', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.15":
        st.markdown('#### 📸 Элемент CupertinoListTile👇')
        path = 'programs/Listing_2_15.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinolisttile', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.16":
        st.markdown('#### 📸 Элемент CupertinoTextField👇')
        path = 'programs/Listing_2_16.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinotextfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.17":
        st.markdown('#### 📸 Элемент ListTile👇')
        path = 'programs/Listing_2_17.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/listtile', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.18":
        st.markdown('#### 📸 Элемент ListView👇')
        path = 'programs/Listing_2_18.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/listview', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.19":
        st.markdown('#### 📸 Элемент ListView👇')
        path = 'programs/Listing_2_19.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/listview', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.20":
        st.markdown('#### 📸 Элемент Markdown👇')
        path = 'programs/Listing_2_20.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/markdown', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.21":
        st.markdown('#### 📸 Элемент Markdown👇')
        path = 'programs/Listing_2_21.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/markdown', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.22":
        st.markdown('#### 📸 Элемент Screenshot👇')
        path = 'programs/Listing_2_22.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/screenshot', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.23":
        st.markdown('#### 📸 Элемент ShaderMask👇')
        path = 'programs/Listing_2_23.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/shadermask', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.24":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_24.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.25":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_25.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.26":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_26.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.27":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_27.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.28":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_28.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.29":
        st.markdown('#### 📸 Элемент Text👇')
        path = 'programs/Listing_2_29.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/text', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.30":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_30.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.31":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_31.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.32":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_32.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.33":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_33.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.34":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_34.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.35":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_35.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 2.36":
        st.markdown('#### 📸 Элемент TextField👇')
        path = 'programs/Listing_2_36.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/textfield', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)