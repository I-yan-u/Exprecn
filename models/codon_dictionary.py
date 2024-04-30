"""
Codon dictionary
"""

from .engine.codon_maker import codons_gen, clean_seq
from models.engine.amino_list import amino_acid_codons_rna as acr
from models.engine.amino_list import rna_codon_amino_acids as rca