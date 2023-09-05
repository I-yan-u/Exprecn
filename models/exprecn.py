#!/usr/bin/python3
"""
Base class for Nucleotides
"""
from .engine.codon_maker import codons_gen, clean_seq
from models.engine.amino_list import amino_acid_codons_rna as acr
from models.engine.amino_list import rna_codon_amino_acids as rca

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
        """ 
        Transcribe DNA to RNA.
        arguments
            reversed(bool): specifies if RNA should be reversed transcribed.
        returns
            transcribed (or reversed) sequence
        """
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
            if self.template != '':
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
            else:
                for nucleotide in self.coding:
                    if nucleotide.upper() == 'A':
                        new_strand += 'U'
                    elif nucleotide.upper() == 'T':
                        new_strand += 'A'
                    elif nucleotide.upper() == 'C':
                        new_strand += 'G'
                    else:
                        new_strand += 'C'
                return "'5-{}-3'".format(new_strand)

    def translate(self, **kwargs):
        """
        Translates mRNA into AminoAcid chain.
        arguments
            meth (bool): Specifies if methionine should appear in output (True by default)
            ret: Specifies return format (choose 'list' to return a list).
                 default is string format.
        return
            List or string chain of amino acid.            
        """
        mRNA = ''
        if self.__NucleicAcid == 'DNA':
            mRNA = self.transcribe()
        else:
            mRNA = self.coding
        codons = codons_gen(clean_seq(mRNA))
        start = False
        amino_chain_struct = []
        if 'AUG' in codons:
            for codon in codons:
                if codon == 'AUG':
                    start = True
                if start == True:
                    for k, v in rca.items():
                        if len(codon) == 3 and codon == k:
                            if codon in ['UAA', 'UAG', 'UGA']:
                                start = False
                            amino_chain_struct.append(v)
                        else:
                            pass
        else:
            return 'No start codon found', codons
        if kwargs.get('ret', None) == 'list':
            if kwargs.get('meth', True) == True:
                return amino_chain_struct
            else:
                amino_chain_struct.remove('Methionine')
                return amino_chain_struct
        else:
            if kwargs.get('meth', True) == True and 'Methionine' in amino_chain_struct:
                amino_chain = ''
                for ac in range(len(amino_chain_struct) - 1):
                    amino_chain += amino_chain_struct[ac] + '-'
                amino_chain += amino_chain_struct[-1]
                return amino_chain
            elif kwargs.get('meth') == False:
                amino_chain = ''
                for ac in range(1, len(amino_chain_struct) - 1):
                    amino_chain += amino_chain_struct[ac] + '-'
                amino_chain += amino_chain_struct[-1]
                return amino_chain

    def to_dict(self):
        """Converts class object to dictionary"""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict