def validate_registration_input(name, email, phone):
    clean_name = name.strip()
    clean_email = email.strip().lower()
    clean_phone = phone.strip()
    
    # TODO 1: Kiểm tra email chứa ký tự @
    is_email_valid = "@" in clean_email
    
    # TODO 2: Kiểm tra SĐT (10 chữ số, toàn số, đầu 03/05/07/08/09)
    valid_prefixes = ("03", "05", "07", "08", "09")
    # Điền valid_prefixes vào phương thức startswith()
    is_phone_valid = (len(clean_phone) == 10) and clean_phone.isdigit() and clean_phone.startswith(valid_prefixes)
    
    return clean_name, clean_email, is_email_valid, clean_phone, is_phone_valid

# Dữ liệu kiểm thử
registers = [
    {"name": "  Nguyen Van An  ", "email": "an.nguyen@gmail.com", "phone": "0987654321"},
    {"name": "Tran Thi Bich", "email": "bich_gmail.com", "phone": "0912345678"},
    {"name": "Le Hoang Cuong", "email": "cuong@rikkei.edu.vn", "phone": "0123456789"}
]

print("=== BÁO CÁO KẾT QUẢ VALIDATE THÔNG TIN ===")
for r in registers:
    c_n, c_e, e_ok, c_p, p_ok = validate_registration_input(r["name"], r["email"], r["phone"])
    status = "✅ HỢP LỆ" if (e_ok and p_ok) else "❌ KHÔNG HỢP LỆ"
    print(f"[{c_n}] Email: {c_e} | SDT: {c_p} -> {status}")