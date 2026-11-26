<?php
// Initialize the session.
session_start();

if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
    header("location: welcome.php");
    exit;
}

// Include config file.
require_once "config.php";

// Define variables and initialize with empty strings.
$username = $password = "";
$username_err = $password_err = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $username = $_POST["username"];
    $password = $_POST["password"];

    // *REVISED* Problem 2 (ii) 
    $sql = "SELECT * FROM users_table WHERE username = ? ";


    if ($stmt = mysqli_prepare($link, $sql)) {

        // This binds username to the ?
        mysqli_stmt_bind_param($stmt, "s", $username);

        // Gives statements
        mysqli_stmt_execute($stmt);

        // The results 
        $res = mysqli_stmt_get_result($stmt);

        // This checks if the username exists in the database 
        if (mysqli_num_rows($res) == 1) {
            $row = mysqli_fetch_assoc($res);
 
            //*REVISED* Problem 2 (iv) makes the password hashed. 
           	// What this do is the user's orginal password gets hashed before going into the database of username and password. 
            //PASSWORD_BCRYPT uses CRYPT_BLOWFISH algorithm to create the hash. 
            //https://www.geeksforgeeks.org/php/what-is-the-most-used-method-for-hashing-passwords-in-php/
            $hashed_password = password_hash($password, PASSWORD_BCRYPT);
            
            // *REVISED*  Problem 2 (iv)
			// this verifies the password with the hashed password
            //https://www.geeksforgeeks.org/php/how-to-encrypt-and-decrypt-passwords-using-php/
            $verify = password_verify($password, $hashed_password);
            
            if ($verify) {
                
                 //*REVISED* Problem 2 (i)
                 // This issues a new session ID login and deletes the old one. 
                 // The reason is because the session ID changes every time a user logs in the old cookie value does not work anymore.
                 // The cookie value can no longer be shared by all the users. 
                session_regenerate_id(true);

                $_SESSION["loggedin"] = true;
                $_SESSION["id"] = $row["id"];
                $_SESSION["username"] = $row["username"];
                $_SESSION["display_username"] = $row["username"];

                // Redirect user
                header("location: welcome.php");
                exit;

            } else {
                $password_err = "The username and/or password you entered was not valid.";
            }

        } else {
            $password_err = "The username and/or password you entered was not valid.";
        }

        mysqli_stmt_close($stmt);
    }

    mysqli_close($link);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; }
        .wrapper{ width: 350px; padding: 20px; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h1>Welcome to OnePhoto!</h1>
        <h2>Login</h2>
        <p>Please fill in your credentials to login.</p>
        <!-- htmlspecialchars is a built-in PHP function to convert special characters to HTML entities.
        $_SERVER is an array built into PHP containing information such as headers, paths, and script 
        locations. The entries in this array are created by the web server. With $_SERVER["PHP_SELF"] we
        are echoing the complete path, including all parameters, to our site. PHP_SELF is a variable that 
        returns the name and path of the current file (from the root folder). However, without htmlspcialchars 
        we would have an XSS vulnerability (see https://www.webadminblog.com/index.php/2010/02/23/a-xss-vulnerability-in-almost-every-php-form-ive-ever-written/).
        Various errors related to the user-entered strings (or omissions of those) are echoed to the
        output of the form for the user to see. -->
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
                <label>Username</label>
                <!-- *REVISED* Added the htmlspecialchars-->
                <input type="text" name="username" class="form-control" value="<?php echo htmlspecialchars($username); ?>">
                <span class="help-block"><?php echo htmlspecialchars($username_err); ?></span>
            </div>
            <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
                <label>Password</label>
                <input type="password" name="password" class="form-control">
                <span class="help-block"><?php echo htmlspecialchars($password_err); ?></span>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Login">
            </div>
            <p>Don't have an account? <a href="index.php">Sign up now</a>.</p>
        </form>
    </div>
</body>
</html>
