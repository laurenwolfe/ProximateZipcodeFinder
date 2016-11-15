IN_FILE = "../data/2016_Gaz_zcta_national.txt"
OUT_FILE = "../data/zip_coords.tsv"

f1 = open(IN_FILE, 'r')
f2 = open(OUT_FILE, 'w')

for line in f1:
    row = line.split("\t")
    new_row = row[0] + "\t" + row[5] + "\t" + row[6]
    f2.write(new_row)
    print new_row

f1.close()
f2.close()
