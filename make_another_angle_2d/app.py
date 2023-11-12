import streamlit as st
from functions.one_2345 import One2345


if 'step_num' not in st.session_state:
    st.session_state.step_num = 1

if 'one_2345' not in st.session_state:
    one_2345 = One2345()
    st.session_state.one_2345 = one_2345

if 'bg_clipped' not in st.session_state:
    st.session_state.bg_clipped = False


st.title('2D to 3D')
st.header('Sample Image')
st.image('images/sample_image.png')

if st.button('背景切り抜き', key=0):
    st.session_state.one_2345.initial_process('images/sample_image.png')
    st.session_state.bg_clipped = True

if st.session_state.bg_clipped:
    st.image(st.session_state.one_2345.selected_path_list[0])
    if st.button('次のstepへ', key='next_step'):
        st.session_state.one_2345.generate_new()
        st.session_state.step_num = 2

if st.session_state.step_num == 2:
    if len(st.session_state.one_2345.generative_path_list):
        st.header('画像選択')
        st.write('建物の画像として相応しいと思うものは追加, 異なるものは削除してください')
        st.image(st.session_state.one_2345.generative_path_list[0])
        col1, col2 = st.columns(2)
        with col1:
            if st.button('選択'):
                print('選択')
        with col2:
            if st.button('削除'):
                st.session_state.one_2345.remove_select()
        st.session_state.one_2345.add_select()

    else:
        if len(st.session_state.one_2345.selected_path_list) < 20:
            st.session_state.one_2345.remove_select()
            st.session_state.one_2345.generate_new()
            st.experimental_rerun()

        else:
            st.session_state.step_num = 3
            st.experimental_rerun()

if st.session_state.step_num == 3:
    for path in st.session_state.one_2345.selected_path_list:
        st.image(path)

