import csv


def add_expense(exp, categories) :
    print("FYI Ketik done Jika Selesai")
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
        
        exp.append({"expense" : ctg, "notes" : notes, "nominal" : nominal})
        
def show_expense(exp) :
    
    if len(exp) == 0 :
        print("Belum Ada Data Yang Terisi!")
        return
    
    print("-" * len(exp))
    print(f"{'Expense Recap':^{len(exp)-2}}")
    print("-" * len(exp))

    for number, expense in enumerate(exp, 1) :
        print(f"{number:<5} {expense['expense']:>10}\n\n {expense['notes']:>8} : {expense['nominal']:>10,.0f}")