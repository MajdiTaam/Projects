<?php
require_once "include/settings.php";
$log = array();
if(isset($_POST['submit'])) {
    $log['username'] = filter_var($_POST['username'], FILTER_SANITIZE_STRING);
    $log['company_name'] = filter_var($_POST['company_name'], FILTER_SANITIZE_EMAIL);
    $log['city'] = filter_var($_POST['city'], FILTER_SANITIZE_STRING);
    $password = filter_var($_POST['password'], FILTER_SANITIZE_STRING);
    $repeat = filter_var($_POST['repeat'], FILTER_SANITIZE_STRING);

    if(empty($log['username']) || empty($log['company_name']) ||
        empty($log['city']) || empty($password)) {
        $log['error'] = "All values must be completed";
    }
    else if($password != $repeat) {
        $log['error'] = "Password does not match";
    }
    else {
        $result = $conn->query("SELECT * FROM users WHERE username='{$log['username']}'");
        if($result->rowCount() > 0) {
            $log['error'] = "Username already in use";
        }
        else {
            // OK, register
            $encrypted = password_hash($password, PASSWORD_BCRYPT);
            $query = "INSERT INTO users(username, company, city, password)
                      VALUES('{$log['username']}', '{$log['company_name']}', 
                             '{$log['city']}', '$encrypted')";
            $conn->exec($query);
            header("Location: login.php");
            die();
        }
    }
    $_SESSION['log'] = $log;
    header("Location: register.php");
    die();
}
else {
    echo "Invalid access";
}