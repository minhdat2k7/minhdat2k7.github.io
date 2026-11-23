
# THIẾT KẾ CÔNG CỤ MÔ PHỎNG KẾ HOẠCH TIẾT KIỆM CHO SINH VIÊN

## 1. Overview

**Topic:** Thiết kế công cụ mô phỏng kế hoạch tiết kiệm cho sinh viên.

**Objective:** Xây dựng công cụ giúp sinh viên lập kế hoạch tiết kiệm, tính toán số tiền tích lũy và đánh giá khả năng đạt mục tiêu tài chính.

**Approach:** Sử dụng Python để xây dựng công cụ mô phỏng, kết hợp dữ liệu khảo sát và các kịch bản tiết kiệm.

## 2. Project Structure

```text
Savings_Simulator_Project/
├── README.md
├── requirements.txt
├── research-metadata.md
├── research-methodology.md
├── literature-review/
├── research/
│   ├── data/
│   ├── experiment-code/
│   │   ├── calculator.py
│   │   ├── visualization.py
│   │   └── main.py
│   └── experiment-results/
└── essay-template/
```

## 3. Technologies

- Python
- Streamlit
- Pandas
- Plotly
- Excel / Google Sheets
- Stata (phân tích dữ liệu khảo sát nếu cần)

## 4. Installation

Cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

## 5. Run the Application

Chạy chương trình:

```bash
python -m streamlit run research/experiment-code/main.py
```

Mở trình duyệt tại:

http://localhost:8501

## 6. Main Features

- Nhập mục tiêu tiết kiệm.
- Nhập số tiền tiết kiệm hàng tháng.
- Thiết lập thời gian tiết kiệm.
- Điều chỉnh lãi suất giả định.
- Tính toán tổng tiền tích lũy.
- Theo dõi tiến độ tiết kiệm.
- So sánh các kịch bản.
- Xuất bảng kết quả.

## 7. Expected Results

Xây dựng được công cụ mô phỏng hoạt động, hỗ trợ sinh viên lập kế hoạch tiết kiệm và đánh giá các phương án tài chính cá nhân.
