#HANDBALL STATICS
import os
import time
borrarPantalla = lambda: os.system ("cls")

#Definir
opc:int();
opc_L:int();
opc_P:int();
opc_A:int();
contraseña:str();
usuario:int();
intentos:int();
L9:int();
modL9:str();
L6:int();
modL6:str();
L9_L:int();
L6_L:int();
L9_V:int();
L6_V:int();
penales:int();
modPENALES:str();
perdidas_L:int();
modP_L:str();
perdidas_V:int();
modP_V:str();
atajadas_L:int();
modA_L:str();
atajadas_V:int();
modA_V:str();

#Iniciar
opc=0;
opc_L=0;
opc_P=0;
opc_A=0;
contraseña="";
usuario=0;
intentos=0;
L9=0;
modL9="";
L6=0;
modL6="";
L9_L=0;
L6_L=0;
L9_V=0;
L6_V=0;
penales=0;
modPENALES="";
perdidas_L=0;
modP_L="";
perdidas_V=0;
modP_L="";
atajadas_L=0;
modA_L="";
atajadas_V=0;
modA_V="";

#Programa
"""usuario=int(input("Bienvenido, ingrese su DNI para comenzar:"));
contraseña=str(input("Ingrese su contraseña:"));
print("");

while intentos <= 3:
    if contraseña != "grupo1":
        contraseña=str(input("La contraseña es incorrecta, vuelva a ingresarla:"));
        intentos=intentos+1;
    else:
        print("¡BIENVENIDO!");
        break;
    
borrarPantalla();"""
print("-----------------------------");
print("|        BIENVENIDO A       |");
print("|          HANDBALL         |");
print("|          STATICS          |");
print("-----------------------------");
time.sleep(2);

while opc != 4:
    print("------------------------------");
    print("|    Estadisticas actuales   |");
    print("| Lanzamientos de 9M:",L9,"    |");
    print("| Lanzamientos de 6M:",L6,"    |");
    print("| Penales:",penales,"               |");
    print("| Perdidas del Local:",perdidas_L,"    |");
    print("| Perdidas del Visitante:",perdidas_V,"|");
    print("| Atajadas del Local:",atajadas_L,"    |");
    print("| Atajadas del Visitante:",atajadas_V,"|");
    print("------------------------------");

    
    print("-"*36);
    print("|","*"*7,"MENU DE OPCIONES","*"*7,"|");
    print("*"*36);
    print("-"*36);
    print("===      1)LANZAMIENTOS          ===");
    print("===                              ===");
    print("===      2)PERDIDAS              ===");
    print("===                              ===");
    print("===      3)ATAJADAS              ===");
    print("===                              ===");
    print("===      4)SALIR                 ===");
    print("-"*36);
    opc=int(input("Elija una opción:"));
    borrarPantalla();
    
    if opc == 1:
        print("-"*36);
        print("*"*9,"LANZAMIENTOS","*"*9);
        print("*"*36);
        print("-"*36);
        print("===      1)GOLES DE 9 MTS        ===");
        print("===                              ===");
        print("===      2)GOLES DE 6 MTS        ===");
        print("===                              ===");
        print("===      3)PENALES               ===");
        print("===                              ===");
        print("===      4)SALIR                 ===");
        print("-"*36);
        
        while opc_L != 4:
            opc_L=int(input("Ingrese la opc de Lanzamiento:"));
            if opc_L == 1:
                modL9=str(input("Se suma(+) o resta(-) el L9:"));
                if modL9 == "+":
                    L9+=1;
                    break;
                elif modL9 == "-":
                    L9=L9-1;
                    break;
            elif opc_L == 2:
                modL6=str(input("Se suma(+) o resta(-) el L6:"));
                if modL6 == "+":
                    L6+=1;
                    break;
                elif modL6 == "-":
                    L6=L6-1;
                    break;
            elif opc_L == 3:
                modPENALES=str(input("Se suma(+) o resta(-) un penal:"));
                if modPENALES == "+":
                    penales+=1;
                    break;
                elif modL9 == "-":
                    penales=penales-1;
                    break;
            else:
                print("Ingrese una opción válida.");
        borrarPantalla();

    elif opc == 2:
        print("*"*36);
        print("*"*9,"PERDIDAS","*"*9);
        print("*"*36);
        print("-"*36);
        print("===      1)LOCAL                 ===");
        print("===                              ===");
        print("===      2)VISITANTE             ===");
        print("===                              ===");
        print("===      3)SALIR                 ===");
        print("-"*36);
        while opc_P != 3:
            opc_P=int(input("Ingrese la opc de Perdida:"));
            if opc_P == 1:
                modP_L=str(input("El local suma(+) o resta(-) una perdida:"));
                if modP_L == "+":
                    perdidas_L+=1;
                    break;
                elif modP_L == "-":
                    perdidas_L=perdidas_L-1;
                    break;
            elif opc_P == 2:
                modP_V=str(input("El visitante suma(+) o resta(-) una perdida:"));
                if modP_V == "+":
                    perdidas_V+=1;
                    break;
                elif modP_V == "-":
                    perdidas_V=perdidas_V-1;
                    break;
            else:
                print("Ingrese una opción válida.");
        borrarPantalla();
        os.system("cls"); 
            
    elif opc == 3:
        print("*"*36);
        print("*"*9,"ATAJADAS","*"*9);
        print("*"*36);
        print("-"*36);
        print("===      1)LOCAL                 ===");
        print("===                              ===");
        print("===      2)VISITANTE             ===");
        print("===                              ===");
        print("===      3)SALIR                 ===");
        print("-"*36);
        
        while opc_A != 3:
            opc_A=int(input("Ingrese la opc de Atajada:"));
            if opc_A == 1:
                modA_L=str(input("El equipo Local suma(+) o resta(-) una atajada:"));
                if modA_L == "+":
                    atajadas_L+=1;
                    break;
                elif modA_L == "-":
                    atajadas_L=atajadas_L-1;
                    break;
            elif opc_A == 2:
                modA_V=str(input("El equipo Visitante suma(+) o resta(-) una atajada:"));
                if modA_V == "+":
                    atajadas_V+=1;
                    break;
                elif modA_V == "-":
                    atajadas_V=atajadas_V-1;
                    break;
            else:
                print("Ingrese una opción válida.");
        borrarPantalla();
        os.system("cls");
    else:
        print("No escribió una opción válida.");

print("-----------------------------");
print("|      Gracias por usar     |");
print("|          HANDBALL         |");
print("|          STATICS          |");
print("-----------------------------");
print("------------------------------");
print("|   Las Estadisticas Finales |");
print("| Lanzamientos de 9M:",L9,"    |");
print("| Lanzamientos de 6M:",L6,"    |");
print("| Penales:",penales,"               |");
print("| Perdidas del Local:",perdidas_L,"    |");
print("| Perdidas del Visitante:",perdidas_V,"|");
print("------------------------------");
print("Gracias, hasta la próxima.");
time.sleep(5);



