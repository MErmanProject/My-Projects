---Challenge 1: Retrieve Customer Data 
---1. Retrieve customer details
---Familiarize yourself with the Customer table by writing a Transact-SQL query that retrieves 
---all columns for all customers.

SELECT * 
FROM SalesLT.Customer;

---2. Retrieve customer name data
---Create a list of all customer contact names that includes the title, first name, middle name 
---(if any), last name, and suffix (if any) of all customers.

SELECT Title, FirstName,ISNULL(MiddleName,'') AS MiddleName, LastName, ISNULL(Suffix,'') AS Suffix 
FROM SalesLT.Customer;

---3. Retrieve customer names and phone numbers 
---Each customer has an assigned salesperson. You must write a query to create a call sheet that lists: 
---a) The salesperson 
---b) A column named CustomerName that displays how the customer contact should be greeted (for example, “Mr Smith”) 
---c) The customer’s phone number. 

SELECT Salesperson, Title + ' ' + LastName AS CustomerName, Phone
FROM SalesLT.Customer;

---Challenge 2: Retrieve Customer and Sales Data 
---1. Retrieve a list of customer companies 
---You have been asked to provide a list of all customer companies in the format <Customer ID> : <Company Name> - for example, 78: Preferred Bikes. 

SELECT Convert(varchar(3),CustomerID)+ ':' + CompanyName
FROM SalesLT.Customer;

---2. Retrieve a list of sales order revisions 
---The SalesLT.SalesOrderHeader table contains records of sales orders. You have been asked to retrieve data for a report that shows: 
---The sales order number and revision number in the format <Order Number> (<Revision>) – for example SO71774 (2). 
---The order date converted to ANSI standard format (yyyy.mm.dd – for example 2015.01.31). 

SELECT  Convert(varchar(10),SalesOrderID)+'('+ Convert(varchar(50),RevisionNumber)+')' AS 'Order(Revision)', Convert(varchar,OrderDate,102) AS OrderDate
FROM SalesLT.SalesOrderHeader;

---Challenge 3: Retrieve Customer Contact Details 
---1. Retrieve customer contact names with middle names if known 
---You have been asked to write a query that returns a list of customer names. The list must consist of a single field in 
---the format <first name> <last name> (for example Keith Harris) if the middle name is unknown, or <first name> <middle name> <last name> 
---(for example Jane M. Gates) if a middle name is stored in the database.

SELECT 
	CASE 
	   WHEN MiddleName IS NULL THEN FirstName + ' ' + LastName
	   ELSE FirstName + ' ' + MiddleName + ' ' + LastName
       END AS CustomerName
FROM SalesLT.Customer;

---2. Retrieve primary contact details 
---Customers may provide adventure Works with an email address, a phone number, or both. If an email address is available,
---then it should be used as the primary contact method; if not, then the phone number should be used. You must write a query that 
---returns a list of customer IDs in one column, and a second column named PrimaryContact that contains the email address if known, 
---and otherwise the phone number. 

SELECT CustomerID, COALESCE(EmailAddress, Phone) AS PrimaryContact
FROM SalesLT.Customer;

---3. Retrieve shipping status 
---You have been asked to create a query that returns a list of sales order IDs and order dates with a column named ShippingStatus that 
---contains the text “Shipped” for orders with a known ship date, and “Awaiting Shipment” for orders with no ship date. 

SELECT SalesOrderID,
	   CASE 
		WHEN ShipDate IS NOT NULL THEN 'Shipped'
		ELSE 'Awaiting Shipment'
	   END AS ShippingStatus
FROM SalesLT.SalesOrderHeader;
