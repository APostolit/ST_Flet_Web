import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 6")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 6",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4",
         "Листинг 6.5", "Листинг 6.6", "Листинг 6.7", "Листинг 6.8",
         "Листинг 6.9", "Листинг 6.10", "Листинг 6.11", "Листинг 6.12",
         "Листинг 6.13", "Листинг 6.14", "Листинг 6.15", "Листинг 6.16",
          ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 6.1":
        st.markdown('#### 📸 Элемент ContextMenu👇')
        path = 'programs/Listing_6_1.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/contextmenu/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.2":
        st.markdown('#### 📸 Элемент ContextMenu👇')
        path = 'programs/Listing_6_2.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/contextmenu/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.3":
        st.markdown('#### 📸 Элемент ContextMenu👇')
        path = 'programs/Listing_6_3.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinocontextmenu/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.4":
        st.markdown('#### 📸 Элемент MenuBar👇')
        path = 'programs/Listing_6_4.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/menubar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.5":
        st.markdown('#### 📸 Элемент MenuBar👇')
        path = 'programs/Listing_6_5.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/menubar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.6":
        st.markdown('#### 📸 Элемент MenuItemButton👇')
        path = 'programs/Listing_6_6.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/menuitembutton/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.7":
        st.markdown('#### 📸 Элемент MenuItemButton👇')
        path = 'programs/Listing_6_7.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/menuitembutton/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.8":
        st.markdown('#### 📸 Элемент PopupMenuButton👇')
        path = 'programs/Listing_6_8.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/popupmenubutton/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.9":
        st.markdown('#### 📸 Элемент SubmenuButton👇')
        path = 'programs/Listing_6_9.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/submenubutton/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.10":
        st.markdown('#### 📸 Элемент AppBar👇')
        path = 'programs/Listing_6_10.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/appbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.11":
        st.markdown('#### 📸 Элемент AppBar👇')
        path = 'programs/Listing_6_11.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/appbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.12":
        st.markdown('#### 📸 Элемент AppBar👇')
        path = 'programs/Listing_6_12.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/appbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.13":
        st.markdown('#### 📸 Элемент BottomAppBar👇')
        path = 'programs/Listing_6_13.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/bottomappbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.14":
        st.markdown('#### 📸 Элемент BottomAppBar👇')
        path = 'programs/Listing_6_14.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/bottomappbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.15":
        st.markdown('#### 📸 Элемент BottomAppBar👇')
        path = 'programs/Listing_6_15.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/bottomappbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 6.16":
        st.markdown('#### 📸 Элемент CupertinoBottomSheet👇')
        path = 'programs/Listing_6_16.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinobottomsheet/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)