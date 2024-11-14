-- Bảng danh mục sản phẩm (Category Table)
CREATE TABLE Category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Bảng thương hiệu mỹ phẩm (Brand Table)
CREATE TABLE Brand (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    origin_country VARCHAR(100)
);

-- Bảng sản phẩm mỹ phẩm (Product Table)
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INTEGER REFERENCES Category(id) ON DELETE CASCADE,
    brand_id INTEGER REFERENCES Brand(id) ON DELETE SET NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER NOT NULL,
    description TEXT,
    skin_type VARCHAR(50) CHECK (skin_type IN ('All', 'Dry', 'Oily', 'Sensitive', 'Normal')) DEFAULT 'All',
    image VARCHAR(100) -- Đường dẫn ảnh (tùy chọn)
);

-- Bảng đơn hàng (Order Table)
CREATE TABLE Order (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_address TEXT NOT NULL,
    customer_phone VARCHAR(15) NOT NULL,
    date_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')) DEFAULT 'Pending'
);

-- Bảng chi tiết đơn hàng (Order Detail Table)
CREATE TABLE OrderDetail (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES Order(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES Product(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
