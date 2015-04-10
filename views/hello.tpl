<!DOCTYPE html>
<html>
<head>
    <title>Hello world</title>
</head>
<body>
<p>
    welcome {{username}}

<p>
<ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
</ul>
<p>

<form action="/fav_fruit" method="POST">
    what is your favourite fruit?
    <input type="text" name="fruit" size="40" value=""><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>