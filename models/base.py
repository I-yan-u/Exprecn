#!/usr/bin/python3
"""
Base class for Nucleotides
"""
from engine.codon_maker import codons_gen, clean_seq

class Exprecn:
    """ Nucleic acid class """
    __NucleicAcid = 'DNA'  # DNA or RNA
    __strands = 2  # DNA = 2, RNA = 1

    def __init__(self, coding: str, template=''):
        """Defines the nucleic acid"""
        if type(coding) != str and type(template) != str:
            self.coding = None
            self.template = None
            self.__NucleicAcid = ''
            self.__strands = 0
            return None
        else:
            if template == '' and 'U' in coding.upper():
                self.coding = coding.upper()
                self.template = ''
                self.__NucleicAcid = 'RNA'
                self.__strands = 1
            else:
                self.coding = coding.upper()
                self.template = template.upper()
                self.__NucleicAcid = 'DNA'
                self.__strands = 2

    @property
    def NucleicAcid(self):
        """ Returns nucleic acid type. (DNA or RNA) """
        return self.__NucleicAcid

    @property
    def strands(self):
        """ Returns number of strands in sequence """
        return self.__strands

    def __str__(self) -> str:
        """ String representation"""
        if self.__NucleicAcid == '':
            return 'None'
        elif self.__NucleicAcid == 'DNA':
            return '({}) - {} Strands\n\'5-{}-3\'\n\'3-{}-5\''\
                    .format(self.__NucleicAcid, self.__strands,
                            self.coding, self.template)
        else:
            return '({}) - {} Strand\n\'5-{}-3\''\
                    .format(self.__NucleicAcid, self.__strands, self.coding)

    def transcribe(self, reversed=False):
        """ Transcribe DNA to RNA """
        if self.__NucleicAcid == 'RNA':
            if reversed == True:
                new_strand = ''
                for nucleotide in self.coding:
                    if nucleotide.upper() == 'A':
                        new_strand += 'T'
                    elif nucleotide.upper() == 'U':
                        new_strand += 'A'
                    elif nucleotide.upper() == 'C':
                        new_strand += 'G'
                    else:
                        new_strand += 'C'
                return "'3-{}-5'".format(new_strand)
            else:
                return "'5-{}-3'".format(self.coding)
        if self.__NucleicAcid == 'DNA':
            new_strand = ''
            for nucleotide in self.template:
                if nucleotide.upper() == 'A':
                    new_strand += 'U'
                elif nucleotide.upper() == 'T':
                    new_strand += 'A'
                elif nucleotide.upper() == 'C':
                    new_strand += 'G'
                else:
                    new_strand += 'C'
            return "'5-{}-3'".format(new_strand)

    def translate(self):
        """Translates mRNA into AminoAcid chain."""
        mRNA = self.transcribe()
        codons = codons_gen(clean_seq(mRNA))
        ...