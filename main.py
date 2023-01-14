from model.daftar_nilai import *
from view.view_nilai import *


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("[> Project UAS                                     <]")
print("[> FAQIH IRIANTO (312210021)                       <]")
print("[> TI.22.C1                                        <]")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    print("\n")
    menu = input("(L) Lihat, (T) Tambah, (U) Ubah, (H) Hapus, (C) Cari, (E) Exit\nPilih menu: ")
    print("\n")

    if menu.lower() == 't':
        tambah_data()

    elif menu.lower() == 'l':
        lihat_data()

    elif menu.lower() == 'u':
        ubah_data()

    elif menu.lower() == 'h':
        hapus_data()

    elif menu.lower() == 'c':
        cari_data()

    elif menu.lower() == 'e':
        break

    else:
        print("Something went wrong, Please try again!")