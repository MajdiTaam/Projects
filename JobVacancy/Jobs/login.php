<?php require_once "include/header.php"; ?>
<?php
$error = '';
$username = '';
if(isset($_SESSION['log'])) {
    $error = $_SESSION['log']['error'];
    $username = $_SESSION['log']['username'];

    unset($_SESSION['log']);
}
?>

    <div class="row">
        <div class="col-md-4 offset-md-4">
            <?php
            if (!empty($error)) {
                echo "<div class='alert alert-danger' role='alert'>
        $error
    </div>";
            }
            ?>

            <form method="post" action="signin.php">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" name="username"
                           value="<?= $username; ?>">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" name="password">
                </div>
                <button type="submit" name="submit" >Login</button>
            </form>

            <a href="register.php"> Don't have an account? </a>
        </div>
    </div>

<?php require_once "include/footer.php"; ?>