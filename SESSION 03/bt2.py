students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4}
]

# TODO 1: SV thay dấu ... để sắp xếp GIẢM DẦN theo gpa (So sánh gpa[j] < gpa[j+1])
n = len(students)
for i in range(n):
    for j in range(0, n - i - 1):
        # Điền "gpa" để so sánh điểm của sinh viên thứ j+1
        if students[j]["gpa"] < students[j + 1]["gpa"]:
            # Điền j để hoàn thành việc hoán đổi (swap) 2 sinh viên
            students[j], students[j + 1] = students[j + 1], students[j]

print("Bảng xếp hạng sinh viên (GPA Giảm Dần):")
for s in students:
    print(f"  -> {s['name']}: {s['gpa']} điểm")