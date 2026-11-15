# -*- coding: utf-8 -*-
# Riscrive i blocchi della home (IT + EN) da questa tabella. Rilancio sicuro: python automation/home_blocchi.py
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = [("pulizie-uffici","Pulizie uffici","Office cleaning"),("pulizie-condominiali","Pulizie condominiali","Building common areas"),
     ("pulizie-domestiche","Pulizie domestiche","Home cleaning"),("pulizie-fine-lavori","Fine lavori e post ristrutturazione","Post-renovation cleaning"),
     ("pulizie-industriali","Pulizie industriali","Industrial cleaning"),("pulizie-negozi-vetrine","Negozi e vetrine","Shops and shop windows"),
     ("pulizie-studi-medici","Studi medici e ambulatori","Medical offices"),("pulizie-hotel-bb-case-vacanza","Hotel, B&B e case vacanza","Hotels, B&B and holiday homes"),
     ("pulizia-vetrate-facciate","Vetrate e facciate","Windows and facades"),("pulizia-cucine-professionali","Cucine professionali","Professional kitchens"),
     ("lavaggio-moquette-tappeti","Moquette e tappeti","Carpets and rugs"),("lucidatura-pavimenti-marmo","Pavimenti in marmo","Marble floors"),
     ("pulizia-pannelli-fotovoltaici","Pannelli fotovoltaici","Solar panels"),("igienizzazione-sanificazione","Igienizzazione ambienti","Surface sanitising")]
