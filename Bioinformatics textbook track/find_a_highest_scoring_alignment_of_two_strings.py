#解法1 (Biopython)
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def global_align_with_affine(s,t):#global_align_with_affine
    s=s.replace("\n","")
    t=t.replace("\n","")
    
    matrix = matlist.blosum62
    alignments = pairwise2.align.globalds(s, t, matrix,-5,-5)
    best_alignment = alignments[0]
    
    #print pairwise2.format_alignment(*best_alignment)

    print (int(best_alignment[2]))
    print (best_alignment[0])
    print (best_alignment[1])

global_align_with_affine(s,t)


#解法2 (動的計画法）
作成中



