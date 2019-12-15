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

      <input id="submit" type="submit" value="Start Simulation" >

      </form>

<p>Calculate the probability of an data point being more extreme than a certain x-value.</p>

<form action="" id="form2">
		<input type="hidden" id="mean" name="mean">
		<input type="hidden" id="stdev" name="stdev">
       
		<table>
		<tbody>
			<tr>
				<td nowrap="nowrap">x-value:</td>
				<td><input type="text" name="argument" size="15"></td>
			</tr>
			<tr>
				<td nowrap="nowrap">Probability:</td>
				<td><input type="text" NAME="result" SIZE="15"></td>
			</tr>
		</tbody>
		</table>

		<input id="calc" type="button" value="Calculate" onclick="compute(this.form)" disabled>

	</form>
    </td>
    <td id="right">
    
    </td>
  </tbody>
</table>

<SCRIPT LANGUAGE="JavaScript">
<!-- hide this script tag's contents from old browsers

function normalcdf(X){   //HASTINGS.  MAX ERROR = .000001
	var T=1/(1+.2316419*Math.abs(X));
	var D=.3989423*Math.exp(-X*X/2);
	var Prob=D*T*(.3193815+T*(-.3565638+T*(1.781478+T*(-1.821256+T*1.330274))));
	if (X>0) {
		Prob=1-Prob
	}
	return Prob
}   

function compute(form) {
    Z=eval(form.argument.value)
    M=eval(form.mean.value)
    SD=eval(form.stdev.value)
    with (Math) {
		if (SD<0) {
			alert("The standard deviation must be nonnegative.")
		} else if (SD==0) {
		    if (Z<M){
		        Prob=0
		    } else {
			    Prob=1
			}
		} else {
			if (Z<M) {
      	Prob=normalcdf((Z-M)/SD);
				Prob=round(100000*Prob)/100000;
      } else {
      	Prob=1-normalcdf((Z-M)/SD);
        Prob=round(100000*Prob)/100000;
      }
		}
	}
    form.result.value = Prob;
}
// done hiding from old browsers -->
</SCRIPT>
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
  
  document.getElementById("submit").disabled = true;
  
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
      document.getElementById('mean').value = data[key];
      } else if(key == "StDev"){
      tr.innerHTML = key + " = " + data[key];
      document.getElementById('stdev').value = data[key];
      } else {
      value = String(data[key]).replace(/,/g,', ');
      tr.innerHTML = key + " = " + value;
      }
      
      maincontainer.appendChild(tr);
    }
  }
  )
  .catch(error => alert("ERROR", error));
  
  document.getElementById("calc").disabled = false;
  
  event.preventDefault();
  }
</script>
