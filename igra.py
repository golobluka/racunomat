import bottle, razredi, time
bottle.TEMPLATE_PATH.insert(0, 'C:\\Users\\uka\\Documents\\vsc\\Python\\računomat\\views')
racunomat = razredi.Racunomat()

@bottle.get('/')
def pozdravi():
        return bottle.template('menu.tpl')
    
@bottle.post('/igra/')
def nova_igra():
        id_igre = racunomat.nova_igra()
        bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
        
        naloga = racunomat.igre[id_igre][0]
        tocke = racunomat.igre[id_igre][1]
        resitev = naloga.izberi_racun()
        
        return bottle.template('igraj.tpl',
        naloga = naloga,
        resitev = resitev,
        tocke =tocke,
        id_igre = id_igre
        
       
        )

@bottle.get('/igra/<id_igre:int>/<resitev>/')
def odgovor(id_igre, resitev):
        naloga = racunomat.igre[id_igre][0]
        odgovor = bottle.request.query.getunicode('odgovor')
        if odgovor.isdigit():
                odgovor = float(odgovor)
        else:
                return bottle.template('naroben_unos.tpl',
                id_igre = id_igre
                )
        porabljen_cas = time.time() - naloga.cas
        
        return bottle.template('izpis_rezultatov.tpl',
        id_igre = id_igre,
        naloga = naloga,
        odgovor = odgovor,
        napaka = naloga.relativna_napaka(odgovor),
        porabljen_cas = porabljen_cas
        )



                


        
bottle.run(reloader=True, debug=True)




