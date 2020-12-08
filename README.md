# ParcialHerramientasComputacionales
parcial de herramientas computacionales numero 3
## ¿QUE PROBLEMA ES?
El problema consiste en proponer un algortimo que identifique cual es el rol del individuo para asi otorgarle un descuento, dependiendo en que rol se encuentre el individuo ya sea **estudiante** o **profesor** tendra un descuento del _50%_ y el _20%_ respectivamente.
Se desea saber cuanto debe pagar en total por la compra realizada cuando es un profesor o un estudiante. por esta razon nos indican los datos a pedir del individuo con el fin de caracterizarlos y realizar su debido descuento, algunos de estos datos importandos por el cliente son:
* Cedula
* producto a comprar
* unidades a comprar
* rol 
* Cedula

## ¿ QUE MODELO COMPUTACIONAL LO RESUELVE?
El modelo computacional que resolvio este problema esta en parcial3.py
## ¿SU ALGORITMO QUE RECIBE COMO ENTRADA?
Recibe como entrada:
* Rol del cliente si es estudiante o profesor
* Cedula
* producto a comprar
* unidades a comprar
## ¿CUAL SERIA LAS SALIDAS DEL ALGORITMO?
Las salidas que arroja el algoritmo son:
* Rol del cliente
* Total a pagar con descuento incluido
* cedula
* codigo del producto seleccionado
##¿COMO SE CALCULA?
La manera de calcular el costo total a pagar es dependiento primeramente del rol del cliente ya que si es estudiante o prefesor su descuento es diferente
### profesor _20%_
* TOTAL A PAGAR = PRODUCTO X UNIDADES-(PRODCUTO X UNIDADES X _20%_)
### estudiante _50%_
* TOTAL A PAGAR = PRODUCTO X UNIDADES-(PRODCUTO X UNIDADES X _50%_)
> De esta manera se calcularia el total a pagar en cualquiera de las dos situaciones.
