#
# In the strings.py file, write the value return functions:
# get_hamming_distance with string parameter dna1 and dna2 (see hamming distance above for function code)
# get_dna_complement with string parameter dna (see complements above for function code)
    #In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'
def get_hamming_distance(dna1,dna2):
    i = 0
    ham = 0

    while i < len(dna1):
        #print(dna1[i], end=", ")
        if dna1[i] != dna2[i]:
            ham += 1
        i += 1
    return ham
   

def get_dna_complement(dna):
    #print(dna)
    complement = ''
    for n in dna:
        if n == 'A':
            complement += 'T'
        elif n == 'T':
            complement += 'A'
        elif n == 'C':
            complement += 'G'
        elif n == 'G':
            complement += 'C'
    return complement[::-1]


# dna1 = 'GAGCCTACTAACGGGAT'
# dna2 = 'CATCGTAATGACGGCCT'
# dna = 'AAAACCCGGT'
# print(get_hamming_distance(dna1,dna2))
# print(get_dna_complement(dna))

