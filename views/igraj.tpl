<!DOCTYPE html>
<html>
    <head>
        <title>Racunomat</title>
    </head>
    <body>
        <table width=550pt frame=box border=4>
            <tr>
                <th align=center>
                 <h1>{{izkupicek}}---xxx*** Računoma+ ***xxx---{{izkupicek}}</h1>
                </th>
            </tr>
            <tr>
                <td height=300pt align=center>
       <blockquote>
       Izdan je bil račun: 
       <h3>{{ naloga.zapis }}({{ naloga.x }})</h3>
        </blockquote>

        <form action='/igra/{{id_igre}}/odgovor/' method='get'>
            Rešitev:
            <input type='text' name='odgovor'>
            <button, type = 'submit' placeholder="vnesi rezultat" >     
            </button>

<!-- Tu sem zaradi lažjega izvajanja igre prikopiral del kode -->           
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
        <p><small> ... v potrditev pritisnite tipko Enter</small></p>
        
                </td>
            </tr>
            <tr height=30pt>
                <td>
                    <form action="/" method="get">
                    <button type="submit">Menu</button>
                    </form>
                </td>
            <tr>
        </table>

    </body>
</html>