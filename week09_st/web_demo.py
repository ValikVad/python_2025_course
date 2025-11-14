import json
from datetime import datetime

import streamlit as st

JSON_PATH = "tasks.json"


def load_tasks():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def add_task(task: dict = None):
    if isinstance(task, dict):
        cur_tasks = load_tasks()
        cur_tasks.append(task)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(cur_tasks, f, indent=3)


def change_status_i_task():
    print("st session state", st.session_state)


list_tasks = []
st.title("TODO list")
tab1, tab2 = st.tabs(["Страница добавления задач", "Список актуальных задач"])
with tab1:
    st.subheader("В окне ниже введите задачу")
    task_name = st.text_area("Введите название задачи", height=30)
    task_description = st.text_area("Введите опизание задачи в этом окне", height=100)
    estimate = st.selectbox("Сколько часов займет задача", [0, 1, 2, 3, 4])
    # estimate = st.select_slider(label="kek slider", options= ,  value=[0, 1, 2, 3 ,4, 5])

    if st.button("Добавить задачу!"):
        try:
            add_task(
                {
                    "name": task_name,
                    "desc": task_description,
                    "est": estimate,
                    "status": "new",
                }
            )
        except Exception:
            st.write("Not succes")
with tab2:
    list_tasks = load_tasks()

    for id, val_i in enumerate(
        sorted(list_tasks, reverse=True, key=lambda x: x.get("est", 0))
    ):
        with st.container(border=True):
            title, description, estimate, status = st.columns([2, 2, 1, 1])
            title.write(val_i.get("name"))
            description.write(val_i.get("desc"))
            estimate.write(val_i.get("est"))
            status.selectbox(
                "",
                ["new", "inprogress", "done"],
                key=val_i,
                on_change=change_status_i_task,
                label_visibility="collapsed",
            )
    print("st session state before selectbox change", st.session_state)
