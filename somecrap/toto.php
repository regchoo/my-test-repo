<!DOCTYPE html>
<html>
<head>
	<title> Your TOTO Lucky Numbers </title>
</head>

<body>

<h1><u>TOTO Numbers Generator</u></h1>
<p>
<h2>Press F5 to refresh or
<p>
<a href="javascript:history.go(0)">Click here to refresh page</a>
<p>
</h2>
<?php

$Type=6;
// Populate array with the 49 numbers
for ($Numbers=1;$Numbers<=49;$Numbers+=1)
	{
		$TotoArray[$Numbers] = $Numbers;
	}

//Select Toto numbers randomly
$Repeat=1;
while ($Repeat<=$Type)
	{
		$RandomIndex=rand(1, 49);
		while ($TotoArray[$RandomIndex]=="99")
			{
				$RandomIndex=rand(1, 49);
			}
		$SelectedTotoNum[$Repeat]=$TotoArray[$RandomIndex];
		$TotoArray[$RandomIndex]=99;
		$Repeat++;
	}

//Sort selected numbers and output in a table format
sort($SelectedTotoNum);
echo "<table border=4 cellpadding=12><tr>";
foreach ($SelectedTotoNum as $key => $val)
	{
    		echo "<td><font size=20>".$val."</td>";
	}	
echo "</tr></table>";
?>
</body>
</html>
