import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 7")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3", "Листинг 7.4",
         "Листинг 7.5", "Листинг 7.6", "Листинг 7.7", "Листинг 7.8",
         "Листинг 7.9", "Листинг 7.10", "Листинг 7.11", "Листинг 7.12",
         "Листинг 7.13", "Листинг 7.14", "Листинг 7.15",
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

    elif options == "Листинг 7.1":
        st.markdown('#### 📸 Элемент Bage👇')
        path = 'programs/Listing_7_1.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/types/badge/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.2":
        st.markdown('#### 📸 Элемент Bage👇')
        path = 'programs/Listing_7_2.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/types/badge/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.3":
        st.markdown('#### 📸 Элемент CircleAvatar👇')
        path = 'programs/Listing_7_3.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/circleavatar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.4":
        st.markdown('#### 📸 Элемент Icon👇')
        path = 'programs/Listing_7_4.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/icon/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.5":
        st.markdown('#### 📸 Элемент CupertinoActivityIndicator👇')
        path = 'programs/Listing_7_5.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/cupertinoactivityindicator/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.6":
        st.markdown('#### 📸 Элемент ProgressBar👇')
        path = 'programs/Listing_7_6.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/progressbar/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.7":
        st.markdown('#### 📸 Элемент ProgressRing👇')
        path = 'programs/Listing_7_7.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/progressring/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.8":
        st.markdown('#### 📸 Элемент ProgressRing👇')
        path = 'programs/Listing_7_8.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/progressring/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.9":
        st.markdown('#### 📸 Элемент Audio👇')
        path = 'programs/Listing_7_9.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/services/audio/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)


    elif options == "Листинг 7.10":
        st.markdown('#### 📸 Элемент Camera👇')
        path = 'programs/Listing_7_10.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/camera/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.11":
        st.markdown('#### 📸 Элемент Image👇')
        path = 'programs/Listing_7_11.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/image/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.12":
        st.markdown('#### 📸 Элемент Image👇')
        path = 'programs/Listing_7_12.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/image/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.13":
        st.markdown('#### 📸 Элемент Image👇')
        path = 'programs/Listing_7_13.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/image/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.14":
        st.markdown('#### 📸 Элемент Image👇')
        path = 'programs/Listing_7_14.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/image/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.15":
        st.markdown('#### 📸 Элемент Video👇')
        path = 'programs/Listing_7_15.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/video/',
                             label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)


