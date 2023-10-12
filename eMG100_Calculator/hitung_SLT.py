from constant_eMG100 import MAX_CAPACITY_SLT_CARD, KSUS_DEFAULT_SLT, MIN_SLIB8, MIN_SLIU8

def itungan_SLT(user_Input_SLT):
    counter = 0
    SLIB8_card = MIN_SLIB8
    SLIU8_card = MIN_SLIU8

    lebih = user_Input_SLT - KSUS_DEFAULT_SLT

    while(lebih >= MAX_CAPACITY_SLT_CARD):
        if counter % 2 == 0: 
            SLIB8_card += 1
        else:
            SLIU8_card += 1
        counter += 1
        lebih -= MAX_CAPACITY_SLT_CARD

    return SLIB8_card, SLIU8_card