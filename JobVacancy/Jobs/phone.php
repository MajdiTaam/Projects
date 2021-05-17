<?php
require_once "include/settings.php";

$id = filter_var($_POST['id'], FILTER_SANITIZE_STRING);
$phone = filter_var($_POST['phone'], FILTER_SANITIZE_STRING);


$conn->exec("UPDATE users SET phone='$phone' WHERE id = {$_SESSION['sess_id']}");

header("Location: profile.php");
die();


