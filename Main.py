from prims import *
from kurskul import *
from floy import * 
from dijistra import *
from boruvkas import *
from bellmanford import *
from cluster import *
import os
import datetime
def mainfun():
    x = datetime.datetime.now()
    print("\t\t\t\t\t\tWelcome to the world of Algorithms\t\t\tDate & Time:",x)
    print("1) Prims Algorithm")
    print("2) Kurskul Algorithm")
    print("3) Floyd Warshall Algorithm")
    print("4) Dijisktra Algorithm")
    print("5) boruvaks Algorithm")
    print("6) Bellman Ford Algorithm")
    print("7) Cluster Coefficent Algorithm")
    val1=input("\n\n\n\t\t\t Select Algorithm:")
    print("\n\n1)Input10.txt")
    print("2)Input20.txt")
    print("3)Input30.txt")
    val2=input("\n\n\n\t\t\t Select InputFiles:")
    if(val2=='1'):
        filename="input10"
    elif(val2=='2'):
        filename="input20"
    elif(val2=='3'):
        filename="input30"
    if(val1=='1'):
        primsalgo(filename)
    elif(val1=='2'):
        Kurskulalgo(filename)
    elif(val1=='3'):
        floydalgo(filename)
    elif(val1=='4'):
        dijikstraalgo(filename)
    elif(val1=='5'):
        boruvkasalgo(filename)
    elif(val1=='6'):
       bellmanfordalgo(filename)
    elif(val1=='7'):
        clusteralgo(filename)
    print("\n\n\t\tpress any key to continue")
    a = input('').split(" ")[0]
    os.system("cls")
    mainfun()
mainfun()




