
<?php
require_once "include/settings.php";

if (isset($_SESSION['log'])) {
    $log = $_SESSION['log'];
    $username = $log['job_username'];
    $company_name = $log['company_name'];
    $city = $log['city'];
    $error = $log['error'];

    unset($_SESSION['log']);
}

?>


<?php require_once "include/header.php"; ?>

<div class="row">
    <div class="col-md-6 offset-md-3">
        <h1>Register</h1>

        <?php
        if (!empty($error)) {
            echo "<div class='alert alert-danger' role='alert'>
        $error
    </div>";
        }
        ?>

        <form method="post" action="signup.php">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username"
                       value="<?= $username; ?>">
            </div>
            <div class="form-group">
                <label for="company_name">Company Name</label>
                <input type="text" class="form-control" id="company_name" name="company_name"
                       value="<?= $company_name; ?>">
            </div>
            <div class="form-group">
                <label for="name">City</label>
                <input type="text" class="form-control" id="city" name="city"
                       value="<?= $city; ?>">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
            <div class="form-group">
                <label for="repeat">Repeat Password</label>
                <input type="password" class="form-control" id="repeat" name="repeat">
            </div>
            <button type="submit" name="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</div>

<?php require_once "include/footer.php"; ?>