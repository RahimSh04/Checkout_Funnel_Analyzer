"""Public dashboard metrics.

This repo keeps the hosted app lightweight by using the final computed results
directly. The original CSV cleaning + SQLite pipeline is preserved below as
commented reference code because the raw CSV (~396 MB) and generated DB
(~117 MB) are too large to ship in the public repo/deployment.
"""

FINAL_DASHBOARD_DATA = {
    "view_users": 358212,
    "cart_users": 83458,
    "purchase_users": 25613,
    "cart_conversion": 0.23298493629470815,
    "purchase_conversion": 0.30689688226413286,
    "overall_conversion": 0.07150235056335355,
    "total_users": 369452,
    "returning_users": 186937,
    "retention_rate": 0.5059845392635579,
}


# Original data pipeline kept for code review/reference only.
# The live app does not execute this block because the source files are too
# large for the public repo and lightweight Streamlit deployment.
#
# import streamlit as st
# import sqlite3
# import pandas as pd
# from explore_data import load_clean_events
#
# @st.cache_data
# def load_dashboard_data():
#     conn = sqlite3.connect("funnel_analysis.db")
#
#     df = load_clean_events()
#     df.to_sql("events", conn, if_exists="replace", index=False)
#     conn.commit()
#
#     funnel_query = """
#     WITH funnel_events AS (
#         SELECT
#             user_id,
#             event_type,
#             MIN(timestamp) AS first_timestamp
#         FROM events
#         GROUP BY user_id, event_type
#     ),
#     funnel_counts AS (
#         SELECT
#             COUNT(DISTINCT CASE WHEN event_type = 'view' THEN user_id END) AS view_users,
#             COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS cart_users,
#             COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
#         FROM funnel_events
#     )
#     SELECT
#         view_users,
#         cart_users,
#         purchase_users,
#         1.0 * cart_users / NULLIF(view_users, 0) AS cart_conversion,
#         1.0 * purchase_users / NULLIF(cart_users, 0) AS purchase_conversion,
#         1.0 * purchase_users / NULLIF(view_users, 0) AS overall_conversion
#     FROM funnel_counts;
#     """
#
#     retention_query = """
#     WITH first_activity AS (
#         SELECT
#             user_id,
#             MIN(timestamp) AS first_timestamp
#         FROM events
#         GROUP BY user_id
#     ),
#     returning_users AS (
#         SELECT DISTINCT e.user_id
#         FROM events e
#         JOIN first_activity f
#             ON e.user_id = f.user_id
#         WHERE e.timestamp > f.first_timestamp
#     )
#     SELECT
#         (SELECT COUNT(DISTINCT user_id) FROM events) AS total_users,
#         COUNT(*) AS returning_users,
#         1.0 * COUNT(*) / NULLIF((SELECT COUNT(DISTINCT user_id) FROM events), 0) AS retention_rate
#     FROM returning_users;
#     """
#
#     funnel_df = pd.read_sql_query(funnel_query, conn)
#     retention_df = pd.read_sql_query(retention_query, conn)
#
#     conn.close()
#
#     return funnel_df, retention_df
#
# def get_dashboard_data():
#     funnel_df, retention_df = load_dashboard_data()
#     view_users = funnel_df.loc[0, "view_users"]
#     cart_users = funnel_df.loc[0, "cart_users"]
#     purchase_users = funnel_df.loc[0, "purchase_users"]
#     cart_conversion = funnel_df.loc[0, "cart_conversion"]
#     purchase_conversion = funnel_df.loc[0, "purchase_conversion"]
#     overall_conversion = funnel_df.loc[0, "overall_conversion"]
#     total_users = retention_df.loc[0, "total_users"]
#     returning_users = retention_df.loc[0, "returning_users"]
#     retention_rate = retention_df.loc[0, "retention_rate"]
#     return {
#         "view_users": view_users,
#         "cart_users": cart_users,
#         "purchase_users": purchase_users,
#         "cart_conversion": cart_conversion,
#         "purchase_conversion": purchase_conversion,
#         "overall_conversion": overall_conversion,
#         "total_users": total_users,
#         "returning_users": returning_users,
#         "retention_rate": retention_rate,
#     }


def get_dashboard_data():
    """Return precomputed metrics for the public Streamlit build."""
    return FINAL_DASHBOARD_DATA.copy()
