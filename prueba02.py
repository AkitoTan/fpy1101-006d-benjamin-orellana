import os
print ("*"*50)
print ("STOCk".center(50, "*"))
print ("*"*50)
menup = ["ver producto","añadir producto","ajustar producto","eliminar producto","salir"]
productos = {"escoba" : 5,"huevos" : 25, "leche" : 9}

while True:
    for ind in range(len(menup)):
        print(f"{ind+1}.{menup[ind]}")
    ans = input ("Que desea hacer?\n")
    if ans == "1":
        os.system("cls")
        for a, b in productos.items():
            print(f"{a.center(20, " ")}: {b}")
            print()
    elif ans == "2":
      os.system("cls")
      while True:
         prod = input("indique el producto que desea añadir:\n")
         if prod.replace (" ", '').isalpha():
            break
         if prod.lower() in productos:
            os.system("cls")
            print("error: el producto ya existe\n")
            continue
         else:
            os.system("cls")
            productos[prod.lower()] = 0
            print("producto agregado exitosamente\n")
    elif ans == "3":
       os.system("cls")
       while True:
          pass
    elif ans =="4":
       while True:
          os.system("cls")
          prod = input ("indique el producto a eliminar\n")
          if prod.replace(" ", '').isalpha():
             break
          if prod.lower() in productos ():
             os.system("cls")
             del productos[prod.lower()]
             print("Producto eliminado exitosamente\n")
             break

    elif ans =="5":
       os.system("cls")
       print("Hasta luego")
       break
      
