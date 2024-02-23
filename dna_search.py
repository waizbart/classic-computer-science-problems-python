from enum import IntEnum
from typing import List, Tuple, Callable
from time import time

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

def test_search(label: str, function: Callable[[Gene, Codon], bool], params):
    start_time = time()
    
    result = function(*params)
    
    print("Label: {}".format(label))
    print("Result: {}".format(result))
    print("Elapsed time: {:.5f}s\n".format(time() - start_time))
    

if __name__ == "__main__":
    gene_str: str = 'ACTGACTGCACGATCGATCGATCGACGCGATTATAGACTACATCGTGACTGATCGA' * 1000000

    my_gene: Gene = string_to_gene(gene_str)
    my_sorted_gene: Gene = sorted(my_gene)

    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)

    test_search("Linear search", linear_contains, (my_gene, acg))
    test_search("Binary search", binary_contains, (my_sorted_gene, acg))