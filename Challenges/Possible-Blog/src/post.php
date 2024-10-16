<?php

session_start();

include 'db.php';

if (!(isset($_POST['textpost']) || isset($_SESSION['LoggedInUser']))) {
    echo "no fuck you";
    header("Location:/?err=NoInput");
    die();
}

$user = $_SESSION['LoggedInUser'];
$post = $_POST['textpost'];

if (!(isset($_POST['private']))) {
    $private = 0;
}
else {
    $private = 1;
}


qAdd_Post($DBConnection, $user, $post, $private);
header("Location:/");
die();
?>
