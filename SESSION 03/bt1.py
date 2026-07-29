inventory = [
    {"id": "SP1", "ten": "Tai nghe Sony", "gia": 1200000, "danh_muc": "Phụ kiện"},
    {"id": "SP2", "ten": "Chuột không dây", "gia": 450000, "danh_muc": "Phụ kiện"},
    {"id": "SP3", "ten": "Bàn phím cơ", "gia": 950000, "danh_muc": "Phụ kiện"},
    {"id": "SP4", "ten": "Màn hình Dell", "gia": 3500000, "danh_muc": "Thiết bị"}
]

# TODO 1: SV thay dấu ... bằng điều kiện lọc gia <= 1000000 và danh_muc == "Phụ kiện"
filtered_items = []
for item in inventory:
    # Điền 1000000 cho giá và "Phụ kiện" cho danh mục
    if item["gia"] <= 1000000 and item["danh_muc"] == "Phụ kiện":
        filtered_items.append(item["ten"])

print("Sản phẩm Phụ kiện <= 1 triệu:", filtered_items)