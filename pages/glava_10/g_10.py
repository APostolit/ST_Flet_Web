import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 10", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 10")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 10",
        ("Листинг 10.1", "Листинг 10.2", "Листинг 10.3", "Листинг 10.4", "Листинг 10.5",
         "Листинг 10.6", "Листинг 10.7", "Листинг 10.8", "Листинг 10.9", "Листинг 10.10",
         "Листинг 10.11", "Листинг 10.12", "Листинг 10.13", "Листинг 10.14", "Листинг 10.15",
         "Листинг 10.16", "Листинг 10.17", "Листинг 10.18", "Листинг 10.19", "Листинг 10.20",
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

    elif options == "Листинг 10.1":
        st.markdown('#### 📸 Элемент CupertinoNavigationBar👇')
        path = 'programs/Listing_10_1.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinonavigationbar',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.2":
        st.markdown('#### 📸 Элемент CupertinoNavigationBar👇')
        path = 'programs/Listing_10_2.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinonavigationbar',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.3":
        st.markdown('#### 📸 Элемент NavigationBar👇')
        path = 'programs/Listing_10_3.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/navigationbar',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.4":
        st.markdown('#### 📸 Элемент NavigationDrawer👇')
        path = 'programs/Listing_10_4.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/navigationdrawer/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.5":
        st.markdown('#### 📸 Элемент NavigationDrawer👇')
        path = 'programs/Listing_10_5.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/navigationdrawer/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.6":
        st.markdown('#### 📸 Элемент NavigationDrawer👇')
        path = 'programs/Listing_10_6.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/navigationdrawer/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.7":
        st.markdown('#### 📸 Элемент NavigationRail👇')
        path = 'programs/Listing_10_7.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/navigationrail/',
                             label='🛠️ Документация')
                st.page_link('https://flet.dev/docs/controls/navigationraildestination/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.8":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_8.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.9":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_9.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.10":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_10.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.11":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_11.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.12":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_12.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.13":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_13.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.14":
        st.markdown('#### 📸 Элемент Router👇')
        path = 'programs/Listing_10_14.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/router/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.15":
        st.markdown('#### 📸 Элемент View👇')
        path = 'programs/Listing_10_15.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
                # if st.button("🚀Выполнить код"):
                    # launch_flet(path)
            with col2:
                st.page_link('https://flet.dev/docs/controls/view/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.16":
        st.markdown('#### 📸 Элемент View👇')
        path = 'programs/Listing_10_16.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
                # if st.button("🚀Выполнить код"):
                    # launch_flet(path)
            with col2:
                st.page_link('https://flet.dev/docs/controls/view/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.17":
        st.markdown('#### 📸 Элемент View👇')
        path = 'programs/Listing_10_17.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/view/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.18":
        st.markdown('#### 📸 Элемент Column👇')
        path = 'programs/Listing_10_18.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
                # if st.button("🚀Выполнить код"):
                    # launch_flet(path)
            with col2:
                st.page_link('https://flet.dev/docs/controls/column/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.19":
        st.markdown('#### 📸 Элемент Column👇')
        path = 'programs/Listing_10_19.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
                # if st.button("🚀Выполнить код"):
                    # launch_flet(path)
            with col2:
                st.page_link('https://flet.dev/docs/controls/column/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 10.20":
        st.markdown('#### 📸 Элемент Column👇')
        path = 'programs/Listing_10_20.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/column/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)






