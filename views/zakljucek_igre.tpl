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
        
       <p>
       Vaš končni rezultat je: {{izkupicek}}.
        </p>
% if mesto == False:
        
        <form action='/' method='get'>
        <button type='submit'>Na zacetno stran</button>
        </form>
% else:
        <p>
            Na lestvici ste dosegli {{mesto}}. mesto.
        </p>
        <form action='/igra/{{id_igre}}/zapis_rezultatov/{{mesto}}/' method="POST">
            Ime: <input type="text" name='ime'>
            <button type='submit'>Potrdi</button>
        </form>
% end
           
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