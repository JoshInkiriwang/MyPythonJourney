from constant_eMG100 import KSUS_DEFAULT_SLT, MIN_SLIB8, MIN_SLIU8, MAX_CAPACITY_SLT_CARD, MAX_CAPACITY_CO_CARD, MIN_COIU4, MAX_COIU4

def itungan_SLT(userInput):
    # LocalVariabel
    SLIB8 = MIN_SLIB8
    SLIU8 = MIN_SLIU8
    default = KSUS_DEFAULT_SLT
    capacity_SLT = MAX_CAPACITY_SLT_CARD

    # Bawaan SLT di eMG100 ada 6 SLT
    lebih = userInput - default

    while(lebih > 0):
        SLIB8 += 1 # Menggunakan satu card SLT (SLIB8)
        lebih -= capacity_SLT # Dikurangi dengan kapasitas card SLIB8

        if lebih > 0 :
            SLIU8 += 1 # Menggunakan satu card SLT (SLIU8)
            lebih -= capacity_SLT # Dikurangi dengan kapasitas card SLIU8
        else :
            break
    
    return SLIB8, SLIU8
    
def itungan_CO(userInput): 
    # LocalVariabel
    COIU4 = MIN_COIU4
    capacity_CO = MAX_CAPACITY_CO_CARD

    lebih = userInput - capacity_CO
    while lebih >= 0 :
        COIU4 += 1
        lebih -= capacity_CO

    return COIU4

def main():
    input_SLT = int(input("Berapa Telepon Single Line ? "))
    input_COLine = int(input("Berapa banyak line telkom ? "))

    count_SLIB8, count_SLIU8 = itungan_SLT(input_SLT)
    count_COIU4 = itungan_CO(input_COLine)

    print(f"Jumlah Card SLIB8 : {count_SLIB8}")
    print(f"Jumlah Card SLIU8 : {count_SLIU8}")
    print(f"Jumlah Card COIU4 : {count_COIU4}")

    total_slt = (count_SLIB8 + count_SLIU8) * MAX_CAPACITY_SLT_CARD + KSUS_DEFAULT_SLT
    total_co = count_COIU4 * MAX_CAPACITY_CO_CARD
    
    print(f"Total : \n Single Line Telephone : {total_slt} \n CO Line : {total_co}")

if __name__ == "__main__" :
    main()