from constant_eMG100 import MAX_CAPACITY_SLT_CARD

def itungan_SLT(default, min_SLIB8, min_SLIU8, max_SLIB8, max_SLIU8):
    counter = 0
    SLIB8_card = 0
    SLIU8_card = 0

    input_SLT = int(input("Berapa Telepon Single ? "))
    
    # 0 tersebut berarti jumlah terkecil untuk Single Line Telephone
    if 0 <= input_SLT <= default :
        return 0 # Tidak perlu card tambahan untuk Single Line Telephone
    else : 
        lebih = input_SLT - default
        while(lebih >= MAX_CAPACITY_SLT_CARD and SLIU8_card <= 2) :
            if counter % 2 == 0: 
                lebih -= MAX_CAPACITY_SLT_CARD
                SLIB8_card += 1
            else :
                lebih -= MAX_CAPACITY_SLT_CARD
                SLIU8_card += 1
            counter += 1
        else:
            pass

        return SLIB8_card, SLIU8_card