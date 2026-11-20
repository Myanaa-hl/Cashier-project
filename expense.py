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
        
        ctg = input ("[Bahan, Karyawan, Operasional, Lainnya] Silahkan Pilih: ").strip().lower()
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
        exp.append({"times" : time_exp  ,"expense" : ctg, "notes" : notes, "nominal" : nominal})
        
def show_expense(exp) :
    
    if len(exp) == 0 :
        print("Belum Ada Data Yang Terisi!")
        return
    
    print("-" * wides)
    print(f"{'Expense Recap':^{wides-2}}")
    print("-" * wides)
    
    print(f"{'No':<3} {'Date':<10} {'Category':<10} {'Notes':<20} {'Subtotal':>11}")
    print("-" * wides)
    for number, expense in enumerate(exp, 1) :
        print(f"{number:<3} {expense['times']:<10} {expense['expense']:<10} {expense['notes']:<15} : {expense['nominal']:>12,.0f}")
        
        st = 0 + expense['nominal'] 
    print("-" * wides)
    print(f"{'Total':<5} : {st:>52,.0f}")
