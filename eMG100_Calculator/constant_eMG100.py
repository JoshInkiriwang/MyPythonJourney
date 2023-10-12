# A maximum number for extend PBX
THRESHOLD_MAX_KSUS = 2

# This section is for default configuration of PBX 
KSUS_DEFAULT_SLT = 6 # Default Single Line Telephone Slot for PBX
KSUS_DEFAULT_DISPLAY = 2 # Default Digital Phone Slot for PBX
KSUS_DEFAULT_CO = 0 # Default CO Line Slot for PBX

# Section Card untuk Digital Telephone (Universal Slot)
MAX_DTIB = 2 # This is a main card for Display Key Telephone, 
# DTIB have a daughter slot for COIU2/COIU4/SLIU8
MAX_CAPACITY_DISPLAY_CARD = 8 # This is a capacity for DTIB8

# Section Card untuk Single Line Telephone (Universal Slot)
MIN_SLIB8 = 0 # This is a main card for Single Line Telephone
MIN_SLIU8 = 0 # SLIU8 can attach on SLIB8
MAX_CAPACITY_SLT_CARD = 8 # This is a capacity for SLIB8 and SLIU8

# Section Card untuk CO-Line (Trunk Slot)
MAX_CAPACITY_CO_CARD = 4 # This is a capacity for COIU4
MAX_COIU4 = 2 # Maximum number for COIU4
MIN_COIU4 = 0 # Minimum number for COIU4

