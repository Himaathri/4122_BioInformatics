def Brutr_force_motif_search(s,t):
	score=[]
	for i in range (len(s)-len(t)+1):
		match=True
		for j in range (len(t)):
			if s[i+j] != t[j]:
				match=False
				break
		if match:
			score.append(i)
	print(score)
		
		
t = 'TCCA'
s = 'CTTCACCATCAACTTCGCTCGAAGCTGCCTTCCACTCCAACTTCACAACTTCCTCAACTTCCTCACCAACTTCAGCAACTTCTCTAGGGCCAACTTCCAACTTCTCAACTTCTCAACTTCCAACTTCCGACAACTTAACTTCTACACGCAACTTCCAACTTCTGGTCCCAACTTCATAACTTCAGTCAACTTC'

Brutr_force_motif_search(s,t)
