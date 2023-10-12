from hitung_SLT import itungan_SLT


def main():
    input_SLT = int(input("Berapa Telepon Single Line ? "))

    count_SLIB8, count_SLIU8 = itungan_SLT(input_SLT)

    # if(jumlah_pabx > 1) :
    #     print("01 x eMG-100 : EXPCABLE")

    print(f"Jumlah Card SLIB8 : {count_SLIB8}")
    print(f"Jumlah Card SLIU8 : {count_SLIU8}")

if __name__ == "__main__" :
    main()