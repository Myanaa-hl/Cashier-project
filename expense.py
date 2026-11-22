import csv
import time


wides = 60

def add_expense(exp, categories) :
    print()
    
    print("-" * wides)   
    print(f"{"Indigo's Expense":^{wides-2}}")
    print("-" * wides)
    print("FYI Ketik done Jika Selesai")
    print()
    while True :
        
        ctg = input ("[Bahan, Karyawan, Keperluan, Lainnya] Silahkan Pilih: ").strip().lower()
        if ctg == "done" :
                break
        elif ctg not in categories :
            print("Tolong isi Sesuai Pilihan Yang Ada!")
            continue
        elif ctg.isdigit() :
            print("Tidak Boleh Angka!")
            continue
        elif ctg == "" :
            print("Tidak Boleh Kosong!")    
            continue
        
        notes = input("Silahkan Ketik Keterangannya: ").strip()
        if notes == "" :
            print("Tidak Boleh Kosong!")
            continue
        elif notes.isdigit() :
            print("Tidak Boleh Angka!")
        
        try :
            nominal = float(input("Isi Nominalnya: "))
        except ValueError :
            print("Tolong Isi Dengan Angka!")
            continue
        if nominal <= 0 :
            print("Tidak Boleh 0 Dan Kurang Dari 0!")
            continue
            
        time_exp = time.strftime("%Y-%m-%d")
        exp.append({"times" : time_exp  ,"items" : ctg, "notes" : notes, "nominal" : nominal})
        
def show_expense(exp) :
    
    if len(exp) == 0 :
        print("Belum Ada Data Yang Terisi!")
        return
    
    print("-" * wides)
    print(f"{'Expense Recap':^{wides-2}}")
    print("-" * wides)
    
    print(f"{'No':<3} {'Date':<10} {'Category':<8} {'Notes':>20} {'Subtotal':>15}")
    print("-" * wides)
    st = 0
    for number, expense in enumerate(exp, 1) :
        print(f"{number:<3} {expense['times']:<10} {expense['items']:<10} {expense['notes']:>20} : {expense['nominal']:>11,.0f}")
        st += expense['nominal'] 
        
    print("-" * wides)
    print(f"{'Total':<5} : {st:>52,.0f}")
     
#exp load    
ex_track = "expense.csv"
fields = ["times","items", "notes", "nominal"]
def exp_load() :
    exp = []
    
    try :
        with open(ex_track, "r", newline="") as file :
            for row in csv.DictReader(file) :
                exp.append({
                    "times" : row['times'],
                    "items" : row['items'],
                    "notes" : row['notes'],
                    "nominal" : float(row['nominal'])
                    })
    except FileNotFoundError :
        pass 
    return exp

def save_exp(exp) :
    with open(ex_track, "w", newline="") as file :
        writer = csv.DictWriter (file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(exp)
 