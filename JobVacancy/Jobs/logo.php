<?php
require_once "include/settings.php";


$upload_dir = "images/" . $_SESSION['sess_id'] . "/";
if (!file_exists($upload_dir)) {
    mkdir($upload_dir);
}
$upload_file = $upload_dir . basename($_FILES["logo"]["name"]);
$ok = true;
$max_size = 500000; // 500kb
$extension = strtolower(pathinfo($upload_file,PATHINFO_EXTENSION));
$message = "";

// Is it an image file?
if(isset($_POST["submit"])) {
    $imageData = getimagesize($_FILES["logo"]["tmp_name"]);
    if($imageData !== false) {
        $message = "File ". basename( $_FILES["logo"]["name"]) .
            ", type: " . $imageData["mime"];
        $ok = true;
    } else {
        $message .= "ERROR: File is not an image<br>";
        $ok = false;
    }
}


if ($_FILES["logo"]["size"] > $max_size) {
    $message .= "Error: file is too large ({$_FILES["logo"]["size"]}) 500kb limit<br>";
    $ok = false;
}

if($extension != "jpg" && $extension != "png" && $extension != "jpeg"
    && $extension != "gif" ) {
    $message .= "ERROR: only JPG, JPEG, PNG & GIF images supported<br>";
    $ok = false;
}

if (!$ok) {
    echo $message;

} else {

    if (move_uploaded_file($_FILES["logo"]["tmp_name"], $upload_file)) {
        $conn->exec("UPDATE users SET logo = 
                        '{$_FILES["logo"]["name"]}' WHERE id={$_SESSION['sess_id']}");


    }
    else {
        echo $_FILES["logo"]["error"];
        die();
    }

    header("Location: profile.php");
    die();
}
?>