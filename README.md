# Hand Language Project

Hệ thống nhận diện cử chỉ tay bằng AI cho giao tiếp ngôn ngữ ký hiệu.

Dự án xây dựng một pipeline xử lý hình ảnh và học sâu để phát hiện và nhận dạng các cử chỉ tay thời gian thực, hỗ trợ giao tiếp cho người khuyết tật.
<img width="220" height="220" alt="image" src="https://github.com/user-attachments/assets/b7e4676c-f935-417a-91e0-f2561fa279bb" />

## Tính năng chính

- Nhận diện cử chỉ tay thời gian thực từ camera
- Mô hình học sâu tùy chỉnh được huấn luyện bằng TensorFlow/Keras
- Phân loại ký hiệu tay
- Demo và bộ công cụ phát hiện nằm trong `Hand_Lang/demo.py`
- Mô hình đã huấn luyện lưu tại `Hand_Lang/models`

## Công nghệ sử dụng

- Python
- OpenCV
- TensorFlow / Keras
- NumPy
- Xử lý dữ liệu và huấn luyện mô hình tùy chỉnh

## Cấu trúc dự án

- `Hand_Lang/demo.py` — demo nhận diện cử chỉ tay thời gian thực
- `Hand_Lang/detection.py` — tiện ích phát hiện và dự đoán
- `Hand_Lang/train_model.py` — pipeline huấn luyện mô hình
- `Hand_Lang/models/` — file mô hình đã lưu
- `README_USAGE.txt` — hướng dẫn sử dụng
- `QUICK_START.txt` — ghi chú cài đặt nhanh

## Hướng dẫn chạy

1. Kích hoạt môi trường ảo: `d:\Hand_land\.venv\Scripts\Activate.ps1`
2. Cài đặt các thư viện cần thiết nếu chưa có
3. Chạy demo: `python Hand_Lang/demo.py`

## Ý nghĩa dự án

Dự án thể hiện ứng dụng của machine learning trong công nghệ hỗ trợ, kết hợp thị giác máy tính và học sâu để tạo ra hệ thống thực tiễn giúp giao tiếp cho người khiếm thính hoặc khuyết tật.

## Mô tả

**Hand Land** — Hệ thống nhận diện cử chỉ tay dựa trên AI cho giao tiếp ngôn ngữ ký hiệu. Phát triển toàn bộ pipeline từ tiền xử lý dữ liệu và huấn luyện mô hình đến ứng dụng demo trực tuyến bằng Python, OpenCV và TensorFlow. Hướng đến hỗ trợ giao tiếp cho người khuyết tật.

<img width="799" height="639" alt="image" src="https://github.com/user-attachments/assets/219223d1-cf32-4c95-bdb7-5be9f19f5c03" />
<img width="804" height="637" alt="image" src="https://github.com/user-attachments/assets/cb280c52-59bf-4167-af33-bff41584ab80" />

