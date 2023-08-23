""" Generates codons from mRNA"""
def clean_seq(pre_mRNA: str):
    temp = ""
    ignore_list = ["'", "-", "5", "3"]
    for na in pre_mRNA:
        if na in ignore_list:
            pass
        else:
            temp += na
    pre_mRNA = temp
    return pre_mRNA

def codons_gen(pre_mRNA: str):
    codons = []
    for x in range(0, len(pre_mRNA), 3):
        codons.append(pre_mRNA[x:x+3])
    return codons