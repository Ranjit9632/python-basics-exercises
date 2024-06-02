ct_hats = []
numberoftrue = 0
def determinect_hats():
    # create a list of 100 false values in before round 1 which shows no hat on cat
    catswithhat = [False]*100
    # now start from round 1
    for rounds in range(1,101):
        #start with cat 1
        for cats in range(1,101):
            # logic as per the rounds
            if (cats%rounds ==0):
                # cats-1 because catswithhat has index from 0 to 99 which counts to 100 values
                # the for loop for cats end with 100 so cats-1
                if catswithhat[cats-1] == True:
                    catswithhat[cats-1] = False
                else:
                    catswithhat[cats-1] = True
# tracking the indices using below code and storing the index value only if value is true
    true_indexes = [index for index, value in enumerate(catswithhat) if value]
    return (catswithhat.count(True)),(true_indexes)

numberoftrue,index_list = determinect_hats()
print(numberoftrue)

#index+1 should be added because index starts from 0
new_index_list = [x+1 for x in index_list]
print(new_index_list)
