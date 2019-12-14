<p hidden>
layout: page
title: "Simulation"
permalink: /simulation/
</p>

<table>
  <tbody>
    <td valign="top">
      <form id="form" action="https://blooming-reaches-62688.herokuapp.com/graphs/" method="get">
      <input type="hidden" name="present" value="1">

      <table border="0">
      <tbody>
        <tr>
          <td nowrap="nowrap">mean:</td>
          <td><input value="" name="m"></td>
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
      <form id="calc">
          <input type="hidden" id="mean" value="0">
          <input type="hidden" id="stdev" value="0">
      <table>
      <tbody>
        <tr>
          <input id = "x" value="" name="As extreme as:">
        </tr>
        <tr id="prop">
        </tr>
      </tbody>
      </table>
      
      <input id="prop_btn" type="button" value="Calculate Proportion">
      
      </form>
    </td>
    <td id="right">
    
    </td>
  </tbody>
</table>

<script>

  //function cdfNormal (x, mean, standardDeviation) {
  //  return (1 - math.erf((mean - x ) / (Math.sqrt(2) * standardDeviation))) / 2
  //}
  
  document.getElementById("prop_btn").onclick = (e => {
  var m = document.getElementById('mean').value;
  var s = document.getElementById('stdev').value;
  var x = document.getElementById('x').value;
  var p = 0;
  
  var formula = "(1 - erf( (("+m+") - ("+x+")) / (sqrt(2) * ("+s+")) ) / 2)".replace(/ /g, "");
  p = fetch("https://api.mathjs.org/v4/?expr="+encodeURIComponent(formula))
      .then(response => response.text())
      .then(data => {
        if(x < m){
          p = data;
        } else if(x >= m){
          p = 1-data;
        }
  
        document.getElementById('prop').innerHTML = "Proportion of samples: " + p;
      });
  });
  
</script>
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
      tr.setAttribute('style', 'width: ' + (width-(width/6))/2 + 'px; word-break: normal;')
      
      if (key.includes("dataurl")) {
      tr.innerHTML = '<img style="height: ' + height/2 + '; width: auto" src="' + data[key] + '" alt="A very important graph.">';
      } else if(key == "mean"){
      tr.innerHTML = key + " = " + data[key];
      document.getElementById('mean').value = value;
      } else if(key == "StDev"){
      tr.innerHTML = key + " = " + data[key];
      document.getElementById('stdev').value = value;
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