C = [("roma","Roma"),("fiumicino","Fiumicino"),("pomezia","Pomezia"),("guidonia","Guidonia"),("tivoli","Tivoli"),("monterotondo","Monterotondo"),("mentana","Mentana"),("civitavecchia","Civitavecchia")]
T = {
 "it": dict(
  eb="Pulizie a Roma e provincia", h1="Pulizie professionali per uffici, condomini e case, <em>a Roma e provincia.</em>",
  lead="Ci dici dove e cosa c'e' da pulire, ti rispondiamo con un preventivo. Interventi periodici o una tantum, con orari concordati.",
  b1="Richiedi un preventivo", b2="Vedi i servizi",
  cyc=[("Ci scrivi","Indirizzo, metri quadrati e qualche foto, anche su WhatsApp"),("Ti rispondiamo","Con un preventivo e, se serve, un sopralluogo"),("Concordiamo gli orari","Anche fuori orario di lavoro o nel weekend"),("Si parte","Una volta o con cadenza periodica")],
  se="Cosa facciamo", sh="I nostri servizi di pulizia", sl="Dal singolo ufficio al condominio, dalla casa al capannone.",
  ce="Dove lavoriamo", ch="Roma e provincia", cl="Scegli la tua zona per vedere i servizi disponibili.",
  pe="A chi ci rivolgiamo", ph="Chi si trova bene con noi",
  pl=[("Privati","Pulizie periodiche della casa","Pulizia di fondo e dopo i lavori"),("Condomini","Scale, androni e parti comuni","Calendario concordato con l'amministratore"),("Attivita' e negozi","Uffici, negozi e vetrine","Interventi fuori orario di apertura"),("Strutture ricettive","Camere tra un check-out e il successivo","Pulizie di inizio stagione")],
  me="Come lavoriamo", mh="Dalla richiesta alla pulizia",
  ml=[("Ci scrivi","Ci racconti cosa c'e' da pulire."),("Preventivo","Ti rispondiamo con una proposta chiara."),("Orari","Decidiamo insieme quando intervenire."),("Pulizia","Facciamo il lavoro e restiamo a disposizione.")],
  ke="Contatti", kh="Scriviamoci", kl="Raccontaci di cosa hai bisogno, ti rispondiamo appena possibile.", kb="Richiedi un preventivo", pre="Pulizie a "),
 "en": dict(
  eb="Cleaning in Rome and surroundings", h1="Professional cleaning for offices, buildings and homes, <em>in Rome and surroundings.</em>",
  lead="Tell us where and what needs cleaning and we will reply with a quote. Regular or one-off visits, at times we agree with you.",
  b1="Request a quote", b2="See services",
  cyc=[("You write to us","Address, floor area and a few photos, also on WhatsApp"),("We reply","With a quote and, if needed, a site visit"),("We agree the times","Also out of hours or at weekends"),("We start","One-off or on a regular schedule")],
  se="What we do", sh="Our cleaning services", sl="From a single office to a whole building, from a home to a warehouse.",
  ce="Where we work", ch="Rome and surroundings", cl="Choose your area to see the available services.",
  pe="Who we work for", ph="Who works well with us",
  pl=[("Homes","Regular home cleaning","Deep cleaning and after works"),("Buildings","Stairs, halls and common areas","Schedule agreed with the manager"),("Businesses and shops","Offices, shops and windows","Visits outside opening hours"),("Accommodation","Rooms between check-out and check-in","Start-of-season cleaning")],
  me="How we work", mh="From request to clean",
  ml=[("You write to us","Tell us what needs cleaning."),("Quote","We reply with a clear proposal."),("Times","We decide together when to come."),("Cleaning","We do the work and stay available.")],
  ke="Contact", kh="Get in touch", kl="Tell us what you need and we will reply as soon as possible.", kb="Request a quote", pre="Cleaning in "),
}
def build(l):
    t = T[l]; i = 1 if l == "it" else 2
    cyc = "".join('<div><b>%s</b><span>%s</span></div>' % c for c in t["cyc"])
    hero = '<div class="gc"><section class="ent-hero"><div class="gc-wrap gc-hero-in"><div><p class="gc-eyebrow">%s</p><h1 class="gc-h1">%s</h1><p class="gc-lead">%s</p><div class="gc-act"><a class="gc-btn gc-btn-a" href="__BASEURL__/contatti/">%s</a><a class="gc-btn gc-btn-o" href="__BASEURL__/servizi/">%s</a></div></div><div class="ent-cycle">%s</div></div></section></div>' % (t["eb"], t["h1"], t["lead"], t["b1"], t["b2"], cyc)
    cards = "".join('<div class="gc-pl ent-pl"><span class="n">%02d</span><b>%s</b></div>' % (n+1, ("<a href=\"/servizi/%s/\">%s</a>" % (s[0], s[1])) if l == "it" else s[2]) for n, s in enumerate(S))
    serv = '<div class="gc"><section class="gc-sec gc-soft" id="servizi"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><div class="gc-plat ent-4">%s</div><p><a class="gc-btn gc-btn-k" href="__BASEURL__/servizi/">%s</a></p></div></section></div>' % (t["se"], t["sh"], t["sl"], cards, t["b2"])
    ci = "".join('<div class="gc-pl ent-pl"><b><a href="/servizi/pulizie-%s/">%s%s</a></b></div>' % (s, t["pre"], n) for s, n in C)
    citta = '<div class="gc"><section class="gc-sec" id="zone"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><div class="gc-plat ent-4">%s</div></div></section></div>' % (t["ce"], t["ch"], t["cl"], ci)
    pl = "".join('<div class="gc-pl ent-pl"><b>%s</b><ul><li>%s</li><li>%s</li></ul></div>' % p for p in t["pl"])
    perchi = '<div class="gc"><section class="gc-sec gc-soft" id="perchi"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><div class="gc-plat ent-4">%s</div></div></section></div>' % (t["pe"], t["ph"], pl)
    ml = "".join('<div class="gc-pl"><span class="n">%02d</span><b>%s</b><p>%s</p></div>' % (n+1, a, b) for n, (a, b) in enumerate(t["ml"]))
    metodo = '<div class="gc"><section class="gc-sec" id="metodo"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><div class="gc-plat ent-4">%s</div></div></section></div>' % (t["me"], t["mh"], ml)
    cont = '<div class="gc"><section class="gc-sec gc-dark" id="contatti"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><a class="gc-btn" href="__BASEURL__/contatti/">%s</a></div></section></div>' % (t["ke"], t["kh"], t["kl"], t["kb"])
    names = [("hero","Hero",hero),("servizi","Servizi",serv),("zone","Zone",citta),("perchi","A chi ci rivolgiamo",perchi),("metodo","Come lavoriamo",metodo),("contatti","Contatti",cont)]
    return [dict(id=a, nome=b, enabled=True, html=c) for a, b, c in names]
for l, p in (("it", "_data/blocks_home.json"), ("en", "_data/i18n/en/blocks_home.json")):
    with open(os.path.join(R, p), "w", encoding="utf-8", newline="\n") as f:
        json.dump(build(l), f, ensure_ascii=False, indent=2)
print("ok")
