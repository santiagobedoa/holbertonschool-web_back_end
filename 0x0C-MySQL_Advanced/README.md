# [MySQL advanced](https://intranet.hbtn.io/projects/632)

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://devhints.io/mysql" target="_blank" title="MySQL cheatsheet">
     MySQL cheatsheet
    </a>
   </li>
   <li>
    <a href="https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/" target="_blank" title="MySQL Performance: How To Leverage MySQL Database Indexing">
     MySQL Performance: How To Leverage MySQL Database Indexing
    </a>
   </li>
   <li>
    <a href="https://www.w3resource.com/mysql/mysql-procedure.php" target="_blank" title="Stored Procedure">
     Stored Procedure
    </a>
   </li>
   <li>
    <a href="https://www.w3resource.com/mysql/mysql-triggers.php" target="_blank" title="Triggers">
     Triggers
    </a>
   </li>
   <li>
    <a href="https://www.w3resource.com/mysql/mysql-views.php" target="_blank" title="Views">
     Views
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/functions.html" target="_blank" title="Functions and Operators">
     Functions and Operators
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html" target="_blank" title="Trigger Syntax and Examples">
     Trigger Syntax and Examples
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/create-table.html" target="_blank" title="CREATE TABLE Statement">
     CREATE TABLE Statement
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html" target="_blank" title="CREATE PROCEDURE and CREATE FUNCTION Statements">
     CREATE PROCEDURE and CREATE FUNCTION Statements
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/create-index.html" target="_blank" title="CREATE INDEX Statement">
     CREATE INDEX Statement
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/5.7/en/create-view.html" target="_blank" title="CREATE VIEW Statement">
     CREATE VIEW Statement
    </a>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   General
  </h3>
  <ul>
   <li>
    How to create tables with constraints
   </li>
   <li>
    How to optimize queries by adding indexes
   </li>
   <li>
    What is and how to implement stored procedures and functions in MySQL
   </li>
   <li>
    What is and how to implement views in MySQL
   </li>
   <li>
    What is and how to implement triggers in MySQL
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    All your files will be executed on Ubuntu 18.04 LTS using
    <code>
     MySQL 5.7
    </code>
    (version 5.7.30)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    All your SQL queries should have a comment just before (i.e. syntax above)
   </li>
   <li>
    All your files should start by a comment describing the task
   </li>
   <li>
    All SQL keywords should be in uppercase (
    <code>
     SELECT
    </code>
    ,
    <code>
     WHERE
    </code>
    …)
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    The length of your files will be tested using
    <code>
     wc
    </code>
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <h3>
   Comments for your SQL file:
  </h3>
  <pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
  <h3>
   Use “container-on-demand” to run MySQL
  </h3>
  <ul>
   <li>
    Ask for container
    <code>
     Ubuntu 18.04 - Python 3.7
    </code>
   </li>
   <li>
    Connect via SSH
   </li>
   <li>
    Or via the WebTerminal
   </li>
   <li>
    In the container, you should start MySQL before playing with it:
   </li>
  </ul>
  <pre><code>$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>
  <p>
   <strong>
    In the container, credentials are
    <code>
     root/root
    </code>
   </strong>
  </p>
  <h3>
   How to import a SQL dump
  </h3>
  <pre><code>$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/632)
</html>