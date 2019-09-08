<!DOCTYPE html>
<html>
    <head>
        <title>Racunomat</title>
        <meta charset = "UTF-8">
    </head>
    <body>
        <table width=550pt frame=box border=4>
            <tr>
                <th align=center>
                 <h1>{{seznam[0][1]}}---xxx*** Računoma+ ***xxx---{{seznam[0][1]}}</h1>
                </th>
            </tr>
            <tr>
                <td height=300pt align=center>
                    <ol>
% for podatek in seznam:
                    <li> {{podatek[0]}}  ...  {{podatek[1]}} </li>
% end
                    </ol>        
        
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