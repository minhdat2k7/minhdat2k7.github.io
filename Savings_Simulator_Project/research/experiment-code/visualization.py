
import pandas as pd
import plotly.graph_objects as go


def create_savings_chart(result):
    """
    Tạo biểu đồ mô phỏng quá trình tiết kiệm
    theo từng tháng.
    """

    schedule = result["schedule"]

    # Chuyển dữ liệu thành DataFrame
    df = pd.DataFrame(schedule)

    # Thêm tháng 0 để thể hiện số dư ban đầu
    initial_balance = (
        df.iloc[0]["opening_balance"]
        if not df.empty
        else 0
    )

    chart_months = [0] + df["month"].tolist()
    savings = [initial_balance] + df["closing_balance"].tolist()

    # Khởi tạo biểu đồ
    fig = go.Figure()

    # Đường biểu diễn số tiền tích lũy
    fig.add_trace(
        go.Scatter(
            x=chart_months,
            y=savings,
            mode="lines+markers",
            name="Tiền tích lũy",
            line=dict(width=3)
        )
    )

    # Đường mục tiêu tiết kiệm
    fig.add_trace(
        go.Scatter(
            x=chart_months,
            y=[result["target_amount"]] * len(chart_months),
            mode="lines",
            name="Mục tiêu tiết kiệm",
            line=dict(dash="dash", width=2)
        )
    )

    # Thiết lập giao diện biểu đồ
    fig.update_layout(
        title="Quá trình tích lũy tiền tiết kiệm",
        xaxis_title="Thời gian (tháng)",
        yaxis_title="Số tiền (VNĐ)",
        hovermode="x unified",
        template="plotly_white",
        legend_title="Chú thích"
    )

    fig.update_xaxes(
        dtick=1,
        tickmode="linear"
    )

    fig.update_yaxes(
        tickformat=",.0f"
    )

    return fig


def create_scenario_chart(scenarios):
    """
    So sánh tổng tiền tích lũy
    giữa các kịch bản tiết kiệm.

    scenarios: danh sách kết quả từ calculator.py
    """

    names = [
        scenario["name"] for scenario in scenarios
    ]

    totals = [
        scenario["total_savings"] for scenario in scenarios
    ]

    targets = [
        scenario["target_amount"] for scenario in scenarios
    ]

    fig = go.Figure()

    # Cột tổng tiền tích lũy
    fig.add_trace(
        go.Bar(
            x=names,
            y=totals,
            name="Tổng tiền tích lũy"
        )
    )

    # Đường mục tiêu
    if targets and all(t == targets[0] for t in targets):
        fig.add_trace(
            go.Scatter(
                x=names,
                y=targets,
                mode="lines",
                name="Mục tiêu",
                line=dict(dash="dash", width=2)
            )
        )

    fig.update_layout(
        title="So sánh các kịch bản tiết kiệm",
        xaxis_title="Kịch bản",
        yaxis_title="Tổng tiền (VNĐ)",
        template="plotly_white",
        barmode="group"
    )

    fig.update_yaxes(tickformat=",.0f")

    return fig


def create_monthly_table(result):
    """
    Tạo bảng theo dõi tiền tiết kiệm từng tháng.
    """

    df = pd.DataFrame(result["schedule"])

    if df.empty:
        return df

    df = df.rename(
        columns={
            "month": "Tháng",
            "opening_balance": "Tiền đầu kỳ",
            "deposit": "Tiền gửi",
            "interest": "Tiền lãi",
            "closing_balance": "Tổng tiền cuối kỳ"
        }
    )

    return df
