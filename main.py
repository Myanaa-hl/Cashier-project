from menu import indigo_m, load, save
from order import take_orders, show_cart, payment, hs_pay, history_load, history_save, income, logout
from expense import add_expense, show_expense, exp_load

def main() :
    
    menus = load()
    cart = []
    history = history_load()
    sold = {}
    netty = {}
    exp = []
    ex_hs = exp_load()
    categories = ['bahan', 'karyawan', 'operasional','lainnya']

    print()
    print("=" * 10, "Indigo Restaurant", "=" * 10)
    print("-" * 39)
    
    while True :
        
        print("1. Order System")
        print("2. Keranjang Belanja Anda")
        print("3. Pembayaran")
        print("4. Riwayat Pembayaran")
        print("5. Tambahkan Menu")
        print("6. Expenses")
        print("7. Expenses Recap")
        print("8. Total Pendapatan")
        print("9. Closing")
        
        customer = input("Silahkan Ketik Berdasarkan Angka: ")
        if customer == "1" :
            take_orders(menus, cart)
        elif customer == "2" :
            show_cart(cart)
        elif customer == "3" :
            payment(cart,history)
            history_save(history)
            cart.clear()
        elif customer == "4" :
            hs_pay(history)
        elif customer == "5" :
            indigo_m(menus)
            save(menus)
        elif customer == "6" :
            add_expense(exp, categories)
        elif customer == "7" :
            show_expense(exp, ex_hs)
        elif customer == "8" :
            income(history,sold,netty)
        elif customer == "9" :
            logout(history)
        else :
            print("Isi Sesuai Nomor Yang Ada")
            
if __name__ == '__main__' :
    main()