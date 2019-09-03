

<!DOCTYPE html>

<html>
    <body>
        <blockquote>
        Vaša rešitev: {{ odgovor }} <br>
        Pravilna rešitev je {{ naloga.resitev }}.
        </blockquote>
        <p>
        Relativna napaka znasa {{napaka}}%.
        </p>
        <p> porabljen cas je enak {{porabljen_cas}}s.
        </p>

        <form action='/igra/{{id_igre}}/' method='get'>
        <button type='submit'>Nadaljuj</button>
        </form>
    </body>
</html>