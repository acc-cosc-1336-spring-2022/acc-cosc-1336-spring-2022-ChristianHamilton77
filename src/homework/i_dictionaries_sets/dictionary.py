#Sample 
dataSet = [['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']]
#print(dataSet[2])

 	 
# Sample Output
# 0.00000 0.40000 0.10000 0.10000 #firstrow
# 0.40000 0.00000 0.40000 0.30000
# 0.10000 0.40000 0.00000 0.20000
# 0.10000 0.30000 0.20000 0.00000



# In the dictionary.py file, write the value return functions:
# get_p_distance with list parameter list1 and list2 (see get p distance above for function code)
# get_p_distance_matrix with list parameter list1 (see general matric function above for function code)
# Use the get_p_distance function to get the distance between two lists, save the result to p_distance_matrix[i][j].

def get_p_distance(list1,list2):
    i = 0
    pDist = 0

    while i < len(list1):
        #print(list1[i], end=", ")
        if list1[i] != list2[i]:
            pDist += 1
        i += 1
    return pDist

def get_p_distance_matrix(list1):   
    #loop length of dataSet and compare list loop to 1 through length of dataSet
    i = 0
    get_p_distance_matrix = []
    while i < len(list1):
        #print(i," : ",dataSet[i])
        j = 0
        #print(len(dataSet[i]))
        ratioList = []
        while j < len(list1):
            p_distance = get_p_distance(list1[i],list1[j])
            ratio = p_distance / len(list1[i])
            #print(ratio)
            ratioList.append(ratio)
            j += 1
        #print(ratioList)
        get_p_distance_matrix.append(ratioList)
        i += 1
        #get Pvalue/length of list stor to p_distance_matrix[i][j]
    return get_p_distance_matrix

# print(get_p_distance_matrix(dataSet))