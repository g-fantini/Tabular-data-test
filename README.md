# Tabular data test 
We would like you to build an application consisting of the following three items:

● A form with four input fields (name, date of birth, email address and number of children) and a button 

● A table

● A text input 
 
We would like to see your approach to bundling these visual html elements in a way that makes it easy to re-use the code (ideally with appropriate tests) and how you manage the communication between them. The form will be used to add data to the table. The table will display the data added through the form and the data should be persisted in an SQLite database. The text input will be used to filter the data in the name and email columns – there should be one text field to filter on both columns.
The table should have a header row and clicking the header on a specific column should result in the data being sorted in that column. 
Default sorting order should be ascending. Clicking the same column a second time should result in the column being sorted in descending order. 
The data should be paginated when there are more than 15 rows. The sorted column and sorting order should be displayed on the page inside a paragraph.
The user should be prevented from entering invalid data. Please ensure that your code is written in such a way that it can be easily maintained in future.
Please also note what additional work you would plan to do if you needed to re-use the sortable table code in another project (e.g. would this affect your code structure?)
