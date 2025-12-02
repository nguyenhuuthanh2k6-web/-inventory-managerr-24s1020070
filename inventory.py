def view_inventory():
    if not products:
        print("Kho hiện đang trống!")
        return
    print('Danh sách sản phẩm trong kho:')
    stt = 1
    for p in products:
        print(f"{stt}. Sản phẩm: {p['name']}, giá: {p['price']}, số lượng: {p['qty']}")
        stt += 1
