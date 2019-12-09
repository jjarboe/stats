<p hidden>
layout: page
title: "Simulation"
permalink: /simulation/
</p>

<table>
  <tbody>
    <td valign="top">
      <form id="form" action="http://localhost:8000/graphs/" method="get">
      <input type="hidden" name="present" value="1">

      <table border="0">
      <tbody>
        <tr>
          <td nowrap="nowrap">mean:</td>
          <td><input value="" name="p"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">number of trials:</td>
          <td><input value="" name="n"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">size of bins:</td>
          <td><input value="" name="b"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">size of trials:</td>
          <td><input value="" name="t"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">seed:</td>
          <td><input value="" name="s"></td>
        </tr>
      </tbody>
      </table>

      <input type="submit" value="Start Simulation" >

      </form>
    </td>
    <td id="right">
    
    </td>
  </tbody>
</table>


<script>
  
  var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var height = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;
  
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
  .then(data => {

    var maincontainer = document.getElementById("right")
    
    while (maincontainer.firstChild) {
      maincontainer.removeChild(element.firstChild);
    }
    
    for(var key in data){
      var tr = document.createElement("tr");
      tr.setAttribute('style', 'width: ' + (width-(width/6))/2 + 'px; word-break: normal;')
      
      if (key.includes("dataurl")) {
      tr.innerHTML = '<img style="max-height: ' + height + '; width: auto" src="' + data[key] + '" alt="A very important graph.">';
      } else {
      value = String(data[key]).replace(/,/g,', ');
      tr.innerHTML = key + " = " + value;
      }
      
      maincontainer.appendChild(tr);
    }
  }
  )
  .catch(error => alert("ERROR", error));
  
  
  event.preventDefault();
  }
</script>
