#!/usr/bin/python3
"""
Base class for Nucleotides
"""


class Nucleic_Acid:
    """ Nucleic acid class """
    __NucleicAcid = 'DNA'  # DNA or RNA
    __strands = 2  # DNA = 2, RNA = 1

    def __init__(self, strand1: str, strand2=''):
        """Defines the nucleic acid"""
        if strand1 is None and strand2 is None:
            return None
        if strand2 == '' and 'U' in strand1.upper():
            self.lead = strand1.upper()
            self.__NucleicAcid = 'RNA'
            self.__strands = 1
        else:
            self.lead = strand1.upper()
            self.lag = strand2.upper()
            self.__NucleicAcid = 'DNA'
            self.__strands = 2

    @property
    def NucleicAcid(self):
        return self.__NucleicAcid

    @property
    def strands(self):
        return self.__strands

    def __str__(self) -> str:
        if self.__NucleicAcid == 'DNA':
            return '({}) - {} Strands\n\'5-{}-3\'\n\'5-{}-3\''\
                    .format(self.__NucleicAcid, self.__strands,
                            self.lead, self.lag)
        else:
            return '({}) - {} Strand\n\'5-{}-3\''\
                    .format(self.__NucleicAcid, self.__strands, self.lead)


class Nucleotides:
    """ Nucleotides class"""
    __components = ['phosphate', 'sugar', 'Nitrogenous Base']
    __types = {
        'purines': {
            'A': 'adenine',
            'G': 'guanine'
        },

        'pyrimidines': {
            'C': 'cytosine',
            'T': 'thymine',
            'U': 'uracil'
        }
    }

    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    lead = 'actgtggcagactgtgcacatg'
    lag = 'actgtggcagactgtgcacatg'

    na = Nucleic_Acid(lead, lag)
    print(na.NucleicAcid)
