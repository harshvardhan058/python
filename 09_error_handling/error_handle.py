file = open('youtube2.txt','w')

try:
    file.write("Abe Bhidu Apne Kam se Kam rakhna")
finally:
    file.close()


with open('youtube3.txt',"w") as file2:
    file2.write("Tere ko Kitni baar bolne ka apne kam se kam rakh")