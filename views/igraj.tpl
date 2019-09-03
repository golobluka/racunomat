% import time

<!DOCTYPE html>
<html>
    <head>
        <title>Pozdrav na strani</title>
    </head>
    <body>
       <blockquote>
       Izdan je bil račun: {{ naloga.zapis }}({{ naloga.x }})
        </blockquote>

        <form action='/igra/{{id_igre}}/{{resitev}}/' method='get'>
            Rešitev:
            <input type='text' name='odgovor'>
            <button, type = 'submit' >      ... v potrditev pritisnite tipko Enter</button>

<script>
var input = document.getElementById("myInput");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("myBtn").click();
  }
});
</script>

        </form>



       
        

    </body>
</html>