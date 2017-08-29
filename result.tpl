<link rel="stylesheet" href="bottle.css" rel="stylesheet">
<link rel="stylesheet" href="style.css" rel="stylesheet">

<div class="well"><h1>Invoice Export</h1></div>

<div class="box"><h4>Result of the validation</h3></div>

 <div class="bcontainer">

%if len(errors) > 0:
<table class="table">
    <tr>
        <th>Row</th>
        <th>Level</th>
        <th>Type</th>
        <th>Message</th>
    </tr>
    %for error in errors:
        <tr>
            <td>{{error.line}}
            <td>{{error.level_name}}
            <td>{{error.type_name}}
            <td>{{error.message}}    
        </tr>
    %end
</table>
%else:
<div class="tx-lt-green">
<h3>The uploaded XML is valid against the latest scheme provided by the Hungarian Tax Authority.</h3>
</div>
%end


<form action="/goback" method="POST">
    <input type ="submit" value="« Go back" class="btn bg-lt-orange">
</form>

</div>