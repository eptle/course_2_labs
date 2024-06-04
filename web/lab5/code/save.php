<?php
include 'composer/vendor/autoload.php';
function redirectToHomePage(){
    header('Location: /index.php');
    exit();
}

if (false === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])){
    redirectToHomePage();
    exit();
}
$email = $_POST['email'];
$category = $_POST['category'];
$title = $_POST['title'];
$description = $_POST['description'];

$toSpreadsheet = [[$category, $email, $title, $description]];

$googleAccountKeyFilePath = "key.json";

putenv('GOOGLE_APPLICATION_CREDENTIALS=' . $googleAccountKeyFilePath);

$client = new Google_Client();

$client->useApplicationDefaultCredentials();
$client->addScope('https://www.googleapis.com/auth/spreadsheets');
$service = new Google_Service_Sheets($client);
$spreadsheetId = "1dkUQaSFdAO7aTBs-xz4-eef9mVIjPq32YRBSZhX2Lm8";
$spreadsheetName = "web4";

$body = new Google_Service_Sheets_ValueRange(['values' => $toSpreadsheet]);

$options = array('valueInputOption' => 'USER_ENTERED');

$service->spreadsheets_values->append($spreadsheetId, $spreadsheetName, $body, $options);
redirectToHomePage();