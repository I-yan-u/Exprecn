#!/usr/bin/python3
"""
Base class for Nucleotides
"""
from .engine.codon_maker import codons_gen, clean_seq
from .engine.amino_list import amino_acid_codons_rna as acr
from .engine.amino_list import rna_codon_amino_acids as rca
from typing import Union, List


class Exprecn:
    """A class representing a nucleic acid sequence.

    Attributes:
        __NucleicAcid (str): The type of nucleic acid (DNA or RNA).
        __strands (int): The number of strands in the sequence.
        info (dict): Additional information about the sequence.

    Methods:
        __init__(self, template: str, coding=''): Initializes the Exprecn object.
        NucleicAcid(self) -> str: Returns the type of nucleic acid.
        strands(self) -> int: Returns the number of strands in the sequence.
        __str__(self) -> str: Returns a string representation of the sequence.
        transcribe(self, reversed: bool = False) -> str: Transcribes DNA to RNA.
        translate(self, **kwargs) -> Union[list, str]: Translates mRNA into an amino acid chain.
        to_dict(self) -> dict: Converts the Exprecn object to a dictionary.
    """
    def __init__(self, template: str = None, coding: str = None) -> None:
        """Initializes the Exprecn object.

        Args:
            template (str, optional): The template strand of the nucleic acid sequence. Defaults to None.
            coding (str, optional): The coding strand of the nucleic acid sequence. Defaults to None.

        Raises:
            ValueError: If the sequence contains invalid characters.
            ValueError: If the sequence is not a string.
        """
        self.template = None
        self.coding = None
        self.__NucleicAcid = None
        self.__strands = 0
        self.info = {'status': ''}

        # Check if the input sequences are strings
        if template is not None and not isinstance(template, str):
            self.info['status'] = 'Invalid sequence, input should be a string'
            return

        if coding is not None and not isinstance(coding, str):
            self.info['status'] = 'Invalid sequence, input should be a string'
            return

        if template is None:
            return

        # Check for invalid characters in the template strand
        ignore_chars = {'b', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 'v', 'w', 'x', 'y', 'z'}
        invalid_chars = set(template.lower()) & ignore_chars
        if invalid_chars:
            char = invalid_chars.pop()
            ind = template.lower().index(char)
            self.info['status'] = f'Invalid nucleotide {char} at index {ind}'
            return

        # Check for valid RNA sequence
        if 'U' in template.upper() and 'T' not in template.upper():
            self.template = template.upper()
            self.__NucleicAcid = 'RNA'
            self.__strands = 1
            self.info['status'] = 'Single strand RNA'
            return

        # Check for valid DNA sequence
        if 'U' in template.upper() and 'T' in template.upper():
            self.info['status'] = 'Invalid sequence'
            return

        if len(template) <= 2:
            self.info['status'] = 'Invalid sequence, sequence too short'
            return

        self.template = template.upper()
        self.__NucleicAcid = 'DNA'
        
        # Check for single or double strand DNA
        self.coding = coding.upper() if coding is not None else ''
        if self.coding == '' and self.template != '':
            self.__strands = 1
            self.info['status'] = 'Single strand DNA'
        elif self.template != '':
            self.__strands = 2
            self.info['status'] = 'Double strand DNA'
        if self.__strands == 2 and not self.complementary():
            self.template = None
            self.coding = None
            self.__NucleicAcid = None
            self.__strands = 0
            self.info['status'] = 'Invalid sequence, strands are not complementary'
            return

    @property
    def NucleicAcid(self) -> str:
        """Returns the type of nucleic acid (DNA or RNA)."""
        return self.__NucleicAcid

    @property
    def strands(self) -> int:
        """Returns the number of strands in the sequence."""
        return self.__strands

    def __str__(self) -> str:
        """Returns a string representation of the sequence."""
        if self.__NucleicAcid == None or self.__NucleicAcid == '':
            return 'None'
        elif self.__NucleicAcid == 'DNA':
            return '({}) - {} Strands\n\'3-{}-5\'\n\'5-{}-3\'\n{}'\
                    .format(self.__NucleicAcid, self.__strands,
                            self.template, self.coding, self.info)
        else:
            return '({}) - {} Strand\n\'3-{}-5\'\n{}'\
                    .format(self.__NucleicAcid, self.__strands, self.template, self.info)
        
    def complementary(self, seq: str = None) -> bool:
        """Returns the complementary DNA sequence."""
        base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        if self.__strands == 2:
            if len(self.template) != len(self.coding):
                return False
            
            for b1, b2 in zip(self.template, self.coding):
                if base_pairs[b1] != b2:
                    return False
            return True
        elif seq:
            if len(seq) != len(self.template):
                return False
            for b1, b2 in zip(self.template, seq):
                if base_pairs[b1] != b2:
                    return False
            return True
        
    def replicate(self, force: bool = False) -> str:
        """Replicates the DNA sequence.
        `Args`:
            `force` (bool, optional): <RNA only> Specifies if the RNA sequence should be replicated forcefully.
            Defaults to False.

        `Returns`:
            str: The replicated DNA sequence.
        """
        base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A'}
        if self.__NucleicAcid == 'DNA':
            new_strand_temp = ''
            new_strand_coding = ''
            for nucleotide in self.template:
                new_strand_temp += base_pairs[nucleotide.upper()]
            if self.__strands == 2:
                for nucleotide in self.coding:
                    new_strand_coding += base_pairs[nucleotide.upper()]
            return Exprecn(new_strand_temp, new_strand_coding)

        elif self.__NucleicAcid == 'RNA':
            if force:
                new_strand = ''
                reversed = [nb for nb in clean_seq(self.transcribe(reversed=True))]
                for nucleotide in reversed:
                    new_strand += base_pairs[nucleotide.upper()]
                return Exprecn(new_strand)

            return 'Cannot replicate RNA'

    def transcribe(self, reversed: bool = False) -> str:
        """Transcribes DNA to RNA.

        Args:
            reversed (bool, optional): Specifies if RNA should be reversed transcribed. Defaults to False.

        Returns:
            str: The transcribed (or reversed) sequence.
        """
        if self.__NucleicAcid == 'RNA':
            if reversed == True:
                new_strand = ''
                base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A'}
                for nucleotide in self.template:
                    new_strand += base_pairs[nucleotide.upper()]
                return "'5-{}-3'".format(new_strand)
            else:
                return "'3-{}-5'".format(self.template)
        elif self.__NucleicAcid == 'DNA':
            base_pairs = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
            new_strand = ''
            if self.template != '':
                for nucleotide in self.template:
                    new_strand += base_pairs[nucleotide.upper()]
                return "'5-{}-3'".format(new_strand)
        else:
            return None

    def translate(self, **kwargs) -> Union[List, str]:
        """Translates mRNA into an amino acid chain.

        Args:
            **kwargs: Additional keyword arguments.
                meth (bool): Specifies if methionine should appear in the output. Defaults to True.
                ret: Specifies the return format (choose 'list' to return a list). Defaults to string format.

        Returns:
            list or str: The list or string chain of amino acids.
        """
        mRNA = ''
        if self.__NucleicAcid == 'DNA':
            mRNA = self.transcribe()
        elif self.__NucleicAcid == 'RNA':
            mRNA = self.template
        else:
            return 'Not a nucleic acid', []
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
                return 'Success', amino_chain
            elif kwargs.get('meth') == False:
                amino_chain = ''
                for ac in range(1, len(amino_chain_struct) - 1):
                    amino_chain += amino_chain_struct[ac] + '-'
                amino_chain += amino_chain_struct[-1]
                return 'Success', amino_chain

    def to_dict(self):
        """Converts the Exprecn object to a dictionary."""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict