def sap_xep_va_loai_bo_trung(arr):
    # Tạo một từ điển để đếm số lần xuất hiện của mỗi phần tử
    count_dict = {}
    for item in arr:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    # Sắp xếp từ điển theo số lần xuất hiện giảm dần
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Tạo một danh sách mới từ các phần tử đã sắp xếp
    sorted_unique_items = [item for item, count in sorted_items]
    
    return sorted_unique_items

# Sử dụng hàm
danh_sach = [4, 2, 5, 2, 1, 4, 5, 6, 2, 4, 4]
ket_qua = sap_xep_va_loai_bo_trung(danh_sach)
print(ket_qua)