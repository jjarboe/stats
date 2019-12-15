<script type="text/javascript">
   fetch("https://api.github.com/repos/frostforth/stats/contents/Gallery?ref=gh-pages")
   .then(data => data.json())
   .then(data => {
      alert(data['download_url']);
   });
</script>
