def  check_low_stock():
    if not products:
        print("Kho hiện tại đang trống")
        return
    print('Danh sách sản phẩm có số lượng dưới 5: ')
    print('--------------------------')
    stt = 1
    for p in products:
        if p['qty'] < 5:
            print(f"{stt}. Sản phẩm: {p['name']}, giá: {p['price']}, số lượng: {p['qty']}")
            stt += 1
