import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Checkout Funnel Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
    html {
        scroll-behavior: smooth;
    }

    :root {
        --bg: #f7f9fc;
        --panel: rgba(255, 255, 255, 0.9);
        --panel-strong: #ffffff;
        --text: #0a2540;
        --muted: #5b6b7d;
        --line: rgba(10, 37, 64, 0.1);
        --accent: #635bff;
        --accent-deep: #4338ca;
        --accent-soft: rgba(99, 91, 255, 0.1);
        --soft-blue: rgba(15, 123, 255, 0.1);
        --shadow: 0 24px 60px rgba(10, 37, 64, 0.08);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(99, 91, 255, 0.14), transparent 26%),
            radial-gradient(circle at top right, rgba(15, 123, 255, 0.12), transparent 24%),
            linear-gradient(180deg, #fbfdff 0%, #f7f9fc 100%);
        color: var(--text);
    }

    header[data-testid="stHeader"] {
        display: none;
    }

    div[data-testid="stToolbar"] {
        display: none;
    }

    div[data-testid="stDecoration"] {
        display: none;
    }

    div.block-container {
        max-width: 1220px;
        padding-top: 0.85rem;
        padding-bottom: 3rem;
    }

    .nav-shell {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 0.9rem 1.25rem;
        box-shadow: var(--shadow);
        backdrop-filter: blur(8px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.25rem;
    }

    .nav-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text);
        letter-spacing: -0.01em;
    }

    .nav-actions {
        display: flex;
        justify-content: flex-end;
        gap: 0.55rem;
        flex-wrap: wrap;
    }

    .nav-pill {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border: 1px solid var(--line);
        color: var(--text);
        background: rgba(255, 255, 255, 0.85);
        border-radius: 999px;
        padding: 0.46rem 0.85rem;
        font-size: 0.83rem;
        font-weight: 500;
        text-decoration: none;
        transition: transform 180ms ease, background 180ms ease, color 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
        box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.45);
    }

    .nav-pill:link,
    .nav-pill:visited,
    .nav-pill:active {
        color: var(--text);
        text-decoration: none;
    }

    .nav-pill:hover {
        transform: translateY(-2px) scale(1.02);
        color: white;
        background: linear-gradient(135deg, #0f7bff, var(--accent));
        border-color: transparent;
        box-shadow: 0 14px 28px rgba(99, 91, 255, 0.2);
    }

    .hero-shell {
        background:
            linear-gradient(135deg, rgba(99, 91, 255, 0.08), rgba(255, 255, 255, 0.72) 30%),
            linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.82));
        border: 1px solid var(--line);
        border-radius: 34px;
        padding: 1.8rem 1.8rem 1.9rem;
        box-shadow: var(--shadow);
        backdrop-filter: blur(8px);
        margin-bottom: 0.5rem;
    }

    .hero-eyebrow {
        display: inline-block;
        font-size: 0.76rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--accent);
        background: var(--accent-soft);
        padding: 0.46rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    .hero-title {
        margin: 0;
        font-size: 3.25rem;
        line-height: 0.98;
        letter-spacing: -0.04em;
        color: var(--text);
        max-width: 760px;
    }

    .hero-copy {
        margin: 1rem 0 0;
        max-width: 720px;
        color: var(--muted);
        font-size: 1.02rem;
        line-height: 1.6;
    }

    .pill-row {
        display: flex;
        gap: 0.65rem;
        flex-wrap: wrap;
        margin-top: 1.25rem;
    }

    .pill {
        border: 1px solid rgba(99, 91, 255, 0.12);
        color: var(--accent-deep);
        background: rgba(255, 255, 255, 0.9);
        border-radius: 999px;
        padding: 0.5rem 0.9rem;
        font-size: 0.84rem;
    }

    .section-heading {
        margin-top: 0.65rem;
        margin-bottom: 0.5rem;
        font-size: 1.85rem;
        letter-spacing: -0.03em;
        font-weight: 700;
        color: var(--text);
    }

    .section-copy {
        margin-top: 0;
        margin-bottom: 1.15rem;
        color: var(--muted);
        font-size: 0.98rem;
    }

    .kpi-card {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 1.05rem 1.05rem 1.1rem;
        box-shadow: var(--shadow);
        min-height: 148px;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }

    .kpi-card:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 0 28px 60px rgba(10, 37, 64, 0.14);
        border-color: rgba(99, 91, 255, 0.2);
    }

    .kpi-label {
        color: var(--muted);
        font-size: 0.84rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.9rem;
    }

    .kpi-value {
        color: var(--text);
        font-size: 2rem;
        line-height: 1;
        font-weight: 700;
        margin-bottom: 0.7rem;
    }

    .kpi-note {
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.45;
    }

    .panel-shell {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 28px;
        padding: 1.15rem 1.15rem 1.2rem;
        box-shadow: var(--shadow);
        height: 100%;
    }

    .panel-title {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.45rem;
    }

    .panel-copy {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.55;
        margin-bottom: 0.85rem;
    }

    .chart-placeholder {
        border: 1.5px dashed rgba(102, 112, 133, 0.36);
        border-radius: 22px;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(236, 243, 255, 0.78));
        padding: 1.2rem;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .chart-placeholder.small {
        min-height: 240px;
    }

    .funnel-shell {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 28px;
        padding: 1.15rem 1.15rem 1.25rem;
        box-shadow: var(--shadow);
        height: 100%;
    }

    .funnel-stage {
        margin-top: 1rem;
    }

    .funnel-stage:first-of-type {
        margin-top: 0.3rem;
    }

    .funnel-line {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        gap: 1rem;
        margin-bottom: 0.45rem;
    }

    .funnel-step {
        color: var(--text);
        font-size: 0.96rem;
        font-weight: 700;
    }

    .funnel-users {
        color: var(--muted);
        font-size: 0.9rem;
        font-weight: 600;
    }

    .funnel-track {
        width: 100%;
        background: rgba(99, 91, 255, 0.08);
        border-radius: 999px;
        padding: 0.35rem 0;
    }

    .funnel-fill {
        min-width: 96px;
        margin: 0 auto;
        border-radius: 999px;
        padding: 0.78rem 1rem;
        background: linear-gradient(135deg, var(--accent), #0f7bff);
        box-shadow: 0 12px 28px rgba(99, 91, 255, 0.16);
        text-align: center;
        color: white;
        font-weight: 700;
        font-size: 0.88rem;
        letter-spacing: 0.01em;
    }

    .funnel-detail {
        color: var(--muted);
        font-size: 0.88rem;
        margin-top: 0.45rem;
        text-align: center;
    }

    .analysis-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin: 0.1rem 0 0.95rem;
    }

    .analysis-badge {
        background: rgba(99, 91, 255, 0.08);
        color: var(--accent-deep);
        border: 1px solid rgba(99, 91, 255, 0.12);
        border-radius: 999px;
        padding: 0.42rem 0.78rem;
        font-size: 0.82rem;
        font-weight: 600;
    }

    .retention-shell {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 28px;
        padding: 1.15rem 1.15rem 1.25rem;
        box-shadow: var(--shadow);
        height: 100%;
    }

    .retention-row {
        margin-top: 1rem;
    }

    .retention-row:first-of-type {
        margin-top: 0.4rem;
    }

    .retention-line {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        gap: 1rem;
        margin-bottom: 0.45rem;
    }

    .retention-label {
        color: var(--text);
        font-size: 0.96rem;
        font-weight: 700;
    }

    .retention-users {
        color: var(--muted);
        font-size: 0.9rem;
        font-weight: 600;
    }

    .retention-track {
        width: 100%;
        height: 20px;
        background: rgba(10, 37, 64, 0.06);
        border-radius: 999px;
        overflow: hidden;
        position: relative;
    }

    .retention-fill {
        height: 100%;
        border-radius: 999px;
    }

    .retention-fill.total {
        background: linear-gradient(135deg, #0f7bff, #635bff);
    }

    .retention-fill.returning {
        background: linear-gradient(135deg, #1db954, #0d9f6e);
    }

    .retention-fill.nonreturning {
        background: linear-gradient(135deg, #ff6b6b, #e63946);
    }

    .retention-detail {
        color: var(--muted);
        font-size: 0.88rem;
        margin-top: 0.45rem;
    }

    .retention-summary {
        margin-top: 1.15rem;
        padding-top: 0.95rem;
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.9rem;
        line-height: 1.55;
    }

    .placeholder-title {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.45rem;
    }

    .placeholder-copy {
        max-width: 440px;
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.92rem;
    }

    .insight-list {
        margin: 0;
        padding-left: 1.05rem;
        color: var(--text);
    }

    .insight-list li {
        margin-bottom: 0.7rem;
        line-height: 1.55;
    }

    .footer-shell {
        background: rgba(255, 255, 255, 0.86);
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 1rem 1.25rem;
        box-shadow: var(--shadow);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        min-height: 76px;
    }

    .footer-side {
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.45;
    }

    .footer-center {
        text-align: center;
        color: var(--text);
        font-size: 0.96rem;
        font-weight: 700;
        letter-spacing: -0.01em;
    }

    .footer-link-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.95);
        color: var(--text);
        min-width: 270px;
        padding: 0.72rem 1.15rem;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.45);
        transition: transform 180ms ease, background 180ms ease, color 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
        text-decoration: none;
    }

    .footer-link-button:link,
    .footer-link-button:visited,
    .footer-link-button:active {
        color: var(--text);
        text-decoration: none;
    }

    .footer-link-button:hover {
        transform: translateY(-2px) scale(1.02);
        color: white;
        background: linear-gradient(135deg, #0f7bff, var(--accent));
        border-color: transparent;
        box-shadow: 0 14px 28px rgba(99, 91, 255, 0.2);
    }

    .footer-actions {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 0.55rem;
        flex-wrap: wrap;
    }

    .footer-text {
        color: var(--muted);
        font-size: 0.84rem;
        font-weight: 600;
        margin-right: 0.2rem;
    }

    .footer-logo {
        width: 40px;
        height: 40px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(99, 91, 255, 0.08);
        border: 1px solid rgba(99, 91, 255, 0.12);
        border-radius: 999px;
        transition: transform 180ms ease, box-shadow 180ms ease;
    }

    .footer-logo:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 26px rgba(99, 91, 255, 0.14);
    }

    .footer-logo img {
        width: 18px;
        height: 18px;
    }

    .footer-text {
        color: var(--muted);
        font-size: 0.84rem;
        font-weight: 600;
        margin-right: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from main import get_dashboard_data

data = get_dashboard_data()

funnel_chart_data = {
    "Step": ["View", "Added to Cart", "Purchased"],
    "Users": [data["view_users"], data["cart_users"], data["purchase_users"]]
}

funnel_chart_df = pd.DataFrame(funnel_chart_data)


def format_count(value) -> str:
    return f"{int(value):,}"


def format_percent(value) -> str:
    return f"{float(value):.2%}"


display_data = {
    "total_users": format_count(data["total_users"]),
    "view_users": format_count(data["view_users"]),
    "purchase_users": format_count(data["purchase_users"]),
    "overall_conversion": format_percent(data["overall_conversion"]),
    "cart_users": format_count(data["cart_users"]),
    "returning_users": format_count(data["returning_users"]),
    "retention_rate": format_percent(data["retention_rate"]),
    "cart_conversion": format_percent(data["cart_conversion"]),
    "purchase_conversion": format_percent(data["purchase_conversion"]),
}

non_returning_users = max(int(data["total_users"]) - int(data["returning_users"]), 0)
display_data["non_returning_users"] = format_count(non_returning_users)
non_returning_users_percentage = format_percent(non_returning_users / int(data["total_users"]))

view_to_cart_dropoff = 1 - float(data["cart_conversion"])
cart_to_purchase_dropoff = 1 - float(data["purchase_conversion"])

if view_to_cart_dropoff >= cart_to_purchase_dropoff:
    largest_dropoff_label = "View -> Add to Cart"
    largest_dropoff_value = view_to_cart_dropoff
else:
    largest_dropoff_label = "Add to Cart -> Purchase"
    largest_dropoff_value = cart_to_purchase_dropoff

additional_purchases_if_checkout_improves = round(float(data["purchase_users"]) * 0.10)

funnel_insights = [
    f"Largest drop-off occurs at {largest_dropoff_label} ({format_percent(largest_dropoff_value)}).",
    f"Only {format_percent(data['overall_conversion'])} of viewers complete purchase.",
    f"If checkout conversion improves by 10%, purchases rise by about {format_count(additional_purchases_if_checkout_improves)}.",
]

retention_insights = [
    f"Total number of returning users equals {format_count(data['returning_users'])}.",
    f"Approximately {non_returning_users_percentage} of users do not return."
]


def render_kpi_card(label: str, value: str, note: str) -> None:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chart_placeholder(title: str, copy: str, small: bool = False) -> None:
    size_class = "small" if small else ""
    st.markdown(
        f"""
        <div class="chart-placeholder {size_class}">
            <div class="placeholder-title">{title}</div>
            <div class="placeholder-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel_title(title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="panel-title">{title}</div>
        <div class="panel-copy">{copy}</div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_panel(title: str, copy: str, bullets: list[str]) -> None:
    bullet_markup = "".join(f"<li>{item}</li>" for item in bullets)
    st.markdown(
        f"""
        <div class="panel-shell">
            <div class="panel-title">{title}</div>
            <div class="panel-copy">{copy}</div>
            <ul class="insight-list">
                {bullet_markup}
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_funnel_panel() -> None:
    stage_rows = [
        ("View", data["view_users"], "Starting point of the funnel"),
        ("Add to Cart", data["cart_users"], f"{display_data['cart_conversion']} progress from view"),
        ("Purchase", data["purchase_users"], f"{display_data['purchase_conversion']} progress from cart"),
    ]

    max_users = max(users for _, users, _ in stage_rows)
    stage_markup = ""

    for step, users, detail in stage_rows:
        width_percent = (users / max_users) * 100 if max_users else 0
        stage_markup += f"""
        <div class="funnel-stage">
            <div class="funnel-line">
                <div class="funnel-step">{step}</div>
                <div class="funnel-users">{format_count(users)} users</div>
            </div>
            <div class="funnel-track">
                <div class="funnel-fill" style="width: {width_percent:.1f}%;">
                    {format_count(users)}
                </div>
            </div>
            <div class="funnel-detail">{detail}</div>
        </div>
        """

    st.markdown(
        f"""
        <div class="funnel-shell">
            <div class="panel-title">Funnel Flow</div>
            <div class="panel-copy">
                This view turns your three funnel steps into a shrinking progression so the drop-offs are immediately visible.
            </div>
            {stage_markup}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_retention_panel() -> None:
    total_users = int(data["total_users"])
    returning_users = int(data["returning_users"])

    stage_rows = [
        ("Total Users", total_users, 100.0, "total"),
        ("Returning Users", returning_users, float(data["retention_rate"]) * 100, "returning"),
        (
            "Non-returning Users",
            non_returning_users,
            (non_returning_users / total_users * 100) if total_users else 0,
            "nonreturning",
        ),
    ]

    stage_markup = ""
    for label, users, width_percent, fill_class in stage_rows:
        stage_markup += f"""
        <div class="retention-row">
            <div class="retention-line">
                <div class="retention-label">{label}</div>
                <div class="retention-users">{format_count(users)} users</div>
            </div>
            <div class="retention-track">
                <div class="retention-fill {fill_class}" style="width: {max(width_percent, 3):.1f}%;"></div>
            </div>
            <div class="retention-detail">{width_percent:.1f}% of total users</div>
        </div>
        """

    st.markdown(
        f"""
        <div class="retention-shell">
            <div class="panel-title">Retention View</div>
            <div class="panel-copy">
                A horizontal comparison of the full user base, the users who returned later, and the share that did not come back.
            </div>
            {stage_markup}
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="nav-shell">
        <div class="nav-title">Checkout Funnel Analyzer</div>
        <div class="nav-actions">
            <a class="nav-pill" href="#overview-section">Overview</a>
            <a class="nav-pill" href="#funnel-section">Funnel</a>
            <a class="nav-pill" href="#retention-section">Retention</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="overview-section"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero-shell">
        <div class="hero-eyebrow">E-commerce analytics dashboard</div>
        <h1 class="hero-title">Find the friction between first view and final purchase.</h1>
        <p class="hero-copy">
            A clean dashboard for checking how users progress through the checkout funnel,
            where the biggest losses happen, and whether customers come back after their
            first activity.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown('<div class="section-heading">KPI Cards</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">Top-line metrics for the dashboard. Replace the placeholder values with your real results.</div>',
    unsafe_allow_html=True,
)

kpi_1, kpi_2, kpi_3, kpi_4, kpi_5, kpi_6 = st.columns(6)
with kpi_1:
    render_kpi_card("Total Users", display_data["total_users"], "")
with kpi_2:
    render_kpi_card("Users Who Viewed", display_data["view_users"], "")
with kpi_3:
    render_kpi_card("Added to Cart", display_data["cart_users"], "")
with kpi_4:
    render_kpi_card("Purchased", display_data["purchase_users"], "")
with kpi_5:
    render_kpi_card("Conversion", display_data["overall_conversion"], "")
with kpi_6:
    render_kpi_card("Retention Rate", display_data["retention_rate"], "")

st.markdown("")
st.markdown('<div id="funnel-section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Funnel Analysis</div>', unsafe_allow_html=True)

funnel_col, funnel_insights_col = st.columns([1.85, 1], gap="large")
with funnel_col:
    render_funnel_panel()

with funnel_insights_col:
    st.markdown(
        f"""
        <div class="analysis-badges">
            <span class="analysis-badge">Cart conversion: {display_data["cart_conversion"]}</span>
            <span class="analysis-badge">Checkout conversion: {display_data["purchase_conversion"]}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_insight_panel(
        "Analysis",
        "Short summary of funnel chart results",
        funnel_insights,
    )

st.markdown("")
st.markdown('<div id="retention-section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Retention</div>', unsafe_allow_html=True)

retention_col, retention_insights_col = st.columns([1.85, 1], gap="large")
with retention_col:
    render_retention_panel()

with retention_insights_col:
    render_insight_panel(
        "Retention Analysis",
        "Short summary of retention chart results",
        retention_insights,
    )

st.markdown("")
st.markdown(
    """
    <div class="footer-shell">
        <div class="footer-side">
            © 2026 Rahim Shahzad
        </div>
        <div class="footer-center">
            <a
                class="footer-link-button"
                href="https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop"
                target="_blank"
                rel="noopener noreferrer"
            >
                Download the dataset CSV file
            </a>
        </div>
        <div class="footer-actions">
            <span class="footer-text">
                Built with: 
            </span>
            <span class="footer-logo" title="Python">
                <img src="https://cdn.simpleicons.org/python/3776AB" alt="Python">
            </span>
            <span class="footer-logo" title="SQLite">
                <img src="https://cdn.simpleicons.org/sqlite/003B57" alt="SQLite">
            </span>
            <span class="footer-logo" title="Streamlit">
                <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" alt="Streamlit">
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
