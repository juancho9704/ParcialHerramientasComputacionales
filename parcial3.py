ROL = input( "por favor dijite si es estudiante o profesor:")
CEDULA = int(input(" por favor dijite su cedula:"))

AREPA = 1500
CARP= 101
PANDEBONO = 800
CPBO=102
AVENA = 1200
CAVN=103
HUEVOS = 3000
CHV=104

print ("valor de AREPA es",AREPA,"con codigo",CARP)
print ("valor de PANDEBONO es",PANDEBONO,"con codigo",CPBO)
print ("valor de AVENA es",AVENA,"con codigo",CAVN)
print ("valor de HUEVOS es",HUEVOS,"con codigo",CHV)

if ROL =="estudiante"or ROL=="ESTUDIANTE":



    PRODUCTO = input ("por favor digite el producto deseado:")
    
    CANTIDAD= int(input ("dijite la cantidad de su pedido escojido:"))
    DESCUENTO = (50/100)
 

    if PRODUCTO == "AREPA" or PRODUCTO == "arepa":

        TOTAL= AREPA*CANTIDAD-(AREPA*CANTIDAD*DESCUENTO)

        print("el estudiante con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CARP)
               
                
    elif PRODUCTO == "PANDEBONO" or PRODUCTO == "pandebono":

        TOTAL= PANDEBONO*CANTIDAD-(PANDEBONO*CANTIDAD*DESCUENTO)

        print("el estudiante con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CPBO )



    elif PRODUCTO == "AVENA" or PRODUCTO == "avena":

        TOTAL= AVENA*CANTIDAD-(AVENA*CANTIDAD*DESCUENTO)

        print("el estudiante con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CAVN )


    elif PRODUCTO == "HUEVOS" or PRODUCTO == "huevos":

        TOTAL= HUEVOS*CANTIDAD-(HUEVOS*CANTIDAD*DESCUENTO)

        print("el estudiante con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CHV )



    else:

        print (" la opcion digitada no es correcta por favor digite las dos opciones posibles")







if ROL =="profesor"or ROL== "PROFESOR":


    PRODUCTO = input ("por favor digite el producto deseado:")
    
    CANTIDAD= int(input ("dijite la cantidad de su pedido escojido:"))
    DESCUENTO = (20/100)
 

    if PRODUCTO == "AREPA" or PRODUCTO == "arepa":

        TOTAL= AREPA*CANTIDAD-(AREPA*CANTIDAD*DESCUENTO)

        print("el profesor con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CARP)
               
                
    elif PRODUCTO == "PANDEBONO" or PRODUCTO == "pandebono":

        TOTAL= PANDEBONO*CANTIDAD-(PANDEBONO*CANTIDAD*DESCUENTO)

        print("el profesor con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CPBO )



    elif PRODUCTO == "AVENA" or PRODUCTO == "avena":

        TOTAL= AVENA*CANTIDAD-(AVENA*CANTIDAD*DESCUENTO)

        print("el profesor con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CAVN )


    elif PRODUCTO == "HUEVOS" or PRODUCTO == "huevos":

        TOTAL= HUEVOS*CANTIDAD-(HUEVOS*CANTIDAD*DESCUENTO)

        print("el profesor con cedula",CEDULA,"debe pagar" ,TOTAL,"por el prodcuto",CHV )



    else:

        print (" la opcion digitada no es correcta por favor digite las dos opciones posibles")









        

    
    

