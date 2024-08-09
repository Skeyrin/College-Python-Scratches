import pprint
import nltk
import time

kal_tag = open("corpus.txt", "r")
kal_tag = kal_tag.readlines()

startTime = time.time()

for i in range(len(kal_tag)):
	kalimat1 = kal_tag[i]
	kalimatchunk = [nltk.tag.str2tuple(t) for t in kalimat1.split()]  # mengubah ke bentuk tuple
	print("---- Kalimat ke-", i + 1, "-----")
	print(f"kalimat awal = {kalimat1}")
	print(f"kalimat tuple = {kalimatchunk}")

	# rule grammar untk membentuk frasa
	grammar = r"""
			NP : { <N>+ }
			VB : { <V>+ }
			DT : { <D>+ }
			NP : { <NP> <DT>? }
			VB : { <VB> <NP> }
		"""
	cp = nltk.RegexpParser(grammar)
	fileresult = open("hasilCorpus.txt", "w+")
	pp = pprint.PrettyPrinter(indent=4)
	result = cp.parse(kalimatchunk)

	for i, item in enumerate(result):
		if item.count(',') != 0:
			print(",", i, file=fileresult)
		else:
			if item.count('?') != 0:
				print("?", i, file=fileresult)
			else:
				if item.count('!') != 0:
					print("!", i, file=fileresult)
				else:
					if item.count('.') != 0:
						print(".", i, file=fileresult)
					else:
						print(item, i, file=fileresult)

	# print(item,file=fileresult)
	print(result)
	print("Panjang kalimat = ", len(result))
	fileresult.close()
	print(time.time() - startTime)  # ukur waktu proses --akhir
	print("=" * 30)
	result.draw()  # untuk menampilkan grambar tree