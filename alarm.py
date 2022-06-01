import csv
import json
with open("an.csv", "r") as mycsvfile:
        heading = next(mycsvfile)
        heading = heading.rstrip("\n")
        split_head = heading.split(",")
        reader = csv.reader(mycsvfile)
        data = []
        count = 0
        # print(type(reader))

        for row in reader:
          inner = dict()
          for i in row:
            inner[split_head[count]] = i             
            count +=1   
          data.append(inner)
          print(data)
          count = 0
        # print(data);
        # for i,r in reader.items():
        #   # data.append({r: r})
        #   print(i,r)
        # for row in reader:
        #   print(type(reader))
          # for i in len(row[0]):
          #   print(row[i])
            # print(i)
          # cont = split_head[count]
          # rowin = len(row)
          # data.append({split_head[count]: row[count], count += 1})
          
          
          # count += 1
          # for headIn,rowIn in zip(head,row):
          
            
        
        #     for words in row:
        #         data.append({"Hello": words})
        # print(data)        
            # data.append({split_head[count]: row[count]})
            # count += 1

            # data.append({split_head[0]: row[0], split_head[1]: row[1], split_head[2]
            #                 : row[2], split_head[3]: row[3], split_head[4]: row[4]})