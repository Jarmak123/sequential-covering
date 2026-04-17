from itertools import combinations


#combinations funkcja
def get_data():
    obiekty = {}
    with open('data.txt', 'rt') as myfile:
        contents = myfile.readlines()

    for i in range(len(contents)):
        etykieta = "o"+str(i+1)
        atrbuty = list((contents[i].rstrip('\n').replace(" ",'')))
        del atrbuty[-1]
        obiekty[etykieta] = [atrbuty, list((contents[i].rstrip('\n').replace(" ",'')))[len(list((contents[i].rstrip('\n').replace(" ",''))))-1]]

    return obiekty


def zbiory(data, liczenosc):
    for key, value in data.items():
        zbior = combinations(value[0], liczenosc)
        value[0] = list(zbior)

    return data

def printData(dict):
    print("      'a1' 'a2' 'a3' 'a4' 'a5' 'a6' 'd'")
    for key, value in dict.items():
        print(f"{key}: {value}")

def printResult(dict):
    for key, value in dict.items():
        print(f"z {key} ({value[0]} => (d = {value[len(value)-1]}")


def main():
    global new_data
    result = {}
    data = get_data()
    printData(data)
    i=1

    while True:
        if len(result) == len(data): break
        if i>1: new_data = zbiory(data, i)
        pokrycie = 0

        if new_data:
            act_data = new_data
        else:
            act_data = data

        #głóna petla
        for x in range(len(act_data)):
            for i in act_data[x][0]:
                for y in range(len(act_data)):
                    pass

        i+=1
        pokrycie = 0

    printResult(result)





if __name__ == "__main__":
    main()
