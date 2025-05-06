import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ---------------- AUTH SECTION ---------------- #
USER_CREDENTIALS = {
    "admin": "admin123",
    "manager": "manager123"
}

# Sidebar login form
with st.sidebar:
    st.header("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.button("Login")

# Login logic
if login:
    if USER_CREDENTIALS.get(username) == password:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.success(f"Welcome, {username}!")
    else:
        st.error("Invalid credentials")
        st.stop()

if not st.session_state.get("logged_in"):
    st.warning("Please login to continue.")
    st.stop()

# ---------------- DATABASE CONNECTION ---------------- #
try:
    engine = create_engine("mysql+mysqlconnector://root@localhost/employeeslist")
    conn = engine.connect()
    st.sidebar.success("✅ Connected to MySQL")
except Exception as e:
    st.sidebar.error(f"❌ DB Connection Failed: {e}")
    st.stop()

# ---------------- MAIN UI ---------------- #
st.title("🏢 Company Employee Database")

# --- Insert New Employee ---
with st.expander("➕ Add New Employee"):
    with st.form("add_employee_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        dept = st.selectbox("Department", ["HR", "IT", "Sales", "Finance" , "Admin" ])
        submit = st.form_submit_button("Insert")

        if submit:
            insert_query = text("""
                INSERT INTO employee (name, age, department)
                VALUES (:n, :a, :d)
            """)
            conn.execute(insert_query, {"n": name, "a": age, "d": dept})
            conn.commit()
            st.success("✅ Employee added successfully!")

# --- Filter and Display Employees ---
st.subheader("📋 View Employees")

filter_dept = st.selectbox("Filter by Department", ["All", "HR", "IT", "Sales", "Finance" , "Admin" ])
if filter_dept == "All":
    query = "SELECT * FROM employee"
    df = pd.read_sql(query, conn)
else:
    query = text("SELECT * FROM employee WHERE department = :dept")
    df = pd.read_sql(query, conn, params={"dept": filter_dept})

st.dataframe(df)

# Close connection
conn.close()
