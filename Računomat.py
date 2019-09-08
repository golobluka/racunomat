import bottle, razredi, time
bottle.TEMPLATE_PATH.insert(0, '\\views')
racunomat = razredi.Racunomat()

@bottle.get('/')
def pozdravi():
        return bottle.template('menu.tpl')
    
@bottle.post('/igra/')
def nova_igra():
        id_igre = racunomat.nova_igra()
        bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/lestvica/')
def prikazi_lestvico():
        seznam = racunomat.preberi_lestvico()
        return bottle.template('lestvica.tpl',seznam = seznam)


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
        
        naloga = razredi.Racun(razredi.seznam_formul)
        racunomat.igre[id_igre][0] = naloga
        resitev = naloga.izberi_racun()
        izkupicek = racunomat.igre[id_igre][1]
        
        return bottle.template('igraj.tpl',
        naloga = naloga,
        resitev = resitev,
        id_igre = id_igre,
        izkupicek = izkupicek 
        )

@bottle.get('/igra/<id_igre:int>/odgovor/')
def odgovor(id_igre):
        naloga = racunomat.igre[id_igre][0] 
        odgovor = bottle.request.query.getunicode('odgovor')
        
        if naloga.je_stevilo(odgovor):
                odgovor = float(odgovor)
        else:
                return bottle.template('naroben_unos.tpl',
                id_igre = id_igre, 
                izkupicek = racunomat.igre[id_igre][1]
                )
        
        porabljen_cas = round(time.time() - naloga.cas)

        tocke = razredi.tockar(odgovor, naloga.resitev, porabljen_cas )
        izkupicek = racunomat.dodaj_tocke(id_igre, tocke)

        konec = racunomat.konec_igre(id_igre)
        racunomat.dodaj_krog(id_igre)
        
        return bottle.template('izpis_rezultatov.tpl',
        id_igre = id_igre,
        naloga = naloga,
        odgovor = odgovor,
        napaka = naloga.relativna_napaka(odgovor),
        porabljen_cas = porabljen_cas,
        tocke = tocke,
        izkupicek = izkupicek,
        konec = konec
        )

@bottle.get('/igra/<id_igre:int>/zakljucek/')
def zakljucek(id_igre):
        mesto, vrstice = racunomat.preveri_izkopicek(id_igre)
        izkupicek = racunomat.igre[id_igre][1]
        
        
        return bottle.template('zakljucek_igre.tpl',
        id_igre = id_igre,
        mesto = mesto,
        izkupicek = izkupicek
        )

@bottle.post('/igra/<id_igre:int>/zapis_rezultatov/<mesto:int>/')
def zapis_rezultatov(id_igre, mesto):
        ime = bottle.request.forms['ime']
        izkupicek = racunomat.igre[id_igre][1]
        racunomat.spremeni_lestvico(mesto,ime, izkupicek)

        bottle.redirect('/')


                


        
bottle.run(reloader=True, debug=True)




