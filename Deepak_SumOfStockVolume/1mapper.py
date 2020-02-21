input = open("dataset.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    exchange, stock, date, data, low, high, adj, stockvolume, med = datalist
    output.write(stock + "\t" + stockvolume + "\n")

input.close()
output.close()