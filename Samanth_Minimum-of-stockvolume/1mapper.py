input = open("try.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    exchange, stock, stockvolume, data, low, high, adj, date, med = datalist
    output.write(stock + "\t" + date + "\n")

input.close()
output.close()