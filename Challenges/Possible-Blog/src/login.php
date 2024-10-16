<?php
session_start();
include 'db.php';

function getName($n) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ='; // Is the = necessary??
    $randomString = '';

    for ($i = 0; $i < $n; $i++) {
        $index = rand(0, strlen($characters) - 1);
        $randomString .= $characters[$index];
    }

    return $randomString;
}

if (!(isset($_POST['username']) || isset($_POST['password']))) {
    echo "no fuck you";
    header("Location:/?err=NoInput");
    die();
}

$username = htmlspecialchars($_POST['username'], );
$password = $_POST['password'];

$password = md5($password);

if (!(qValidate_Login($DBConnection, $username, $password))) {
    header("Location:/?err=loginfailed");
    die();
}

$cookie = "KAKA_";
$cookie .= getName(20);
$cookie .= base64_encode($username); // username in base64, should be username in finishied product
$cookie .= rand(1111, 9999);


setcookie("CerCookie", $cookie);

header("Location:/");

?>
