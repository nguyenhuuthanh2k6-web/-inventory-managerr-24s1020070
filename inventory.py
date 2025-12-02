def add_product():
    print("\n=== NHẬP HÀNG MỚI ===")
    name = input("Tên sản phẩm: ")
    price = int(input("Giá bán: "))
    qty = int(input("Số lượng tồn: "))

    product = {
        "name": name,
        "price": price,
        "qty": qty
    }

    products.append(product)
    print("✔ Đã nhập hàng thành công!?")