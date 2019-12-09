# EC601-Mini-Project3
Mini Project 3

User stories for store Data:

1. Markerting Director/Product manager want to store the perferrence of users to specific products

2. President candidate want to store the advice of users

3. The product manager of WeChat want to store the users feedback for analysing

4. A fan of Jay Chou want to store some interesting comments to popular songs of Jay Chou

5. A company want to store the disadvantages and advantages of apple pay or google pay

User stories for displaying Data:

1. Markerting Director/Product manager want to display the percentage of users perferrence to specific products by pie chart

2. President candidate want to display the advice with lists and chart

3. The product manager of WeChat want to display the users feedback with line chart

4. A fan of Jay Chou want to display some interesting comments to popular songs of Jay Chou by word list

5. A company want to display the percentage of the disadvantages and advantages of apple pay or google pay by histogram

Differences between MongoDB and MySQL:

1. Representation. In MongoDB, data represents in a collection of JSON documents while in MySQL, data is in tables and rows. JSON documents can compare to associative arrays when using PHP and directory objects when using Python.

2. Querying. You have to put a string in the query language that the DB system parses. The query language is called Structured Query Language, or SQL,from where MySQL gets its name. This exposes your DB susceptible to SQL injectionattacks. On the other hand, MongoDB’s querying is object-oriented, which means you pass MongoDB a document explaining what you are querying. There is no parsing whatsoever, which will take some time getting used to if you already use SQL.

3. Join operation is the best benefits of relational databases like MySQL. he operation allows for the querying across several tables. Although MongoDB doesn’t support joints, it supports multi-dimensional data types like other documents and arrays.

4. MySQL can embed documents. You would have to create one table for comments and another for posts if you are using MySQL to create a blog. In MongoDB, you will only have one array of comments and one collection of posts within a post.

5. MySQL supports atomic transactions. You can have several operations within a transaction and you can roll back as if you have a single operation. There is no support for transactions in MongoDB and the single operation is atomic.

6. One of the best things about MongoDB is that you are not responsible for defining the schema. All you need to do is drop in documents. Any 2 documents in a collection need not be in the same field. You have to define the tables and columns before storage in MySQL. All rows in a table share the same columns.

7. MongoDB’s performance is better than that of MySQL and other relational DBs. This is because MongoDB sacrifices JOINS and other things and has excellent performance analysis tools. Note that you still have to index the data and the data in most applications is not enough for them to see a difference. MySQL is criticized for poor performance, especially in ORM application. However, you are unlikely to have an issue if you do proper data indexing and you are using a database wrapper.

8. One advantage of MySQL over NoSQL like MongoDB is that the community in MySQL is much better than NoSQL. This is mostly because NoSQL is relatively new while MySQL has been around for several years.

9. There are no reporting tools with MongoDB, meaning performance testing and analysis is not always possible. With MySQL, you can get several reporting tools that help you rove the validity of your applications.

10. RDBSs function on a paradigm called ACID, which is an acronym for (Atomicity, Consistency, Isolation, and Durability). This is not present in MongoDB database.

11. MongoDB has a Map Reduce feature that allows for easier scalability. This means you can get the full functionality of MongoDB database even if you are using low-cost hardware.

12. You do not have to come up with a detailed DB model with MongoDB because of is non-relational. A DB architect can quickly create a DB without a fine-grained DB model, thereby saving on development time and cost.

MongoDB API: https://docs.mongodb.com/

MySQL API: https://dev.mysql.com/doc/refman/8.0/en/


Reference:

Comparing MongoDB with MySQL, Jenny Richards, June 24, 2015

Retrieved from: 
https://www.analyticbridge.datasciencecentral.com/profiles/blogs/comparing-mongodb-with-mysql

Accessed 8 Decemeber, 2019