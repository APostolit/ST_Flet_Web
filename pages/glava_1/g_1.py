import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 1", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

st.header("👩🏻‍💻Листинги главы 1")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "Листинги главы 1",
        ("Листинг 1.1", "Листинг 1.2", "Листинг 1.3", "Листинг 1.4", "Листинг 1.5",),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)

with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 1.1":
        st.markdown('#### 📸 Первое приложение👇')
        path = 'programs/Listing_1_1.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 1.2":
        st.markdown('#### 📸 Элемент Column👇')
        path = 'programs/Listing_1_2.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/column', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 1.3":
        st.markdown('#### 📸 Элемент Row👇')
        path = 'programs/Listing_1_3.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/row', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 1.4":
        st.markdown('#### 📸 Элемент Container👇')
        path = 'programs/Listing_1_4.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/container', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 1.5":
        st.markdown('#### 📸 Элемент Page👇')
        path = 'programs/Listing_1_5.py'
        cont_bt = st.container(width=350)
        with cont_bt:
            col1, col2 = st.columns([1, 1])
            with col1:
                pass
            with col2:
                st.page_link('https://flet.dev/docs/controls/page', label='🛠️ Документация')
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)