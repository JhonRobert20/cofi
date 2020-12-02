# Cofi Code Challenge by Jhon Robert Matamoros Vitonera


```
"colores=[ tablas: negro, keys:blue, citas:rojo]
Expamples of products.json:

Code         | Name              |  Price       | 2x1_discount | bulk_discount|
----------------------------------------------------------------------------
VOUCHER      | Cofi Voucher      |   5.00€      |      YES      |      NO: []  |
TSHIRT       | Cofi T-Shirt      |  20.00€      |         NO     |       NO: []      |
MUG          | Cofi Coffee Mug   |    7.50€     |           NO   |          YES : [3,1]    |

Some explanations of json: <li>In challende.md you say "The marketing department believes in 2-for-1 promotions (buy two of the same product, get one free), and would like for there to be a 2-for-1 special on `VOUCHER` items" so i know that inclusions in next phases can be diffucult, in this code you can add directly the option of discount just telling in 2x1_discount ("YES" or "NO") <li>
<li> So you say to <other color>"The CFO insists that the best way to increase sales is with discounts on bulk purchases (buying x or more of a product, the price of that product is reduced), and demands that if you buy 3 or more `TSHIRT` items, the price per unit should be 19.00€.<other color>" another time to make the futures implementations more easy i added "bulk_discount" that funtions with a dicctionary, only add to "bulk_dictionari" {"("YES" or "NO"): ([] or [first_number, second_number])} where "first_number" is the products that a client have to buy to make a discount and "second_number" is the descount that the program make. The program recognise like a "no" if you put some other thing that "Yes"(doesn't matter cappitlaze, upper, or lower case)  <li>
<li>Finally but not less important we have a new implementation in the program, if you add some key with a wrong value the program directly make a new list of prodcuts, this obvius to make the program more strong, if someone scan a product that don't is in the json file the program just don't add this(does't matter if is a string or a name),
you can try to add some new products in "product.json", </li>

functions:
"def scan("product"): Check if is in the list. 
If is okey, return : "Product added"
If not, return : "Product not found in list, please write another one"
"def load_data is created to read a file, for default is "productos.json"
"check_json(productos, parametros): to be sure that the principals keys are right
"check2x1(): Check if we have 2x1 discount or no in the product (if you don't understant please check another time the table and considerations of json file)[the price to pay, the  price without discounts, discount maked]
"checkbulk(): Check if we have bulk discount or no (if you don't understant please check another time the table and considerations of json file)
[the price to pay, the price without discounts,discount maked]
"total(): Check all the prices that we have, select the less expensive, return [the total price to pay, the total price without discounts, total discount maked]
```