dna_strand_1= "ATC-CGG-GAC-CAG-CIG-GCC-GTC" #TAG-GCC-CTG-GTC-GAC-CGG-CAG

dna_strand_2 = ""

for x in range(len(dna_strand_1)):
    char = dna_strand_1[x]
    print(char,end = "',")

    if char == "A":
        dna_strand_2 +="I"
    if char == "I":
        dna_strand_2 += "A"
    if char == "C":
        dna_strand_2 +="G"
    if char == "G":
        dna_strand_2 +="C"
    else:
        dna_strand_2 +=char

print (dna_strand_2)
