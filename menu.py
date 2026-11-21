import csv

#Admin_circle
def indigo_m (menus) :
    
    while True :
        food = input("Silahkan Tambahkan Menu Makanan(Ketik Done Untuk Selesai): ").strip().lower()
        if food == "" :
            print("Tolong Diisi")
            continue
        elif food.isdigit() :
            print("Tidak Boleh Berupa Angka")
            continue
        elif food == "done" :
            break
        try :
            food_amount = float(input("Silahkan Isi List Harga Makanan: "))
        except ValueError :
            print("Tolong Isi Dengan Angka!")
            continue
        if food_amount <= 0 :
            print("Harga Tidak Boleh Sama dan Kurang Dari 0")
            continue
        
        menus.append({"type" : "makanan", "name" : food, "price" : food_amount})
        
    print()
    
    while True :
        drink = input("Silahkan Tambahkan Menu Minuman(Done Untuk Selesai): ").strip().lower()
        if drink == "" :
            print("Tolong Diisi")
            continue
        elif drink == "done" :
            break
        elif drink.isdigit() :
            print("Tidak Boleh Berupa Angka")
            continue
        try :
            drink_amount = float(input("Silahkan Isi List Harga Minuman: "))
        except ValueError :
            print("Tolong Isi Dengan Angka!")
            continue
        if drink_amount <= 0 :
            print("Harga Tidak Boleh Sama dan Kurang Dari 0")
            continue
        
        menus.append({"type" : "minuman", "name" : drink, "price" : drink_amount})

#menu
def show_menu(menus) :   
    
    if len(menus) == 0 :
        print("Belum Ada Data Yang Terisi")
        return
    
    number = 1
    foods = []
    for menu in menus :
        if menu["type"] == "makanan" :
            foods.append(menu)
    
    print("=" * 9, "Indigo's Menu" ,"=" * 9)
    print("-" * 5, "Makanan", "-" * 5)
    for menu in foods :
        print(f"{number:<4}{menu['name']:<25} {menu['price']:>18,.0f}")  
        number += 1
        
    drinks = []
    for menu in menus :
        if menu["type"] == "minuman" :
            drinks.append(menu)
    print()
    print("-" * 5, "Minuman", "-" * 5)
    for  menu in drinks :
        print(f"{number:<4}{menu['name']:<25} {menu['price']:>18,.0f}") 
        number += 1

#save/load
menus_track = "Menus.csv"
fields= ["type", "name", "price"]
def load() :
    menus = []
    
    try :
        with open(menus_track, "r", newline="") as file :
            for row in csv.DictReader (file) :
                menus.append({
                    "type" : row["type"],
                    "name" : row["name"],
                    "price" : float(row["price"]),
                })
    except FileNotFoundError :
        pass
    
    return menus

def save(menus) :
    with open(menus_track, "w", newline="") as file :
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(menus)
             

if __name__ == '__main__' :
    menus = load()
    indigo_m()
    show_menu(menus)
    save(menus)
    