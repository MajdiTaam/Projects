<?php require_once "include/settings.php";
$query = "SELECT * FROM jobs";
$result = $conn->query($query, PDO::FETCH_ASSOC);
?>


<?php require_once "include/header.php"; ?>





<br>

<h2>Vaccant Jobs:</h2>
<div>

        <?php
        foreach($result as $row) {
            echo "<div>
              <p style='color:blue'>{$row['company']}</p>
              <p> {$row['title']} </p>
          
             
          </div>";
        }
        ?>

</div>
<?php require_once "include/footer.php"; ?>