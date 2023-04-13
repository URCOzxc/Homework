<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Generic form-processing page</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<?php
function showit($var,$text="") {
  if (isset($_POST[$var])) {
    if ($text=="") {
      print $_POST[$var];
    } else {
      print $text;
    }
  }
}
//print "<pre>"; print_r($_POST); print "</pre>";
?>
<h1>Form results</h1>
<table border="1">
  <tr><th>Variable</th><th>Value</th></tr>
  <tr><td>Customer Name</td><td>
  <?php showit('custname'); ?>
  </td></tr>
  <tr><td>Customer Address</td><td>
  <?php showit('adr1'); ?>
  </td></tr>
  <tr><td>Shall we cut the grass?</td><td>
  <?php showit('cut'); ?>
  </td></tr>
  <tr><td>How tall a cut?</td><td>
  <?php showit('tall'); ?>
  </td></tr>
  <tr>
    <td>Trim the edges?</td>
    <td>  <?php showit('edge'); ?></td>
  </tr>
  <tr><td>Trim the hedges?</td><td>
  <?php showit('hedge') ?>
  </td></tr>
  <tr><td>Disposal Method</td><td>
  <?php showit('dispose'); ?>
  </td></tr>
  <tr><td>Urgency</td><td>
  <?php
    showit("when","When you get to it");
    showit("soon_x","Come soon");
    showit("help_y","Help!  I'm desperate.");
  ?>
  </td></tr>
</table><hr />
<h2>The information below is used for debugging your program.</h2>
<p>GET variables:</p>
<table border="1"><tr><th>Variable</th><th>Value</th></tr>
<?php
foreach($_GET as $p => $q) {
print("<tr><td>" . $p . "</td><td>" . $q . "</td></tr>");
}
?></table>
<p>POST variables:</p>
<table border="1"><tr><th>Variable</th><th>Value</th></tr>
<?php
foreach($_POST as $p => $q) {
print("<tr><td>" . $p . "</td><td>" . $q . "</td></tr>");
}
?>
</table>
</body>
</html>