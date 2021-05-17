<?php
require_once "include/settings.php";

$id = filter_var($_POST['id'], FILTER_SANITIZE_STRING);

$result = $conn->query("SELECT * FROM jobs where id=$id");
$row = $result->fetch(PDO::FETCH_ASSOC);


$conn->exec("DELETE FROM jobs WHERE id=$id AND users_id={$_SESSION['sess_id']}");


header("Location: profile.php");
die();