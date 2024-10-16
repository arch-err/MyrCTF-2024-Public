<!DOCTYPE html>
<?php 
session_start();

include 'db.php';

if (isset($_COOKIE['CerCookie'])) {
    $cercookie = $_COOKIE['CerCookie'];
    $minusrandom = substr_replace($cercookie, "", 0, 25);
    $currentuser = substr_replace($minusrandom, "", -4, 4);
    $currentuser = base64_decode($currentuser);

    $_SESSION['LoggedIn'] = True;
    $_SESSION['LoggedInUser'] = $currentuser;
}
else {
    $_SESSION['LoggedIn'] = False;
}


?>
<html>
<head>
    <title>Forumu Cerebri</title>
    <link rel="stylesheet" type="text/css" href="./main.css" />
</head>
<body>
    <?php 
    $errormessage = "";
    if (isset($_GET['err'])) {
    switch ($_GET['err']) {
        case "notint":
            $errormessage = "Anställningsnumret är inte ett tal";
            break;
        case "smolemp":
            $errormessage = "Anställningsnumret är för litet";
            break;
        case "bigemp":
            $errormessage = "Anställningsnumret är för stort";
            break;
        case "noteven":
            $errormessage = "Anställningsnumret är inte ett jämt tal";
            break;
        case "sqrdblw11":
            $errormessage = "Anställningsnumret upphöjt till två är inte över elva siffror långt";
            break;
        case "notperfectsquare":
            $errormessage = "Anställningsnumret är inte en perfekt kvadrat";
            break;
        case "missingfive":
            $errormessage = "Anställningsnumret saknar siffran 5";
            break;
        case "employeenumberalreadyinuse":
            $errormessage = "Anställningsnumret är redan i användning";
            break;
        case "usernameunavailable":
            $errormessage = "Användarnamnet är upptaget";
            break;
        default:
            $errormessage = "ERROR IN ERROR";
            break;
        
    }
    echo "<script>alert('" . $errormessage . "')</script>";
    }
    ?>
    <!-- Are you sure that you are looking at the right thing?-->
    <!--
    <div class="header">
        <div class="alternatives">
            <p>Blog</p>
        </div>
        <div class="alternatives">
            <p>My Posts</p>
        </div>
        <div class="alternatives">
            <p>Log In</p>
        </div>
        <div class="alternatives">
            <p>Sign Up</p>
        </div>
    </div>
    -->
        <!-- Maybe you are? -->
        <!--<div class="login">
    
        </div>-->
        
    <div class="clearfix"></div>
    <!-- Jesus christ it's been too long since I did front-end... -->
    <div class="content">
        <div class="main-content">
            <div class="content-box">
                <h1>Roboti Cerebris Interna Blogg</h1>
                <hr />
		<?php if ($_SESSION['LoggedIn'] == True) {echo "<h2>MyrCTF{J4g_H4d3_b3tT_0m_uRs4kt_m3n_NEJ}</h2>";} ?>
                <br />
                <i>Satt på teammöte för några månader sedan och tänkte att vi behövde en sånhär! Lite av ett såkallat "Work in Progress" som man säger på amerikanska, men tänker att den är bra nog att släppa för vår njutning nu. Ja, den är ful. Ja, den är lite fulhackad. Men fick inte mer tid att arbeta på den nu så nära launch, så får väl fixa saker sen. <br /> <br /> // Brainiac</i>
                <br /><br />
                <hr style="width:75%;margin:auto;"/>
                <br />
                <!-- Start Text-Loop -->
                <?php 
                if (isset($_GET['own'])) {
                    if ($_GET['own'] == 'true') {
                        $result = qSelect_Own_posts($DBConnection, $currentuser);
                        while ($row = $result->fetch_assoc()) {
                            echo '<div class="post-box">
                            <h3>' . $row['author'] . '</h3>
                            <p>' . $row['content'] . '</p>
                            </div>';
                        }
                    }
                }
                    else {
                    
                    $result = qSelect_All_Posts($DBConnection);
                    while ($row = $result->fetch_assoc()) {
                        echo '<div class="post-box">
                        <h3>' . $row['author'] . '</h3>
                        <p>' . $row['content'] . '</p>
                        </div>';
                    }
                }

                ?>
            </div>
            
        </div>
        <div class="sorry">
            <p>Front-end på kort tid kräver enkla lösningar, detta är en av dem.</p>
        </div>
        <!-- Could this be used for profile stuff instead? Like a login?  // View your profile?-->
        <!-- Replace this with profile stuff once logged in -->
        <div class="not-main-content">
            <div class="content-box">
                <?php if ($_SESSION['LoggedIn'] == True) {echo '<h2>Hi ' . htmlspecialchars($currentuser) . '!</h2><hr /><br /><a href="index.php?own=true">Visa mina inlägg</a><br /><br /><hr style="width:66%;text-align:center;margin:auto;" /><br /><form method="POST" action="post.php"><textarea name="textpost" rows="10" cols="50" placeholder="Skriv ditt inlägg här!" required></textarea><br /><br /><input type="checkbox" value="1" name="private"><label for="private"> Privat inlägg</label><br /><br /><input type="submit" value="Posta!"></form>';}
                
                else {
                    echo '<h2>Logga in / Registrera dig!</h2>
                <hr />
                <br />
                <form method="POST" action="login.php">
                    <input type="text" name="username" placeholder="Användarnamn" required />
                    <br />
                    <br />
                    <input type="password" name="password" placeholder="Lösenord" required />
                    <br />
                    <br />
                    <input type="submit" value="Logga in!">
                    
                </form>
                <br />
                <p id="No-Account-Text" onclick="document.getElementById(\'SignUpBox\').style.display = \'inline\'">Inget konto ännu?</p>
                <div id="SignUpBox">
                    <form method="POST" action="register.php">
                        <br />
                        <input type="text" name="username" placeholder="Användarnamn" required />
                        <br />
                        <br />
                        <input type="password" name="password" placeholder="Lösenord" required />
                        <br />
                        <br />
                        <input type="text" name="empnumber" placeholder="Anställningsnummer" required />
                        <br />
                        <br />
                        <input type="submit" value="Registrera dig!" />
                    </form>
                </div>';
                }
                
                ?>

            </div>
        </div>
    </div>
    <!-- hOw Do yOu cEnTer A dIv? -->
</body>
</html>
