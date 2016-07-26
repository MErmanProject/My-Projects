--Challenge 1: Retrieve Product Information
--Adventure Works sells many products that are variants of the same product model. You must write queries that retrieve information about these products

--1. Retrieve product model descriptions
--Retrieve the product ID, product name, product model name, and product model summary for each product from the SalesLT.Product table and the 
--SalesLT.vProductModelCatalogDescription view.

SELECT p.ProductID, p.Name, pm.Name AS ModelName, sv.Summary
FROM SalesLT.Product AS p
INNER JOIN SalesLT.vProductModelCatalogDescription AS sv
ON p.ProductModelID = sv.ProductModelID
INNER JOIN SalesLT.ProductModel as pm
ON p.ProductModelID = pm.ProductModelID;

--2. Create a table of distinct colors 
--Create a table variable and populate it with a list of distinct colors from the SalesLT.Product table. Then use the table variable to filter a query that 
--returns the product ID, name, and color from the SalesLT.Product table so that only products with a color listed in the table variable are returned.

DECLARE @varColors AS TABLE (Color varchar(15));
INSERT INTO @varColors
SELECT DISTINCT Color FROM SalesLT.Product
WHERE Color IS NOT NULL;

SELECT c.Color, p.ProductID, p.Name, p.Color
FROM @varColors AS c
JOIN SalesLT.Product AS p
ON p.Color=c.Color;

--3. Retrieve product parent categories
--The AdventureWorksLT database includes a table-valued function named dbo.ufnGetAllCategories, which returns a table of product categories 
--(for example ‘Road Bikes’) and parent categories (for example ‘Bikes’). Write a query that uses this function to return a list of all products 
--including their parent category and category.


SELECT p.Name, GAC.ProductCategoryName AS Category, GAC.ParentProductCategoryName AS ParentCategory
FROM salesLT.Product AS p
CROSS APPLY dbo.ufnGetAllCategories() AS GAC

--Challenge 2: Retrieve Customer Sales Revenue
--Each Adventure Works customer is a retail company with a named contact. You must create queries that return the total revenue for each customer, 
--including the company and customer contact names. 

--1. Retrieve sales revenue by customer and contact
--Retrieve a list of customers in the format Company (Contact Name) together with the total revenue for that customer. Use a derived table or a common table 
--expression to retrieve the details for each sales order, and then query the derived table or CTE to aggregate and group the data.

SELECT Customers, TotalRev
FROM
(SELECT soh.TotalDue as TotalRev, c.CompanyName + ' (' + c.FirstName + ' ' + c.LastName + ' )' AS Customers
 FROM SalesLT.SalesOrderHeader as soh
 JOIN SalesLT.Customer as c
 ON c.CustomerID = soh.CustomerID) AS Rev
GROUP BY Customers, TotalRev
ORDER BY Customers , TotalRev
