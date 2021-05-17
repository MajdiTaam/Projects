<?php require_once "include/settings.php"; ?>
<?php
unset($_SESSION['sess_id']);
header("Location: index.php");
die();