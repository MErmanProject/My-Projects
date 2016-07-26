--Challenge 1: Retrieve Product Price Information
--Adventure Works products each have a standard cost price that indicates the cost of manufacturing the product, and a list price that indicates 
--the recommended selling price for the product. This data is stored in the SalesLT.Product table. Whenever a product is ordered, the actual unit 
--price at which it was sold is also recorded in the SalesLT.SalesOrderDetail table. You must use subqueries to compare the cost and list prices 
--for each product with the unit prices charged in each sale.

--1. Retrieve products whose list price is higher than the average unit price
--Retrieve the product ID, name, and list price for each product where the list price is higher than the average unit price for all products that 
--have been sold.

SELECT ProductID, Name
FROM SalesLT.Product 
WHERE ListPrice >
	(SELECT AVG(UnitPrice) AS UPrice
	FROM  SalesLT.SalesOrderDetail);


--2. Retrieve Products with a list price of $100 or more that have been sold for less than $100
--Retrieve the product ID, name, and list price for each product where the list price is $100 or more, and the product has been sold for less 
--than $100.

SELECT ProductID, Name, ListPrice
FROM SalesLT.Product
WHERE ListPrice > 100 
AND UnitPrice IN
	(SELECT UnitPrice 
	FROM SalesLT.SalesOrderDetail
	WHERE UnitPrice < 100);

--3. Retrieve the cost, list price, and average selling price for each product
--Retrieve the product ID, name, cost, and list price for each product along with the average unit price for which that product has been sold.
SELECT P.ProductID, P.Name, P.ListPrice, P.StandardCost,
(SELECT AVG(UnitPrice)
FROM SalesLT.SalesOrderDetail AS sod 
WHERE P.ProductID = sod.ProductID) AS AvgUnitPrice
FROM SalesLT.Product as P;

--4. Retrieve products that have an average selling price that is lower than the cost
--Filter your previous query to include only products where the cost price is higher than the average
--selling price.
SELECT ProductID, Name, ListPrice 
FROM SalesLT.Product 
WHERE ProductID IN 
(SELECT ProductID 
 FROM SalesLT.SalesOrderDetail 
 WHERE UnitPrice < 100.00) AND ListPrice >= 100.00 
ORDER BY ProductID;


--Challenge 2: Retrieve Customer Information
--The AdventureWorksLT database includes a table-valued user-defined function named
--dbo.ufnGetCustomerInformation. You must use this function to retrieve details of customers based on
--customer ID values retrieved from tables in the database.

--1. Retrieve customer information for all sales orders
--Retrieve the sales order ID, customer ID, first name, last name, and total due for all sales orders from
--the SalesLT.SalesOrderHeader table and the dbo.ufnGetCustomerInformation function.

SELECT s.SalesOrderID, GC.CustomerID, GC.FirstName, GC.LastName, s.TotalDue
FROM SalesLT.SalesOrderHeader AS s
CROSS APPLY dbo.ufnGetCustomerInformation(s.CustomerID) as GC
ORDER BY s.SalesOrderID;

--2. Retrieve customer address information
--Retrieve the customer ID, first name, last name, address line 1 and city for all customers from the
--SalesLT.Address and SalesLT.CustomerAddress tables, and the dbo.ufnGetCustomerInformation
--function.

SELECT ca.CustomerID, GC.FirstName, GC.LastName, a.AddressLine1, a.City
FROM SalesLT.CustomerAddress as ca
JOIN SalesLT.Address as a
ON ca.addressID=a.addressID
CROSS APPLY dbo.ufnGetCustomerInformation(ca.CustomerID) as GC
ORDER BY ca.CustomerID



