few_shots = [
    {'Question' : "Aggregate the total sales for customer 103",
     'SQLQuery' : "SELECT SUM(`priceEach` * `quantityOrdered`) as totalSales FROM `orderdetails` od JOIN `orders` o ON o.`orderNumber` = od.`orderNumber` WHERE o.`customerNumber` = 103;",
     'SQLResult' : "[(Decimal('22314.36'),)]",
     'Answer' : "The total sales for customerNumber 103 is 22314.36."},
    
    {'Question' : "Retrieve all customers who have placed an order but have not made any payment",
     'SQLQuery' : "SELECT customers.customerName, orders.orderNumber FROM customers JOIN orders ON customers.customerNumber = orders.customerNumber LEFT JOIN payments ON customers.customerNumber = payments.customerNumber WHERE payments.customerNumber IS NULL;",
     'SQLResult' : """customerName	orderNumber,
Around the Horn	10104
B's Beverages	10105
Borgna Sausage	10106
Eastern Connection	10107
Ernst Handel	10108
Island Trading	10109
K&S Music	10110
Lacy's Department Store	10111
Laurence Hardware	10112
Morgenstern Garden	10113
Richard's Sporting Goods	10114
Seven Seas Imports	10115
Sport Fan	10116
Victoria's Secret	10117
W.W. Souvenirs	10118
Wine Merchant	10119""",
     'Answer' : """Here are the customer names and their corresponding order numbers who have not made any payments yet.

customerName	orderNumber
Around the Horn	10104
B's Beverages	10105
Borgna Sausage	10106
Eastern Connection	10107
Ernst Handel	10108
Island Trading	10109
K&S Music	10110
Lacy's Department Store	10111
Laurence Hardware	10112
Morgenstern Garden	10113
Richard's Sporting Goods	10114
Seven Seas Imports	10115
Sport Fan	10116
Victoria's Secret	10117
W.W. Souvenirs	10118
Wine Merchant	10119"""},
    
    {'Question': "what is the most ordered 1:10 scale model" ,
     'SQLQuery' : """SELECT `products`.`productCode`, `products`.`productName`, SUM(`quantityOrdered`) as totalQuantityOrdered
FROM `orderdetails`
JOIN `products` ON `orderdetails`.`productCode` = `products`.`productCode`
WHERE `products`.`productScale` = '1:10'
GROUP BY `products`.`productCode`, `products`.`productName`
ORDER BY totalQuantityOrdered DESC
LIMIT 1""",
     'SQLResult' : "[('S10_1678', '1969 Harley Davidson Ultimate Chopper', Decimal('1057'))]",
     'Answer' : "The product with the highest total quantity ordered with a product scale of 1:10 is the '1969 Harley Davidson Ultimate Chopper' (product code: S10\_1678) with a total quantity ordered of 1057."},
    
    {'Question' : "What are the most and least expensive products in the inventory",
     'SQLQuery' : """(SELECT `productName`, `MSRP` FROM `products` ORDER BY `MSRP` DESC LIMIT 1,1)
UNION ALL
(SELECT `productName`, `MSRP` FROM `products` ORDER BY `MSRP` ASC LIMIT 1,1);""",
     'SQLResult' : "[('2001 Ferrari Enzo', Decimal('207.80')), ('1958 Chevy Corvette Limited Edition', Decimal('35.36'))]",
     'Answer' : "The 2001 Ferrari Enzo is the most expensive product at $207.80 and the 1958 Chevy Corvette Limited Edition is the least expensive product at $35.36'"},
    
    {'Question' : "Products of which scale generate the most revenue",
     'SQLQuery' : """SELECT 
    products.productScale, 
    SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalRevenue
    FROM products
    JOIN orderdetails ON products.productCode = orderdetails.productCode
    JOIN orders ON orderdetails.orderNumber = orders.orderNumber
    GROUP BY products.productScale
    ORDER BY totalRevenue DESC
    LIMIT 1;
""",
     'SQLResult' : "[('1:18', Decimal('4071043.35'))]",
     'Answer' : "The product scale with the highest total revenue is '1:18' with a total revenue of $4071043.35."},
    
    {'Question' : "Retrieve the details of orders where the total order value is above the customer's credit limit",
     'SQLQuery' : """SELECT o.`orderNumber`, o.`orderDate`, o.`requiredDate`, o.status, c.`customerName`, c.`creditLimit`, SUM(od.`quantityOrdered` * od.`priceEach`) as totalOrderValue
FROM orders o
JOIN orderdetails od ON o.`orderNumber` = od.`orderNumber`
JOIN customers c ON o.`customerNumber` = c.`customerNumber`
GROUP BY o.`orderNumber`
HAVING totalOrderValue > c.`creditLimit`;""",
     'SQLResult' : "[(10401, datetime.date(2005, 4, 3), datetime.date(2005, 4, 14), 'On Hold', 'Tekni Collectables Inc.', Decimal('43000.00'), Decimal('43525.04')), (10414, datetime.date(2005, 5, 6), datetime.date(2005, 5, 13), 'On Hold', 'Gifts4AllAges.com', Decimal('41900.00'), Decimal('50806.85'))]",
     'Answer' : "There are 2 orders where the total order value exceeds the customer's credit limit:\n1. Order number 10401 from Tekni Collectables Inc. with a total order value of 43525.04, which is higher than their credit limit of 43000.00.\n2. Order number 10414 from Gifts4AllAges.com with a total order value of 50806.85, which is higher than their credit limit of 41900.00."},
    
    {'Question' : "which city has customer with the most orders",
     'SQLQuery' : """SELECT c.city, COUNT(o.orderNumber) as orderCount FROM orders o JOIN customers c ON o.customerNumber = c.customerNumber GROUP BY c.city ORDER BY orderCount DESC
LIMIT 1;""",
     'SQLResult' : "[('Madrid', 31)]",
     'Answer' : "The city with the most orders is Madrid with 31 orders."},
    
    {'Question' : "Who are all the employees reporting to employee number 1002",
     'SQLQuery' : """SELECT `lastName`, `firstName` 
FROM employees 
WHERE `reportsTo` = 1002;""",
     'SQLResult' : "[('Patterson', 'Mary'), ('Firrelli', 'Jeff')]",
     'Answer' : "Mary Patterson and Jeff Firrelli are the employees reporting to employee number 1002."},
    
    {'Question' : "retrieve all the payment info for customer 103",
     'SQLQuery' : """SELECT `customerNumber`, `checkNumber`, `paymentDate`, `amount` 
FROM payments 
WHERE `customerNumber` = 103;""",
     'SQLResult' : "[(103, 'HQ336336', datetime.date(2004, 10, 19), Decimal('6066.78')), (103, 'JM555205', datetime.date(2003, 6, 5), Decimal('14571.44')), (103, 'OM314933', datetime.date(2004, 12, 18), Decimal('1676.14'))]",
     'Answer' : "Customer 103 has made the following payments:\n- Check number HQ336336, amount 6066.78, on date 2004-10-19\n- Check number JM555205, amount 14571.44, on date 2003-06-05\n- Check number OM314933, amount 1676.14, on date 2004-12-18"},
    
    {'Question' : "What is the price of 1968 Ford Mustang",
     'SQLQuery' : "SELECT `priceEach` FROM `orderdetails` od JOIN `products` p ON od.`productCode` = p.`productCode` WHERE p.`productName` = '1968 Ford Mustang' LIMIT 5;",
     'SQLResult' : "[(Decimal('165.38'),), (Decimal('155.66'),), (Decimal('173.17'),), (Decimal('161.49'),), (Decimal('188.73'),)]",
     'Answer' : "The prices for the '1968 Ford Mustang' product are $165.38, $155.66, $173.17, $161.49, and $188.73."},
    
    {'Question' : "List the offices where the total number of employees is greater than 5",
     'SQLQuery' : """SELECT offices.city, offices.phone, COUNT(employees.employeeNumber) AS totalEmployees
FROM offices
JOIN employees ON offices.officeCode = employees.officeCode
GROUP BY offices.officeCode
HAVING totalEmployees > 5;""",
     'SQLResult' : "[('San Francisco', '+1 650 219 4782', 6)]",
     'Answer' : "The San Francisco Office is the only such office with a total of 6 employees"}
    
]