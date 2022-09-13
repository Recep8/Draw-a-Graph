import matplotlib.pyplot as plt

with open("SAGIM39.TXT","r") as file:
    liste = []
    content_of_file = file.read()
    content_of_file = content_of_file.split("\n")
    kg = '7.776'
    data_id = []
    milisaniye = []
    signal1 = []
    signal2 = []
    signal3 = []
    signal4 = []
    signal5 = []
    signal6 = []
    data = []

    for i in content_of_file:
        i=i.split(",")                              #New list
        liste.append(i)

    for i in liste:

        for j in i:

             if j == "":
                 i.pop()

    for i in liste:                                 #Insert data in list
        if len(i) == 9:
            kg = i[8]

        elif len(i) == 8:
            i.append(kg)

    liste.pop()

    for i in liste:
                                           #convert string to integer and new list for graph
        data_id.append(int(i[0]))
        milisaniye.append(int(i[1]))
        signal1.append(int(i[2]))
        signal2.append(int(i[3]))
        signal3.append(int(i[4]))
        signal4.append(int(i[5]))
        signal5.append(int(i[6]))
        signal6.append(int(i[7]))
        data.append(float(i[8]))

    plt.title('Süt verilerinin grafiği')                   #Creating a graph
    plt.plot(data_id, data, 'g-')
    plt.plot(data_id, signal1, 'y-')
    plt.plot(data_id, signal2, 'k-')
    plt.plot(data_id, signal3, 'c-')
    plt.plot(data_id, signal4, 'b-')
    plt.plot(data_id, signal5, 'r-')
    plt.plot(data_id, signal6, 'm-')
    plt.xlabel('ID')
    plt.legend(['w=kilogram', 'w=signal1', 'w=signal2', 'w=signal3', 'w=signal5', 'w=signal6'])
    plt.show()
