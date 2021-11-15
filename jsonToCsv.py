import json

f = open('csv.csv',"w")
f.write("")
with open('data.json','r')as fp:
    json_data = json.load(fp)
    for i in json_data.keys():
        for j in json_data[i].keys():
            strForWritting = str(j) + "," + str(json_data[i][j]) + "\n"
            print(strForWritting)
            f.write(strForWritting)
f.close()