layout: page
title: "Simulation"
permalink: /simulation/


<form action="http://localhost:8000/graphs/" method="get">

<table border="0">
<tbody>
  <tr>
    <td nowrap="nowrap">p</td>
    <td><input value="" name="p"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">n</td>
    <td><input value="" name="n"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">b</td>
    <td><input value="" name="b"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">t</td>
    <td><input value="" name="t"></td>
  </tr>
  <tr>
    <td nowrap="nowrap">s</td>
    <td><input value="" name="s"></td>
  </tr>
</tbody>
</table>

<input type="submit" OnSubmit="return SubmitForm()" value="Draw Sample" >

</form>

<script>
  function SubmitForm(){
  alert ("HOWDY"); return 0;}
</script>
