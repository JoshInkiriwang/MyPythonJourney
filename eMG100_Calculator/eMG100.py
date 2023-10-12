from constant_eMG100 import KSUS_DEFAULT_SLT, MIN_SLIB8, MIN_SLIU8, MAX_SLIB8, MAX_SLIU8
from hitung_SLT import itungan_SLT

def main():
    count_SLIB8, count_SLIU8 = itungan_SLT(KSUS_DEFAULT_SLT, MIN_SLIB8, MIN_SLIU8, MAX_SLIB8, MAX_SLIU8)

    print(f"Jumlah Card SLIB8 : {count_SLIB8}")
    print(f"Jumlah Card SLIU8 : {count_SLIU8}")

if __name__ == "__main__" :
    main()