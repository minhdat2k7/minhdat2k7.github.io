
# RESEARCH METHODOLOGY

## 1. Research Problem

Sinh viên thường gặp khó khăn trong việc xác định số tiền cần tiết kiệm, thời gian tích lũy và khả năng đạt được mục tiêu tài chính.

Đề tài hướng đến việc xây dựng công cụ mô phỏng giúp sinh viên lập kế hoạch tiết kiệm và đánh giá các phương án khác nhau.

## 2. Research Data

Dữ liệu nghiên cứu được thu thập thông qua khảo sát sinh viên.

Các thông tin cần phân tích:

- Đặc điểm người tham gia khảo sát.
- Khả năng tiết kiệm hàng tháng.
- Mục tiêu tiết kiệm.
- Thời gian dự kiến tiết kiệm.
- Các yếu tố ảnh hưởng đến hành vi tiết kiệm.

Dữ liệu được xử lý và phân tích bằng các công cụ phù hợp.

## 3. Research Variables

| Variable | Description |
|---|---|
| Target Amount | Mục tiêu tiết kiệm |
| Monthly Deposit | Số tiền tiết kiệm hàng tháng |
| Initial Savings | Số tiền tiết kiệm ban đầu |
| Saving Duration | Thời gian tiết kiệm |
| Interest Rate | Lãi suất giả định |
| Total Savings | Tổng tiền tích lũy |
| Remaining Amount | Số tiền còn thiếu |

## 4. Mathematical Model

### 4.1. Model without interest

S = P × T + S0

Trong đó:

- S: Tổng tiền tiết kiệm.
- P: Số tiền gửi hàng tháng.
- T: Số tháng tiết kiệm.
- S0: Số tiền ban đầu.

### 4.2. Model with monthly compound interest

S = S0(1+r)^T + P × [(1+r)^T - 1]/r

Trong đó:

- S: Tổng tiền tích lũy.
- S0: Số tiền ban đầu.
- P: Số tiền gửi cuối mỗi tháng.
- r: Lãi suất tháng.
- T: Số tháng tiết kiệm.

Lãi suất tháng được tính:

r = Lãi suất năm / 12 / 100

Trường hợp lãi suất bằng 0:

S = S0 + P × T

## 5. Simulation Method

Công cụ mô phỏng được xây dựng bằng Python.

Các bước thực hiện:

1. Nhập thông tin kế hoạch tiết kiệm.
2. Kiểm tra dữ liệu đầu vào.
3. Tính toán số tiền tích lũy.
4. Tính tiền lãi và số tiền còn thiếu.
5. Xác định khả năng đạt mục tiêu.
6. Hiển thị biểu đồ và bảng kết quả.
7. So sánh các kịch bản tiết kiệm.

## 6. Experimental Design

Thực hiện các kịch bản với:

- Mức tiết kiệm hàng tháng khác nhau.
- Thời gian tiết kiệm khác nhau.
- Lãi suất khác nhau.
- Mức mục tiêu tài chính khác nhau.

## 7. Evaluation

Đánh giá công cụ dựa trên:

- Độ chính xác của kết quả tính toán.
- Khả năng cập nhật khi thay đổi đầu vào.
- Mức độ dễ sử dụng.
- Mức độ dễ hiểu của kết quả.
- Mức độ hữu ích đối với sinh viên.
