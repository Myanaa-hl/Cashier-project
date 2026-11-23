from menu import show_menu
import csv
import time
import ast
from expense import show_expense

#Login


#Open_Orders
def take_orders(menus, cart) :
    
    while True :
        show_menu(menus)
        
        order = input("Silahkan Ketik Menu Yang Ingin Anda Pilih(Ketik Done Jika Sudah Selesai): ").strip().lower()
        if order == "done" :
            break
        elif order == "" :
            print("Tidak Boleh Kosong!")
            continue
        elif order.isdigit() :
            print("Tidak Boleh Angka!")
            continue
        
        select_menu = next( 
            (menu for menu in menus if menu["name"] == order), None)
        if select_menu is None :
            print("Menu Tidak DiTemukan")
            continue
        
        try :
            quantity = int(input("Silahkan Masukkan Quantity Yang Anda Inginkan: "))
        except ValueError :
            print("Tolong Ketik Dalam Angka!")
            continue 
        
        if quantity <= 0 :
            print("Quantity Harus Lebih Dari 0!")
            continue
            
        cart.append({"name" : select_menu["name"], "price" : select_menu["price"], "quantity": quantity })
            
#Cart
def show_cart(cart) :
    
    notes = "Keranjang Belanja Anda"
    width = 45
    total = 0
    
    if not cart :
        print("Belum Ada data Belanjaan Yang Terisi!")
        return 0
    
    print()
    print("=" * width )
    print(f"{notes:^{width - 2}}")
    print("=" * width )
    print()
    
    print(f"{'No.':<3} {'Nama Menu':<20} {'Qty':<5} {'Subtotal':>13}")
    print("-" * width)
    
    for number, item in enumerate(cart, 1) :
        subtotal = item['price'] * item['quantity']
        total += subtotal
        
        print(f"{number:<3} {item['name'].title():<20} x {item['quantity']:<5} {subtotal:>10,.0f}")
    
    print("-" * width)
    print(f"{'Total Belanja':>4} : {total:>28,.0f}")
    return total
    
#Payment
def payment(cart, history) :
    
    if len(cart) == 0 :
        print("Belum Dapat Melakukan Pembayaran Karena Belum Ada Data Yang Terisi")
        return
    
    total = show_cart(cart)  
    print()

    while True :
        
        if len(cart) == 0 :
            print("Belum Dapat Melakukan Pembayaran, Tidak Ditemukan Data")
            return False
        
        transaction_id = f"C{len(history) + 1:03d}"
        
        wide = 38
        end = "Terima Kasih"
        
        try :
            cash = float(input("Silahkan Masukkan Uang Pembayaran: "))
        except ValueError :
            print("Tolong Masukkan Angka!")
            continue
        if cash < total :
            print("Uang Anda Tidak Cukup!")
            continue
        
        change = cash - total
        
        print(f"{'Indigo Restaurant':^{wide-1}}")
        print("-" * 38)
        print(f"Total Belanja :  {total:>20,.0f}")
        print(f"Uang Dibayar  :  {cash:>20,.0f}")
        print("=" * 38)
        print(f"Uang Kembalian : {change:>20,.0f}")
        print("-" * 38)
        print(f"{end:^{wide-2}}")
        
        time_orders = time.strftime("%Y-%m-%d %H:%M")
        history.append({"date" : time_orders ,
                        "transaction_id" : transaction_id ,
                        "item" : cart.copy(),
                        "total" : total,
                        "cash" : cash,
                        "change" : change})
        return True
        
#History    
def hs_pay(history) :
    
    if len(history) == 0 :
        print("Belum Ada Riwayat Transaksi")
        return
    
    print()
    for pay in history :
        print()
        print("-" * 45)
        print(f"{'Riwayat Pembayaran':^43}")
        print("-" * 45)
        print(f"Date           :    {pay['date']:>25}")
        print(f"Transaction Id :    {pay['transaction_id']:>25}")
        print("-" * 45)
        print(f"{'No.':<3} {'Nama Menu':<20} {'Price':>10} {'Qty':>9}")
        print("-" * 45)
        for number, item in enumerate(pay['item'], 1) :
            print(f"{number:<3} {item['name'].title():<20} {item['price']:>10,.0f} {item['quantity']:>9}")
        
        print("=" * 45)
        print(f"Total Belanja  :  {pay['total']:>27,.0f}")
        print(f"Uang Dibayar   :  {pay['cash']:>27,.0f}")
        print("-" * 45)
        print(f"Uang Kembalian :  {pay['change']:>27,.0f}")
    

