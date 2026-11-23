
import streamlit as st
import pandas as pd

from calculator import calculate_savings
from visualization import (
    create_savings_chart,
    create_scenario_chart,
    create_monthly_table
)


# ==========================================
# 1. CẤU HÌNH GIAO DIỆN
# ==========================================

st.set_page_config(
    page_title="Savings Simulator",
    page_icon="💰",
    layout="wide"
)

st.title("💰 CÔNG CỤ MÔ PHỎNG KẾ HOẠCH TIẾT KIỆM")
st.write(
    "Công cụ hỗ trợ sinh viên lập kế hoạch, "
    "theo dõi và mô phỏng mục tiêu tiết kiệm cá nhân."
)

st.divider()


# ==========================================
# 2. HÀM ĐỊNH DẠNG TIỀN
# ==========================================

def format_money(amount):
    return f"{amount:,.0f} VNĐ"


# ==========================================
# 3. NHẬP THÔNG TIN ĐẦU VÀO
# ==========================================

st.header("1. Nhập thông tin kế hoạch")

with st.form("savings_form"):

    col1, col2 = st.columns(2)

    with col1:
        target_amount = st.number_input(
            "🎯 Mục tiêu tiết kiệm (VNĐ)",
            min_value=1,
            value=20000000,
            step=1000000
        )

        initial_savings = st.number_input(
            "💵 Số tiền tiết kiệm ban đầu (VNĐ)",
            min_value=0,
            value=0,
            step=100000
        )

        monthly_deposit = st.number_input(
            "📥 Số tiền gửi mỗi tháng (VNĐ)",
            min_value=0,
            value=1000000,
            step=100000
        )

    with col2:
        months = st.number_input(
            "📅 Thời gian tiết kiệm (tháng)",
            min_value=1,
            max_value=120,
            value=12,
            step=1
        )

        annual_interest_rate = st.number_input(
            "📈 Lãi suất năm (%)",
            min_value=0.0,
            max_value=100.0,
            value=3.0,
            step=0.5
        )

    submitted = st.form_submit_button(
        "🚀 MÔ PHỎNG KẾ HOẠCH",
        use_container_width=True
    )


# ==========================================
# 4. TÍNH TOÁN VÀ HIỂN THỊ KẾT QUẢ
# ==========================================

if submitted:

    try:
        result = calculate_savings(
            target_amount=target_amount,
            monthly_deposit=monthly_deposit,
            months=months,
            annual_interest_rate=annual_interest_rate,
            initial_savings=initial_savings
        )

        st.divider()

        st.header("2. Kết quả mô phỏng")

        # Hiển thị các chỉ số chính
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Tổng tiền tích lũy",
            format_money(result["total_savings"])
        )

        col2.metric(
            "Tổng tiền lãi",
            format_money(result["total_interest"])
        )

        col3.metric(
            "Số tiền còn thiếu",
            format_money(result["remaining_amount"])
        )

        # Kiểm tra mục tiêu
        if result["achieved"]:
            st.success(
                "🎉 Chúc mừng! Bạn đã đạt mục tiêu "
                "tiết kiệm trong thời gian dự kiến."
            )

            st.info(
                f"Bạn đạt mục tiêu vào tháng "
                f"{result['month_reached_goal']}."
            )

        else:
            st.warning(
                "Bạn chưa đạt mục tiêu trong thời gian "
                "đã lựa chọn. Hãy cân nhắc tăng số tiền "
                "gửi hàng tháng hoặc kéo dài thời gian."
            )

        st.info(
            "Số tiền cần gửi mỗi tháng để đạt mục tiêu: "
            + format_money(
                result["required_monthly_deposit"]
            )
        )

        # ==================================
        # 5. BIỂU ĐỒ TĂNG TRƯỞNG
        # ==================================

        st.divider()
        st.header("3. Biểu đồ tăng trưởng tiết kiệm")

        savings_chart = create_savings_chart(result)

        st.plotly_chart(
            savings_chart,
            use_container_width=True
        )

        # ==================================
        # 6. BẢNG THEO DÕI TỪNG THÁNG
        # ==================================

        st.divider()
        st.header("4. Chi tiết kế hoạch từng tháng")

        monthly_table = create_monthly_table(result)

        st.dataframe(
            monthly_table,
            use_container_width=True,
            hide_index=True
        )

        # Tải bảng theo dõi
        csv_data = monthly_table.to_csv(
            index=False
        ).encode("utf-8-sig")

        st.download_button(
            label="📥 Tải bảng kết quả CSV",
            data=csv_data,
            file_name="ket_qua_tiet_kiem.csv",
            mime="text/csv"
        )

        # ==================================
        # 7. SO SÁNH CÁC KỊCH BẢN
        # ==================================

        st.divider()
        st.header("5. So sánh các kịch bản tiết kiệm")

        st.write(
            "Công cụ tự động so sánh ba mức đóng góp: "
            "thấp hơn 50%, mức hiện tại và cao hơn 50%."
        )

        scenarios = []

        deposit_levels = [
            ("Kịch bản thấp", monthly_deposit * 0.5),
            ("Kịch bản hiện tại", monthly_deposit),
            ("Kịch bản cao", monthly_deposit * 1.5)
        ]

        for name, deposit in deposit_levels:

            scenario_result = calculate_savings(
                target_amount=target_amount,
                monthly_deposit=deposit,
                months=months,
                annual_interest_rate=annual_interest_rate,
                initial_savings=initial_savings
            )

            scenarios.append({
                "name": name,
                "total_savings": scenario_result["total_savings"],
                "target_amount": target_amount
            })

        scenario_chart = create_scenario_chart(
            scenarios
        )

        st.plotly_chart(
            scenario_chart,
            use_container_width=True
        )

        # Bảng so sánh
        comparison = pd.DataFrame([
            {
                "Kịch bản": item["name"],
                "Tiền gửi mỗi tháng": deposit,
                "Tổng tiền dự kiến": item["total_savings"],
                "Trạng thái": (
                    "Đạt mục tiêu"
                    if item["total_savings"] >= target_amount
                    else "Chưa đạt"
                )
            }
            for item, (_, deposit) in zip(
                scenarios, deposit_levels
            )
        ])

        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "Lưu ý: Kết quả dựa trên lãi suất giả định, "
            "tiền gửi cuối mỗi tháng và lãi được nhập vào vốn. "
            "Đây là công cụ mô phỏng, không phải cam kết "
            "lợi nhuận từ ngân hàng."
        )

    except ValueError as error:
        st.error(f"Dữ liệu không hợp lệ: {error}")

else:

    st.info(
        "👆 Hãy nhập thông tin và nhấn "
        "'MÔ PHỎNG KẾ HOẠCH' để bắt đầu."
    )

    st.subheader("Công cụ giúp bạn làm gì?")

    col1, col2, col3 = st.columns(3)

    col1.write("🎯 **Lập mục tiêu**")
    col1.caption("Xác định số tiền muốn tiết kiệm.")

    col2.write("📊 **Theo dõi tiến độ**")
    col2.caption("Quan sát số tiền tích lũy theo tháng.")

    col3.write("🔍 **So sánh kịch bản**")
    col3.caption("Thử nhiều mức tiết kiệm khác nhau.")
