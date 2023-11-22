from Bio import ExPASy
from Bio import SeqIO
from Bio.ExPASy import Prosite
from Bio.ExPASy import ScanProsite

handle = ExPASy.get_prosite_raw('PS51442')
record = Prosite.read(handle)

print(record.description)
print(record.pdb_structs[:10])

handle = ExPASy.get_prosite_raw('PS50001')
record = Prosite.read(handle)

print(record.pattern)

prot_record =  SeqIO.read('seq3.FA',format = 'fasta')
len(prot_record.seq)

handle = ScanProsite.scan(seq=prot_record.seq, mirror="https://prosite.expasy.org/")
result = ScanProsite.read(handle)
result.n_match
