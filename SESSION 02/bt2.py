orders = [15000000, 5000000, 22000000, 800000, 12000000]

# TODO 1: Khởi tạo biến tích lũy tổng doanh thu và biến đếm đơn VIP
total_revenue = 0
vip_count = 0

for price in orders:
    total_revenue += price
    if price > 10000000:
        vip_count += 1

print(f"Tổng doanh thu: {total_revenue:,} VNĐ")
print(f"Số đơn VIP: {vip_count} đơn")