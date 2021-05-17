<?php
session_start();

$conn = new PDO("mysql:host=localhost;dbname=job_vacancies",
    "root", "root");