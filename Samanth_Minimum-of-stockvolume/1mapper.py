# providing the input file to the mapper file
input = open("dataset.txt", "r")
# creating the new file to store the output values
output = open("01.txt", "w")

# Iterating the data in the loop to only create the required files.
for line in input:
    datalist = line.strip().split("\t")
    exchange, stock, date, data, low, high, adj, stockvolume, med = datalist
    output.write(stock + "\t" + stockvolume + "\n")

#Closing the files after storing the data
input.close()
output.close()