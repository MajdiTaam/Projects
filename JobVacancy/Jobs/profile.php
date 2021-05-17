<?php require_once "include/settings.php";

if(!isset($_SESSION['sess_id'])) {
    header("Location: login.php");
    die();
}

?>


<?php require_once "include/header.php";?>

<h2 style="text-align: center"> <?=$_SESSION['username'];?> </h2>

<a href="update_profile.php">Update profile</a>

<?php
$result = $conn->query("SELECT * FROM users WHERE id={$_SESSION['sess_id']}");
$row = $result->fetch(PDO::FETCH_ASSOC);

echo "<div>
         Mobile: {$row['phone']}
     </div>"

?>

<?php

echo "<div>
         <img src ='images/{$_SESSION['sess_id']}/{$row['logo']}' alt='' width = '200px'/>  <br>
     </div>"

?>

    <h2>Jobs</h2>

<?php

$statmnt = $conn->query("SELECT * FROM jobs WHERE users_id={$_SESSION['sess_id']}");

while($row = $statmnt->fetch(PDO::FETCH_ASSOC)) {
    echo "<div>
            <p>{$row['title']}</p>
            <form method='post' action='delete_job.php'>
                <input type='text' name='id' value='{$row['id']}' hidden>
                <input type='submit' value='Delete'>
            </form>
          </div>";
}

?>

<?php require_once "include/footer.php"; ?>
