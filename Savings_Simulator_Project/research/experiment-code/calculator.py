
def calculate_savings(
    target_amount,
    monthly_deposit,
    months,
    annual_interest_rate=0,
    initial_savings=0
):
    """
    Mô phỏng kế hoạch tiết kiệm cho sinh viên.

    Giả định:
    - Lãi suất năm được quy đổi thành lãi suất tháng.
    - Tiền được gửi vào cuối mỗi tháng.
    - Lãi phát sinh trên số dư đầu tháng.
    """

    # 1. Kiểm tra dữ liệu đầu vào
    if target_amount <= 0:
        raise ValueError("Mục tiêu tiết kiệm phải lớn hơn 0.")

    if monthly_deposit < 0 or initial_savings < 0:
        raise ValueError("Số tiền tiết kiệm không được âm.")

    if months <= 0 or int(months) != months:
        raise ValueError("Thời gian phải là số tháng nguyên dương.")

    if annual_interest_rate < 0:
        raise ValueError("Lãi suất không được âm.")

    months = int(months)

    # 2. Quy đổi lãi suất năm sang tháng
    monthly_rate = annual_interest_rate / 100 / 12

    # 3. Khởi tạo các giá trị
    balance = initial_savings
    total_interest = 0
    schedule = []

    month_reached_goal = (
        0 if balance >= target_amount else None
    )

    # 4. Mô phỏng từng tháng
    for month in range(1, months + 1):

        opening_balance = balance

        # Tiền lãi phát sinh trong tháng
        interest = opening_balance * monthly_rate

        # Cộng lãi và tiền gửi cuối tháng
        balance = opening_balance + interest + monthly_deposit

        total_interest += interest

        # Kiểm tra thời điểm đạt mục tiêu
        if (
            month_reached_goal is None
            and balance >= target_amount
        ):
            month_reached_goal = month

        # Lưu kết quả từng tháng
        schedule.append({
            "month": month,
            "opening_balance": opening_balance,
            "deposit": monthly_deposit,
            "interest": interest,
            "closing_balance": balance
        })

    # 5. Tính số tiền còn thiếu
    remaining_amount = max(target_amount - balance, 0)

    # 6. Tính số tiền cần gửi mỗi tháng để đạt mục tiêu
    if monthly_rate == 0:
        required_monthly_deposit = max(
            (target_amount - initial_savings) / months,
            0
        )
    else:
        future_initial = (
            initial_savings * (1 + monthly_rate) ** months
        )

        annuity_factor = (
            (1 + monthly_rate) ** months - 1
        ) / monthly_rate

        required_monthly_deposit = max(
            (target_amount - future_initial) / annuity_factor,
            0
        )

    # 7. Tổng tiền đã đóng góp
    total_contribution = (
        initial_savings + monthly_deposit * months
    )

    # 8. Trả về kết quả
    return {
        "target_amount": target_amount,
        "monthly_deposit": monthly_deposit,
        "months": months,
        "annual_interest_rate": annual_interest_rate,
        "total_contribution": total_contribution,
        "total_interest": total_interest,
        "total_savings": balance,
        "remaining_amount": remaining_amount,
        "required_monthly_deposit": required_monthly_deposit,
        "achieved": balance >= target_amount,
        "month_reached_goal": month_reached_goal,
        "schedule": schedule
    }
