--Challenge 1: Generate Invoice Reports
--Adventure Works Cycles sells directly to retailers, who must be invoiced for their orders. You have been tasked with writing a query to 
--generate a list of invoices to be sent to customers. Tip: Review the documentation for the FROM clause in the Transact-SQL Reference.
--1. Retrieve customer orders
--As an initial step towards generating the invoice report, write a query that returns the company name from the SalesLT.Customer table, 
--and the sales order ID and total due from the SalesLT.SalesOrderHeader table.
SELECT c.CompanyName, s.SalesOrderId, t.TotalDue
FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS s
ON c.CustomerID = s.CustomerID
 JOIN SalesLT.SalesOrderHeader AS t
ON c.CustomerID=t.CustomerID
ORDER BY t.TotalDue DESC

--2. Retrieve customer orders with addresses
--Extend your customer orders query to include the Main Office address for each customer, including the full street address, city, state or province,
-- postal code, and country or region
SELECT c.CompanyName, s.SalesOrderId, t.TotalDue, x.AddressLine1, x.AddressLine2, x.city, x.stateprovince, x.PostalCode, x.CountryRegion
FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS s
ON c.CustomerID = s.CustomerID
 JOIN SalesLT.SalesOrderHeader AS t
ON c.CustomerID=t.CustomerID
JOIN SalesLT.CustomerAddress 
ON c.CustomerID=SalesLT.CustomerAddress.CustomerID
JOIN SalesLT.Address as x
ON x.AddressID = SalesLT.CustomerAddress.AddressID
WHERE SalesLT.CustomerAddress.AddressType='Main Office'
ORDER BY t.TotalDue DESC;

--Challenge 2: Retrieve Sales Data
--As you continue to work with the Adventure Works customer and sales data, you must create queries for reports that have been 
--requested by the sales team.

--1. Retrieve a list of all customers and their orders
--The sales manager wants a list of all customer companies and their contacts (first name and last name),
--showing the sales order ID and total due for each order they have placed. Customers who have not
--placed any orders should be included at the bottom of the list with NULL values for the order ID and
--total due.
SELECT c.CompanyName, c.FirstName, c.LastName, s.SalesOrderID, s.TotalDue
FROM salesLT.Customer as c
LEFT JOIN SalesLT.SalesOrderHeader as s
ON c.CustomerID=s.CustomerID
ORDER BY s.TotalDue DESC

--2. Retrieve a list of customers with no address
--A sales employee has noticed that Adventure Works does not have address information for all
--customers. You must write a query that returns a list of customer IDs, company names, contact names
--(first name and last name), and phone numbers for customers with no address stored in the database.
SELECT c.CustomerID, c.CompanyName, c.FirstName + ' ' + c.LastName AS ContactName, c.Phone
FROM salesLT.Customer as c
LEFT JOIN SalesLT.CustomerAddress as ca
ON c.CustomerID=ca.CustomerID
WHERE ca.AddressID IS NULL;


--3. Retrieve a list of customers and products without orders
--Some customers have never placed orders, and some products have never been ordered. Create a query
--that returns a column of customer IDs for customers who have never placed an order, and a column of
--product IDs for products that have never been ordered. Each row with a customer ID should have a
--NULL product ID (because the customer has never ordered a product) and each row with a product ID
--should have a NULL customer ID (because the product has never been ordered by a customer).

SELECT c.CustomerID, p.ProductID
FROM SalesLT.Customer AS c
FULL JOIN SalesLT.SalesOrderHeader AS oh
ON c.CustomerID = oh.CustomerID
FULL JOIN SalesLT.SalesOrderDetail AS od
ON od.SalesOrderID = oh.SalesOrderID
FULL JOIN SalesLT.Product AS p
ON p.ProductID = od.ProductID
WHERE oh.SalesOrderID IS NULL
ORDER BY ProductID, CustomerID;