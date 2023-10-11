"""
This code determines a milk product recommendation based on the user's age input.

Define a dictionary for constant values 
The dictionary is named by MILK_CONSTANTS.

N stands for Nutrisi or Nutrision Milk.
C stands for Kalsium or Calcium Milk.
"""

MILK_CONSTANTS = {
    "N1": "Nutrisi AHA - DHA",
    "N2": "Nutrisi Active",
    "N3": "Nutrisi Teen",
    "C1": "Calcium Teen",
    "C2": "Calcium Active",
    "C3": "Calcium Gold"
}

def get_milk_product(age):
    if age <= 5:
        return MILK_CONSTANTS["N1"]
    elif age <= 10:
        return MILK_CONSTANTS["N2"]
    elif age <= 17:
        return MILK_CONSTANTS["N3"]
    elif age <= 25:
        return MILK_CONSTANTS["C1"]
    elif age <= 50:
        return MILK_CONSTANTS["C2"]
    else:
        return MILK_CONSTANTS["C3"]

try:
    input_age = int(input("Masukkan umur anda = "))
    
    if input_age >= 0:
        recommended_milk = get_milk_product(input_age)
        print(recommended_milk)
    else:
        print("Masukan Umur Diatas 0 Tahun")

except ValueError:
    print("Masukkan umur dalam bentuk angka (integer).")
