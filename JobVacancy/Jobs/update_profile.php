<?php require_once "include/settings.php"; ?>
<?php require_once "include/header.php"; ?>
<?php
if(!isset($_SESSION['sess_id'])) {
    header("Location: login.php");
    die();
}
?>

<h1>Update your profile!</h1>


<div class ="container">
    <div>
        <form method="post" action="logo.php" enctype="multipart/form-data">
            <input type="file" name="logo">
            <input type="submit" value="Add Logo">
        </form>

        <form method ="post" action="phone.php">
            <textarea name="phone"> </textarea>
            <input type="submit" value="Add Phone">
        </form>
        <h2>Add a new job: </h2>
        <form method="post" action="job.php">
            <p> Name: </p>
            <textarea name="job"></textarea> <br><br>
            <p> Description:</p>
            <textarea name="description"></textarea> <br> <br>
            <p> Category:</p>
            <textarea name="category"></textarea>
            <input type="submit" value="Add">
        </form>
    </div>

</div>

<?php require_once "include/footer.php"; ?>