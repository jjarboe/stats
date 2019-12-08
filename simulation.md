<---
layout: page
title: "Simulation"
permalink: /simulation/
--->

<table>
  <tbody>
    <td>
      
    </td>
    <td id="right">
    
    </td>
  </tbody>
</table>


<form id="form" action="http://localhost:8000/graphs/" method="get">
<input type="hidden" name="present" value="1">
  
<table border="0">
<tbody>
  <tr>
    <td nowrap="nowrap">p</td>
    <td><input value="" id="mean" name="p"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">n</td>
    <td><input value="" id="number of trials" name="n"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">b</td>
    <td><input value="" id="size of bins" name="b"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">t</td>
    <td><input value="" id="size of trials" name="t"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">s</td>
    <td><input value="" name="s"></td>
  </tr>
</tbody>
</table>

<input type="submit" value="Start Simulation" >

</form>

<script>
  var f = document.getElementById("form");
  f.onsubmit=SubmitForm;
  function SubmitForm(event){
  var url = f.action;
  var data = (fetch(url, {
          method:"POST", 
          body: new FormData(f)
    })
    .then(response => response.json())
  )
  .then(data => data)
  .catch(error => alert("ERROR", error));
  
  alert(data);
  event.preventDefault();}
  
  var maincontainer = document.getElementById("right")
  for(var key in data){
  alert(key + " = " + data[key]);
  }
</script>
