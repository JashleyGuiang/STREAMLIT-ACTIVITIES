import streamlit as st

# Sidebar
st.sidebar.title("🔧 Topics")
topic = st.sidebar.radio("Choose a topic to explore:", [
    "Introduction", 
    "Components", 
    "Benefits", 
    "Challenges", 
    "Use Cases"
])

# Header
st.title("🏗️ Data Warehousing & Enterprise Data Management")
st.markdown("Explore comprehensive insights into how organizations manage, store, and govern data for business intelligence and strategic decisions.")

# Tabs for sub-categories
tab1, tab2, tab3, tab4 = st.tabs([
    "📦 Data Warehousing", 
    "🏢 Enterprise Data Management",
    "📊 Analytics & Reporting",
    "🔐 Data Governance"
])

with tab1:
    st.header("📦 Data Warehousing")

    if topic == "Introduction":
        st.subheader("What is a Data Warehouse?")
        st.markdown("""
        A **Data Warehouse (DW)** is a centralized repository designed to store integrated data from various sources 
        to support **business intelligence (BI)**, reporting, and decision-making. It is optimized for querying and analysis 
        rather than transaction processing.
        
        Modern data warehouses consolidate structured and semi-structured data, enabling **historical analysis**, 
        **trend discovery**, and **performance tracking** over time.
        """)

        with st.expander("Why not just use a regular database?"):
            st.write("""
            While operational databases (OLTP) are optimized for real-time transactions and updates, 
            **data warehouses (OLAP)** are optimized for **analytical queries and aggregations**. 
            They typically involve large-scale data, complex queries, and historical datasets.
            """)

        with st.expander("📘 Learn More"):
            st.markdown("👉 Star vs Snowflake Schema, Data Marts, ETL/ELT processes...")

    elif topic == "Components":
        st.subheader("Core Components of a Data Warehouse")
        st.write("""
        - **Data Sources**: ERP systems, CRMs, APIs  
        - **ETL/ELT Tools**: Extract, Transform, Load processes  
        - **Staging Area**: Temporary storage for raw data  
        - **Data Storage**: Fact and dimension tables  
        - **Presentation Layer**: BI tools, dashboards  
        """)

    elif topic == "Benefits":
        st.subheader("Benefits of Data Warehousing")
        st.write("""
        - Enhanced business intelligence  
        - Faster decision making  
        - Consistent data quality  
        - Historical data analysis  
        - Improved performance for analytical queries  
        """)

    elif topic == "Challenges":
        st.subheader("Challenges in Data Warehousing")
        st.write("""
        - High implementation costs  
        - Complex integration  
        - Data latency and freshness issues  
        - Maintenance overhead  
        - Scalability concerns with traditional DWs  
        """)

    elif topic == "Use Cases":
        st.subheader("Real-World Use Cases of Data Warehousing")
        st.markdown("""
        ✅ **Retail & E-commerce**  
        Track sales performance, customer behavior, and inventory management using centralized historical data.

        ✅ **Healthcare**  
        Analyze patient records, treatment outcomes, and operational efficiency across facilities.

        ✅ **Banking & Finance**  
        Monitor transactions, detect fraud patterns, and generate compliance reports.

        ✅ **Manufacturing**  
        Optimize supply chains, monitor equipment performance, and forecast demand.

        ✅ **Telecommunications**  
        Analyze customer usage data to reduce churn and improve network optimization.
        """)

        with st.expander("🔍 More Industry Examples"):
            st.markdown("""
            - **Logistics**: Route optimization and delivery time analysis  
            - **Education**: Student performance tracking and institutional reporting  
            - **Energy**: Consumption analysis and predictive maintenance  
            """)

with tab2:
    st.header("🏢 Enterprise Data Management")
    st.markdown("""
    Enterprise Data Management (EDM) ensures that the organization's data is accurate, accessible, and secure.  
    It includes **data governance**, **metadata management**, **master data management**, and **data quality control**.
    """)

# Tab 3: Analytics & Reporting
with tab3:
    st.header("📊 Analytics & Reporting")
    st.markdown("""
    Data warehouses are the backbone of analytics and reporting platforms. They allow users to:
    - Build **dashboards** and **reports** for KPI tracking  
    - Enable **self-service BI** for non-technical users  
    - Perform **advanced analytics** using machine learning and statistical tools  
    - Use **predictive modeling** for sales forecasting, churn prediction, etc.  
    """)

    with st.expander("📈 Common Tools"):
        st.markdown("""
        - Power BI  
        - Tableau  
        - Looker  
        - Apache Superset  
        """)

# Tab 4: Data Governance
with tab4:
    st.header("🔐 Data Governance")
    st.markdown("""
    Data Governance refers to the overall management of data availability, usability, integrity, and security.  
    It includes:
    - **Data stewardship**: Assigning roles and responsibilities  
    - **Policy enforcement**: Ensuring compliance with standards and regulations  
    - **Access control**: Restricting access to sensitive data  
    - **Audit and logging**: Monitoring data usage  
    """)

    with st.expander("🛡️ Regulations to Consider"):
        st.markdown("""
        - GDPR (General Data Protection Regulation)  
        - HIPAA (Health Insurance Portability and Accountability Act)  
        - CCPA (California Consumer Privacy Act)  
        """)
