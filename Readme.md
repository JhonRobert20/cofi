# Cofi Code Challenge, Jhon Robert

# Instalación

 - import json 
 - import os
 - from datetime import datetime

Estas han sido las únicas librerias utilizadas.
El programa se ha hecho con Python3.
 # Instrucciones para su uso
 Para poder utilizar el programa es necesario disponer de los siguientes archivos en una misma carpeta:
 - main.py
 - products.json
 - README.md

El siguiente paso es ejecutar el archivo main.py (funcionará en la terminal).
El programa sigue las indicaciones dadas inicialmente. Sin embargo, si deseas enterarte con más detalle de su funcionamiento, te recomiendo que leas los comentarios explicados en dicho programa, además de los siguientes apartados:


# Introducción
La compañía Cofi, necesita un programa que le permita realizar las compras de los clientes mediante una tienda física. 

Después de leer los requerimientos, el equipo técnico encargado de este proyecto,  ha hecho unas modificaciones, manteniendo la esencia.

En el siguiente punto se explican las modificaciones realizadas y el resultado final.

> El departamento de marketing cree en las promociones del 2 por 1 (compras 2 productos y consigues 1 gratuito), y además les gustaría que hubiese un 2 por 1 especial en los productos “VOUCHER”

> El CFO considera que la mejor manera para incrementar las ventas se consigue mediante descuentos en el monto de productos que se han comprado (comprando más de un producto, el producto de este, se ve reducido) y propone que en el caso de comprar 3 o más productos “TSHIRT”, el precio por unidad sea de 19.00€.

El programa demandado pedía 3 cosas: poder escanear un producto, poder mostrar el total de la compra y hacer descuentos específicos.
El nuevo programa, es capaz de eliminar productos, permitir añadir y modificar los diferentes tipos de descuentos (leer la sección "archivo").

Por favor, echad un vistazo a la nueva interfaz:

 - |Welcome to the Cofi shop|
 - Please select your option:
 - Add object(Add)
 - Remove objet(Remove)
 - Show total(Total)
 - Exit(Exit)

Mediante esta nueva interfaz, el usuario tiene un mayor control de la tienda además, de una mejor experiencia.
Las funciones añadidas para que el programa funcione son las siguientes:
 - Total (te muestra el total a pagar)
 - Check 2x1 (comprueba si existe descuento 2x1)
 - Check bulk (comprueba si existe descuento por cantidad)
 - Remove (elimina)
 - Scan (escanea)
 - Check json (comprueba la compatibilidad del archivo)
 - Load data (carga el archivo)
 - Write ticket (escribe en un archivo aparte las operaciones)



# Files

Como ya se ha mencionado, en este repositorio tenemos 3 archivos: main.py, README.md, products.json donde se encuentran localizados **products** **types** y **parameters**
Adicionalmente, se creará un archivo llamado "Json_Changes" el cual registra cualquier acción que haga el usuario.
Hay que tener en cuenta que para añadir un nuevo producto en el archivo **products.json**, se ha de cumplir con los parámetros y tipos especificados en el mismo archivo, los cuales no han de ser eliminados.
Con lo anteriormente citado, el programa es capaz de eliminar un producto inadecuado (si no tiene el mismo tipo de dato) y además, es capaz de corregir el producto en el caso de que las *keys* introducidas sean incorrectas.

Se define los siguientes parámetros:

> 

 - 2x1_discount: Elegir únicamente ("YES" o  "No"), si escribes "yes",
   cada 2 productos, 1 es gratuito.
 - bulk_discount: Se muestra el siguiente ejemplo:
 - {"YES":[3,1]}  "Se realiza el descuento por bulto (bulk discount) si
   compras 3 o más productos con el mismo código, el descuento es de     1 euro por cada uno.
 - "bulk_discount":  {"NO":[]} No se realiza descuento por bulto

Se muestra un ejemplo del antiguo y nuevo producto: 
 - Nuevo:
 - {
 - "code":  "VOUCHER",
 - "name":"Cofi Voucher",
 - "price":  5,
 - "2x1_discount":  "YES",
 - "bulk_discount":  {"NO":[]}
 - }

Antiguo:
 - {
 - "code":  "VOUCHER",
 - "name":"Cofi Voucher",
 - "price":  5,
 - }

Si el producto no pasa los chequeos correspondientes, se escribirá en el archivo **Json_Changes**, el cual se crea la primera vez que utilizas el programa.
