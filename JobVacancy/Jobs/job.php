<?php
require_once "include/settings.php";

$job = filter_var($_POST['job'], FILTER_SANITIZE_STRING);
$description = filter_var($_POST['description'], FILTER_SANITIZE_STRING);
$category = filter_var($_POST['category'], FILTER_SANITIZE_STRING);

$conn->exec("INSERT INTO jobs (title, description, category, users_id)
                        VALUES ('$job', '$description', '$category', {$_SESSION['sess_id']})");


header("Location: profile.php");
die();