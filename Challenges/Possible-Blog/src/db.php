<?php
// CREATE USER 'rooti'@'localhost' IDENTIFIED BY 'thisisbullshit';
// CREATE DATABASE DBblog CHARACTER SET utf8mb4 COLLATE utf8mb4_swedish_ci;
// CREATE TABLE users (ID int NOT NULL AUTO_INCREMENT, username varchar(64) NOT NULL, password varchar(64) NOT NULL, employeeID int, PRIMARY KEY (ID));
// CREATE TABLE posts (ID int NOT NULL AUTO_INCREMENT, author varchar(64) NOT NULL, content text, date int, status int, PRIMARY KEY (ID));
// GRANT ALL PRIVILEGES ON DBblog.* TO 'rooti'@'localhost' WITH GRANT OPTION;
// FLUSH PRIVILEGES;
// INSERT INTO users (username, password, employeeID) VALUES ('admin', 'a9bab1b35d2bba445f3653bb2d2eb910', 320356);

// admin : ?_N=RD5#}MBw]YW
// nicke : dwasdheswwlo123ndalouhdwa1
// vnorrspratt : kiuydwg1i2763D!#!
session_start();

$DBUser = 'rooti';
$DBPassword = 'thisisbullshit';
$DBDatabase = 'DBblog';

$DBConnection = new mysqli("127.0.0.1", $DBUser, $DBPassword, $DBDatabase);

if ($DBConnectione->connect_error) {
    die("Conn Failed!!!");
}


// Madeup hungarian notation
// q - Query

// Returns all posts from the database in an orderly fashion
function qSelect_All_Posts($DBConnection) {
    $statement = "SELECT * FROM posts WHERE status = 0 ORDER BY ID DESC";
    $sql = $DBConnection->prepare($statement);
    $sql->execute();
    $result = $sql->get_result();

    return $result;
}
function qSelect_Own_posts($DBConnection, $username) {
    $username = $DBConnection->real_escape_string($username);
    $statement = "SELECT * FROM posts WHERE author = ? ORDER BY ID DESC";

    $sql = $DBConnection->prepare($statement);
    $sql->bind_param("s", $username);
    $sql->execute();
    $result = $sql->get_result();
    
    return $result;

}

// Add post to database
function qAdd_Post($DBConnection, $author, $text, $status) {
    $author = htmlspecialchars($author, ENT_QUOTES);
    $text = htmlspecialchars($text, ENT_QUOTES);
    $status = htmlspecialchars($status, ENT_QUOTES);
    $statement = "INSERT INTO posts (author, content, status) VALUES (?, ?, ?)";

    $sql = $DBConnection->prepare($statement);
    $sql->bind_param("ssi", $author, $text, $status);

    $sql->execute();
    return True;

}

// Returns true if only one entry of a user is found, false if no or multiple users are found.
// Used to validate logins
function qValidate_Login($DBConnection, $username, $password) {
    $sql = $DBConnection->prepare("SELECT * FROM users WHERE username = ? AND password = ?");

    $sql->bind_param("ss", $username, $password);

    $sql->execute();
    $result = $sql->get_result();
    $rowcount = mysqli_num_rows($result);

    
    

    if ($rowcount === 1) {
        return True;
    }
    else {
        return False;
    }
}
// Varför failar min prepare??????????
function qVerify_EmpNumAvailability($DBConnection, $employeenumber) {
    $sql = $DBConnection->prepare("SELECT * FROM users WHERE employeeID = ?");
    $employeenumber = (int)$employeenumber;
    $sql->bind_param('i', $employeenumber);
    $sql->execute();

    $result = $sql->get_result();
    $rowcount = mysqli_num_rows($result);

    $result->free();
    
    if ($rowcount != 0) {
        return False;
    }
    return True;
}

function qVerify_UsernameAvailability($DBConnection, $username) {
    $statement = "SELECT * FROM users WHERE username = ?";
    $sql = $DBConnection->prepare($statement);
    $sql->bind_param("s", $username);
    $sql->execute();
    $result = $sql->get_result();
    $rowcount = mysqli_num_rows($result);

    $result->free();

    if ($rowcount != 0) {
        return False;
    }
    return True;
}

function qCreate_User($DBConnection, $username, $password, $employeenumber) {
    $sql = $DBConnection->prepare("INSERT INTO users (username, password, employeeID) VALUES (?,?,?)");
    $sql->bind_param("ssi", $username, $password, $employeenumber);
    $result = $sql->execute();
    //$result->free();
    return True;
}


?>
