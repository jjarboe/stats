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
          <td nowrap="nowrap">p</td>
          <td><input value="" id="p" name="mean"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">n</td>
          <td><input value="" name="number of trials" id="n"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">b</td>
          <td><input value="" name="size of bins" id="b"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">t</td>
          <td><input value="" name="size of trials" id="t"></td>
        </tr>
        <tr>
          <td nowrap="nowrap">s</td>
          <td><input value="" name="seed" id="s"></td>
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
    for(var key in data){
      var tr = document.createElement("tr");
      tr.setAttribute('style', 'width: ' + (width-(width/6))/2 + 'px; word-break: break-all;')
      
      if (key.includes("dataurl")) {
      tr.innerHTML = '<img style="max-height: ' + height + '; width: auto" src="' + data[key] + '" alt="A very important graph.">';
      } else {
      tr.innerHTML = key + " = " + data[key].replace(',',', ');
      }
      
      maincontainer.appendChild(tr);
    }
  }
  )
  .catch(error => alert("ERROR", error));
  
  
  event.preventDefault();
  }
</script>
