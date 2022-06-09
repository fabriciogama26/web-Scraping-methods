import json

with open("ao_vivo.json") as f:
    jsondata = json.load(f)


for i in jsondata["Result"]["Items"][0]["Events"]:

    #print( i["ChampName"], "|",  i["Name"])
    ChampName = i["ChampName"]
    Namejogo = i["Name"]

    for i in jsondata["Result"]["Items"][0]["Events"][0]["Items"]:
        try:
            #print(i["Items"][0]["Price"])
            #print(i["Items"][1]["Price"])
            #print(i["Items"][2]["Price"])
            Price0 = i["Items"][0]["Price"]
            Price1 = i["Items"][1]["Price"]
            Price2 = i["Items"][2]["Price"]

        except:
            pass
            
        for i in jsondata["Result"]["Items"][0]["Events"][0]["Items"]:
                try:       
                    #print(i["Items"][0]["Name"])
                    #print(i["Items"][1]["Name"])
                    #print(i["Items"][2]["Name"])
                    Nameaposta = i["Items"][0]["Name"]
                    Nameaposta1 = i["Items"][1]["Name"]
                    Nameaposta2 = i["Items"][2]["Name"]   

                    print(ChampName, "|", Namejogo,"|", Price0, "|", Price1, "|", Price2, "|", Nameaposta, "|", Nameaposta1, "|", Nameaposta2)

                except:
                    pass



    
       

            
       



   
   