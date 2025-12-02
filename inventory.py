# 24S1020031 - Mai Đăng Khoa
products = []

def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)

def view_inventory():
    if not products:
        print("Kho hiện đang trống!")
        return
    print('Danh sách sản phẩm trong kho:')
    stt = 1
    for p in products:
        print(f"{stt}. Sản phẩm: {p['name']}, giá: {p['price']}, số lượng: {p['qty']}")
        stt += 1

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

def main():
    while True:
        print('Menu quản lý Inventory:')
        print('--------------------------')
        print('1. Thêm sản phẩm')
        print('2. Xem danh sách sản phẩm')
        print('3. Duyệt danh sách sản phẩm có số lượng dưới 5')
        print('4. Thoát chương trình!!!')
        print('--------------------------')
        choice = input("Chọn chức năng: ") 
        if choice == '1': 
            name = input("Nhập tên sản phẩm: ")
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng: "))
            add_product(name, price, quantity)
            print(">> Đã thêm sản phẩm thành công!")
        elif choice == '2': 
            view_inventory() 
        elif choice == '3': 
            check_low_stock() 
        elif choice == '4': 
            print("Kết thúc chương trình.")
            break
        else: 
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
