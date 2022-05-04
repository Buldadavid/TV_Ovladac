<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO8859-2">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ovladač</title>
</head>
<style>
h1   {color: white;
    font: 45px Times;
    font-weight: bold;
}

body {
text-align: left;
background-color: #444444;
font: Arial, sans-serif;
}
.center {
  margin-left: auto;
  margin-right: auto;
  width: 100px;
}
#greet1 {
    background-color: #222222;
    border:  none;
    border-radius: 5px;
    color: white;
    font: 20px Arial, sans-serif;
    height: 50px;
    width: 100%;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}
table, td, td {
  border: 1px solid black;
  color: white;
}
tr{height: 60px;}
    </style>
<body>
<?php
    if(!file_exists("/home/pi/TV/epg.txt"))
    {
        echo "The file from above cannot be found!";
        exit;
    }
    
    $fp = fopen("/home/pi/TV/epg.txt", "r");
    
    if(!$fp)
    {
        echo "Somehow the file cannot be opened! :)";
        exit;
    }
    echo "<table>";
    $counter = 1;
    while(!feof($fp))
    {
        $zeile = fgets($fp);
        echo "<tr><td>$counter</td>";
        echo "<td>$zeile</td>";
        $counter++;
    }
        echo "</table>";
    fclose($fp)
    
?>
<a href="http://10.0.0.200:5000">
   <input type="button" value="Zpět" id = "greet1" />
</a>
</body>
</html>