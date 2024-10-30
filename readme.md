1. Mô tả
Dự án này là một hệ thống quản lý cửa hàng bán quần áo thời trang, sử dụng Django làm backend và Oracle Database làm cơ sở dữ liệu. Hệ thống hỗ trợ quản lý sản phẩm, danh mục, nhà cung cấp và các thông tin liên quan đến cửa hàng thời trang.

2. Yêu cầu
Python (phiên bản 3.8+)
Django (phiên bản 3.2+)
Oracle Database (Oracle 19c hoặc mới hơn)
Oracle Instant Client để kết nối Django với Oracle Database
3. Hướng dẫn cài đặt
Bước 1: Clone dự án

git clone <URL của repository>
cd <tên thư mục dự án>
Bước 2: Tạo môi trường ảo
Tạo môi trường ảo để quản lý các thư viện:

python -m venv venv
source venv/bin/activate      # Trên MacOS/Linux
venv\Scripts\activate         # Trên Windows
Bước 3: Cài đặt các thư viện yêu cầu
Dùng pip để cài đặt các thư viện từ file requirements.txt:


pip install -r requirements.txt
Lưu ý: Đảm bảo bạn đã cài đặt Oracle Instant Client và thêm vào biến môi trường PATH để Python có thể tìm thấy thư viện này.

Bước 4: Cấu hình kết nối Oracle Database
Trong file cấu hình Django settings.py, thiết lập kết nối đến cơ sở dữ liệu Oracle. Ví dụ cấu hình:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '<TÊN_DATABASE>',
        'USER': '<TÊN_USER>',
        'PASSWORD': '<MẬT_KHẨU>',
        'HOST': '<ĐỊA_CHỈ_HOST>',
        'PORT': '<CỔNG_PORT>',
    }
}
Thông tin cần thay thế:

NAME: Tên cơ sở dữ liệu Oracle.
USER: Tên người dùng để truy cập vào Oracle.
PASSWORD: Mật khẩu của người dùng.
HOST: Địa chỉ máy chủ Oracle (localhost hoặc địa chỉ IP).
PORT: Cổng kết nối đến Oracle Database, thường là 1521.
Bước 5: Tạo các bảng và dữ liệu ban đầu
Chạy các lệnh sau để tạo các bảng và dữ liệu ban đầu:


python manage.py makemigrations
python manage.py migrate
Bước 6: Chạy ứng dụng
Chạy server Django bằng lệnh sau:

python manage.py runserver