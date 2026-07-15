import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Dashboard")
st.caption("📈 Analyze student marks, attendance, departments, and performance.")

df = pd.read_csv("students.csv")

st.sidebar.header("🎛️ Dashboard Filters")

city = st.sidebar.selectbox(
    "🌍 Select City",
    ["All"] + list(df["city"].unique())
)

department = st.sidebar.selectbox(
    "🏢 Select Department",
    ["All"] + list(df["department"].unique())
)

filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == city
    ]

if department != "All":
    filtered_df = filtered_df[
        filtered_df["department"] == department
    ]

st.subheader("📌 Performance Overview")

total_students = len(filtered_df)
average_marks = filtered_df["marks"].mean()
highest_marks = filtered_df["marks"].max()
average_attendance = filtered_df["attendance"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👨‍🎓 Total Students",
    total_students
)

col2.metric(
    "📚 Average Marks",
    round(average_marks, 2)
)

col3.metric(
    "🏆 Highest Marks",
    highest_marks
)

col4.metric(
    "📅 Avg. Attendance",
    f"{round(average_attendance, 2)}%"
)

st.divider()

st.subheader("📋 Student Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📊 Average Marks by Department")

department_marks = filtered_df.groupby(
    "department"
)["marks"].mean()

st.bar_chart(department_marks)

st.divider()

st.subheader("🏆 Top 3 Performing Students")

top_students = filtered_df.sort_values(
    "marks",
    ascending=False
).head(3)

st.dataframe(
    top_students,
    use_container_width=True,
    hide_index=True
)

st.divider()

csv_data = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv_data,
    file_name="filtered_students.csv",
    mime="text/csv",
    use_container_width=True
)
