import streamlit as st
import pandas as pd

def home_page():
    st.title('Clinky.Inc')
    st.write('Сайт для работы со снимками КТ печени. Здесь вы можете загрузить ваш файл, а наша обученная нейросеть проверит снимки.')
    if st.button('Перейти к работе'):
        st.session_state['page'] = 'work'

# Функция для страницы работы
def work_page():
    st.header('Clinky.Inc')
    st.subheader('Здесь вы можете загрузить свои файлы')

    uploaded_file = st.file_uploader('Загрузить файл', type=['csv', 'xlsx', 'txt'])

    if st.button('Посмотреть загруженные файлы'):
        if uploaded_file is not None:
            if uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.write(df)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(uploaded_file)
                st.write(df)
            elif uploaded_file.type == "text/plain":
                content = uploaded_file.getvalue()
                st.text(content)
        else:
            st.warning('Файл не загружен. Пожалуйста, загрузите файл.')

    if st.button('Запустить программу'):
        if uploaded_file is not None:
            st.success('Программа запущена!')
        else:
            st.error('Для начала загрузите ваш файл!')

def info_page():
    st.title('Информация о проекте')
    st.write('Работу подготовили: Колмаков К.В. и Мищенко Н.К. Сайт разработан в ходе проекта командой Clinky.Inc')

def main():
    # Инициализация состояния страницы
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    if 'prev_page' not in st.session_state:
        st.session_state['prev_page'] = None

    st.sidebar.title('Навигация')
    if st.sidebar.button('Главная страница'):
        st.session_state['prev_page'] = st.session_state['page']
        st.session_state['page'] = 'home'
    if st.sidebar.button('Информация'):
        st.session_state['prev_page'] = st.session_state['page']
        st.session_state['page'] = 'info'
    if st.sidebar.button('Вернуться назад') and st.session_state['prev_page']:
        st.session_state['page'], st.session_state['prev_page'] = st.session_state['prev_page'], st.session_state['page']

    # Отображение выбранной страницы
    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'work':
        work_page()
    elif st.session_state['page'] == 'info':
        info_page()


if __name__ == '__main__':
    main()



# streamlit run app.py
