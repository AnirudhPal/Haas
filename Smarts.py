## Import Libs
from math import e

## Parameters: Configured during Runtime.
# Name of Input File (NOTE: Has to be in same folder).
DATA_FILE = 'MasterData1.csv'
# Name of OUTPUT File (NOTE: Has to be in same folder).
OUT_FILE = 'OUT.csv'

## Config Vars
# Verbal Prompts
VERBOSE = True

## Global Vars
# Model Array
model_arr = []

## Class
# Reviwe Class
class Model:
    # Constructor
    def __init__(self):
        # Members
        self.county = ''
        self.avgWind = 0;
        self.landAvail = 0;
        self.landPrice = 0;
        self.elecPrice = 0;
        self.profitability = 0;

    # Getters
    def getCounty(self):
        return self.county
    def getWind(self):
        return self.avgWind
    def getLand(self):
        return self.landAvail
    def getRent(self):
        return self.landPrice
    def getElectric(self):
        return self.elecPrice
    def getProfit(self):
        return self.profitability

    # Setter
    def setCounty(self, name):
        self.county = name
    def setWind(self, wind):
        self.avgWind = wind
    def setLand(self, land):
        self.landAvail = land
    def setRent(self, price):
        self.landPrice = price
    def setElectric(self, price):
        self.elecPrice = price
    def setProfit(self, profit):
        self.profitability = profit

## Helper Functions
# Compute Data
def compute():
    # Global Reference
    global model_arr

    # Constants
    IP_t = 2.75

    # Iterate
    for model in model_arr:
        # PG_T
        PG_t = 1.5241 * (e ** (0.0501 * model.getWind()))

        # PG_TY
        PG_ty = PG_t * 365.0 * 24.0

        # R_TYC
        R_tyc = PG_ty * model.getElectric()

        # CO_TY
        CO_ty = IP_t * 75000.0

        # C_T
        C_t = 0.0#4000000.0

        # L_T
        L_t = 500.0 / 100.0

        # CR_T
        CR_t = L_t * model.getRent()

        # P_TYC
        P_tyc = R_tyc - C_t - CO_ty - CR_t

        # Set the Value
        model.setProfit(P_tyc)

    if VERBOSE:
        # Check Model
        for model in model_arr:
            # Print
            print model.getCounty() + ', ' + str(model.getProfit()) + ', ' + str(model.getLand())

# Input Data from File to Array from given Filename
def loadData():
    # Global Reference
    global model_arr

    # Open File
    fd = open(DATA_FILE, 'r')

    # Load Data
    data = fd.read()

    # Close File
    fd.close()

    # Split by Lines
    lines = data.split('\n')

    # Remove First Entry
    lines = lines[1:]

    # Create Model
    for i in lines:
        # Create Object
        model = Model()

        # Split by Entry
        entrys = i.split(',')

        # Error???
        if len(entrys) < 5:
            continue

        # Add County
        model.setCounty(entrys[0])

        # Add Rent
        model.setRent(float(entrys[1]))

        # Add Land
        model.setLand(float(entrys[2]))

        # Add Elec
        model.setElectric(float(entrys[3]))

        # Add Wind
        model.setWind(float(entrys[4]))

        # Add to Array
        model_arr.append(model)

    if VERBOSE:
        # Check Model
        for model in model_arr:
            # Print
            print model.getCounty() + ', ' + str(model.getRent()) + ', ' + str(model.getLand()) + ', ' + str(model.getElectric()) + ', ' + str(model.getWind()) + '\n'

## Main Block
def main():
    # Load Data
    loadData()

    # Compute
    compute()

main()
