<link rel="stylesheet" href="bottle.css" rel="stylesheet">
<link rel="stylesheet" href="style.css" rel="stylesheet">

<div class="well"><h1>Invoice Export</h1></div>

<div class="header">

<div class=" bcontainer  header-text">
    <h3>A tool to validate XML files against the XSD scheme of the Tax Authority</h3>
    <p>Upload the XML file generated by your invoicing software and this solution will validate it against the scheme provided by the Tax Authority and checks for formal errors</p>
</div>

</div>

<div class="bcontainer">

<form action="/upload" method="post" enctype="multipart/form-data">    
    <input id="upload" type="file" value="Select File" name="upload" /> 
    %if (message):
    <div class="tx-lt-red">
      <h4>{{message}}</h4>
    </div>
    %end  
    <br />
  <input type="submit" value="Upload" class="btn bg-lt-orange"/>
</form>

</div>