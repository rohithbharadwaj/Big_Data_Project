#dataset.txt is the file contains all the required data to find the maximum stockvolume 
input = open("dataset.txt", "r")
output = open("01.txt", "w")

#below code is used for strip and split the required fields present in the dataset.txt file and take the output values
#of stock and stockvolume only into another file 01.txt
for line in input:
    datalist = line.strip().split("\t")
    exchange, stock, date, data, low, high, adj, stockvolume, med = datalist
    output.write(stock + "\t" + stockvolume + "\n")

input.close()
output.close()