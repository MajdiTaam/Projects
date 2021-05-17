<?php
require_once "include/settings.php";

$log = array();

if(isset($_POST['submit'])) {
    $log['username'] = filter_var($_POST['username'], FILTER_SANITIZE_STRING);
    $password = filter_var($_POST['password'], FILTER_SANITIZE_STRING);

    if(empty($log['username']) || empty($password)) {
        $log['error'] = "All values must be completed";
    }
    else {
        $result = $conn->query("SELECT * FROM users WHERE username='{$log['username']}'");
        if($result->rowCount() == 0) {
            $log['error'] = "Username is wrong";
        }
        else {
            $row = $result->fetch(PDO::FETCH_ASSOC);
            if(password_verify( $password, $row['password'])) {
                // OK. Proceed
                $_SESSION['sess_id'] = $row['id'];
                $_SESSION['username'] = $log['username'];
                header("Location: profile.php");
                die();
            }
            else {
                // echo  '$password, $encry
                $log['error'] = "Password is wrong";
            }
        }
    }
    $_SESSION['log'] = $log;
    header("Location: login.php");
    die();
}
else {
    echo "Invalid access";
}