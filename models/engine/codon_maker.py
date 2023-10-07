from typing import List

""" Generates codons from mRNA"""
def clean_seq(pre_seq: str) -> str:
    """
    Removes '5-' and '-3' from sequence
        parameters: mRNA sequences (strings).
        returns plain nucleotide sequences.
    """
    temp = ""
    ignore_list = ["'", "-", "5", "3"]
    for na in pre_seq:
        if na in ignore_list:
            pass
        else:
            temp += na
    pre_seq = temp
    return pre_seq


def codons_gen(pre_mRNA: str) -> List[str]:
    """
    Splits mRNA sequences into lists of codons
        parameters: mRNA sequences (strings).
        returns a list of codons.
    """
    codons = []
    for x in range(0, len(pre_mRNA), 3):
        codons.append(pre_mRNA[x:x+3])
    return codons