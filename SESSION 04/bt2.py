def safe_process_invoice(order_id, raw_total, discount_code, is_vip):
    try:
        # TODO 1: Ép kiểu float(raw_total)
        # Điền raw_total vào hàm float() để chuyển đổi chuỗi thành số thập phân
        subtotal = float(raw_total)
        
        # TODO 2: Tính chiết khấu VIP
        discount_rate = 0.0
        if is_vip and discount_code == "VIP10":
            discount_rate = 0.10
        elif is_vip and discount_code == "VIP20":
            discount_rate = 0.20
            
        subtotal_after_discount = subtotal * (1 - discount_rate)
        vat = subtotal_after_discount * 0.10
        final_total = subtotal_after_discount + vat
        
        tier = "HÓA ĐƠN LỚN (VIP)" if final_total >= 10000000 else "HÓA ĐƠN THƯỜNG"
        return final_total, tier
        
    except ValueError: # Điền ValueError để bắt lỗi ép kiểu không thành công
        print(f"⚠️ Xử lý lỗi [{order_id}]: Số tiền '{raw_total}' không hợp lệ! Bỏ qua đơn hàng.")
        return None, "LỖI"

orders = [
    {"id": "DH01", "total": "12500000", "discount_code": "VIP10", "is_vip": True},
    {"id": "DH02", "total": "450000", "discount_code": "INVALID", "is_vip": False},
    {"id": "DH03", "total": "ABC_ERROR", "discount_code": "", "is_vip": False}
]

print("=== BÁO CÁO THỰC THI HÓA ĐƠN ===")
for o in orders:
    tot, t = safe_process_invoice(o["id"], o["total"], o["discount_code"], o["is_vip"])
    if tot:
        print(f"[{o['id']}] Tổng thanh toán: {tot:,.0f} VNĐ [{t}]")