#save and load
hs_track = "history.csv"    
fields = ["date","transaction_id", "item" ,"total","cash","change"]
def history_load() :
    history = []
    
    try :
        with open(hs_track, "r", newline="") as file :
            for row in csv.DictReader(file) :

                history.append({
                    "date" : row['date'],
                    "transaction_id" : row['transaction_id'],
                    "item" : ast.literal_eval(row['item']),
                    "total" : float(row['total']),
                    "cash" : float(row['cash']),
                    "change" : float(row['change'])
                })
    except FileNotFoundError :
        pass
    return history

def history_save(history) :
    with open(hs_track, "w", newline="") as file :
        writer = csv.DictWriter (file,fieldnames=fields) 
        writer.writeheader()
        writer.writerows(history) 

#Income
def income(history,sold,netty, exp) :

    length = 38
    if len(history) == 0 :
        print("Belum Ada Penjualan Saat Ini")
        return
    
    net = 0
    for ex in exp :
        net += ex['nominal'] 
     
    spent = 0
    for transaction in history :
        spent += transaction['total'] 

    ss = spent - net

    for transaction in history :
        for item in transaction['item'] :
            name = item['name'] 
            quant = item['quantity']
            sold[name] = sold.get(name, 0) + quant
            netty[name] = netty.get(name, 0) + (quant * item['price'])

    max_item = ""
    max_am = -1
    
    for name, quant in sold.items() :
        if quant > max_am :
            max_item = name
            max_am = quant

    min_item = ""
    min_am = float("inf")
    
    for name, quant in sold.items() :
        if quant < min_am :
            min_item = name
            min_am = quant
            
    print(f"{'Recap Penjualan':^43}")
    print("-" * 45)
    print(F"{'Name':<20} {'Qty':>7} {'Total':>16}")
    print("-" * 45)
    for name, quant in sold.items() :
        print (f"{name:<20} {quant:>7} {netty[name]:>16,.0f}")
    print("-" * 45)
    print()
    print("=" * 45)
    print()
    print(f"{'Pendapatan Indigo Restaurant':^{length-2}}")
    print("-" * length)
    print(time.strftime ("%Y-%m-%d %H:%M"))
    print()
    print(f"Total Pendapatan : {spent:>19,.0f}")
    print(f"Total Expense    : {net:19,.0f}")
    print("-" * length)
    print(f"Pendapatan Bersih: {ss:19,.0f}")
    print("-" * length)
    print(f"Menu Paling Laku {max_item.title():>21}")
    print(f"Jumlah Terjual {max_am:>23,.0f}")
    print("-" * length)
    print(f"Menu Jarang Keluar {min_item.title():>19}")
    print(f"Jumlah Terjual {min_am:>23}")
    print("-" * length)
    
def logout(history) :
    
    inc = 0
    for rev in history :
        inc += rev['total']
        
    
    while True :
        print(f"{'Closing':^33}")
        print("-" * 45)
        print(f"Cash Seharusnya : {inc:>16,.0f}")
        print()
        admin = float(input("Cash Di Kasir: "))
        print("=" * 45)
        gap = inc - admin
        print()
        print(f"Selisih Antara Aplikasi Dan Kasir {gap:,.0f}")
        print("Jika Sudah Balance Lakukan Closeout")
        print()
        close_out = input("Ketik Closeout Untuk Tutup: ").lower().strip()
        if close_out.isdigit() :
            print("Tidak Boleh Angka!")
            continue
        elif close_out == "closeout" :
            break
        
    