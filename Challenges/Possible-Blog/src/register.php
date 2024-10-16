<?php 
session_start();
include 'db.php';

if (!(isset($_POST['username']) || isset($_POST['password']) || isset($_POST['empnumber']))) {
    echo "no fuck you";
    header("Location:/?err=missingvalue");
    die();
}

$username = $_POST['username'];
$password = $_POST['password'];
$empnumber = $_POST['empnumber'];

/*

empnumber RULES:
MUST BE 6 Characters
Must be divisable by 2
When squared, must be at least 12 numbers long
When rooted, must be perfect square
Must have the number 5 in it

*/
if (ctype_digit($empnumber) == FALSE) {
    header("Location:/?err=notint");
    die();
}
if ($empnumber < 100000) {
    header("Location:/?err=smolemp");
    die();
}
if ($empnumber > 999999) {
    header("Location:/?err=bigemp");
    die();
}
if ($empnumber % 2 != 0) {
    header("Location:/?err=noteven");
    die();
}
if ($empnumber ** 2 <= 99999999999) {
    header("Location:/?err=sqrdblw11");
    die();
}
$empsqrt = sqrt($empnumber);
if ($empsqrt != floor($empsqrt)) {
    header("Location:/?err=notperfectsquare");
    die();
}
$five = 5;
$strempnumber = (string)$empnumber;
$strfive = (string)$five;

if (!(strpos($strempnumber, $strfive))) {
    header("Location:/?err=missingfive");
    die();
}

if (!(qVerify_EmpNumAvailability($DBConnection, $empnumber))) {
    header("Location:/?err=employeenumberalreadyinuse");
    die();
}

if (!(qVerify_UsernameAvailability($DBConnection, $username))) {
    header("Location:/?err=usernameunavailable");
    die();
}

$hashedpassword = md5($password);
$safeusername = htmlspecialchars($username, ENT_QUOTES);

qCreate_User($DBConnection, $safeusername, $hashedpassword, $empnumber);
header("Location:/");
die();

?>
