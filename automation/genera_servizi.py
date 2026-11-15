# genera_servizi.py - crea _servizi/ (servizio base + servizio per citta) e le pagine citta per dittapulizie.
# Rilanciabile: sovrascrive i file generati (stessi nomi). Dati in cima: SERVIZI e CITTA.
# NON scrive prezzi, orari, abilitazioni o garanzie: non sono dati reali (aggiungerli solo se veri).
import os, io
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, '_servizi')
PAGES = os.path.join(BASE, '_pages')
os.makedirs(OUT, exist_ok=True)

SERVIZI = [
 dict(slug='pulizie-uffici', nome='Pulizie uffici', per='uffici, studi professionali e spazi di lavoro',
  intro='Postazioni, sale riunioni, bagni, aree comuni e pavimenti sempre in ordine, con interventi concordati sugli orari di lavoro.',
  voci=['pulizia di scrivanie, superfici e arredi', 'sanificazione dei servizi igienici', 'lavaggio pavimenti e aspirazione', 'svuotamento cestini e raccolta differenziata', 'pulizia di vetri interni e porte'],
  q='Ogni quanto passate in ufficio?', a='La frequenza si decide insieme: ogni giorno, più volte a settimana o una volta a settimana. Anche fuori orario, per non disturbare il lavoro.'),
 dict(slug='pulizie-condominiali', nome='Pulizie condominiali', per='condomini, scale, androni e garage',
  intro='Scale, androni, ascensori e parti comuni puliti con un calendario fisso, per amministratori e condomini.',
  voci=['pulizia di scale, pianerottoli e androni', 'pulizia di ascensori e corrimano', 'lavaggio di garage e cortili', 'pulizia di vetri e portoni', 'gestione di spazi comuni e locali tecnici'],
  q='Lavorate con gli amministratori di condominio?', a='Sì, il preventivo si prepara su misura per lo stabile (piani, scale, garage) e si può concordare un calendario settimanale.'),
 dict(slug='pulizie-domestiche', nome='Pulizie domestiche', per='appartamenti e ville',
  intro='Casa pulita senza pensieri: pulizie periodiche o una tantum, anche di fondo, per appartamenti e ville.',
  voci=['pulizia di cucina, bagni e camere', 'pavimenti, polvere e superfici', 'pulizia di vetri e infissi', 'pulizia di fondo (frigo, forno, armadi)', 'riordino leggero su richiesta'],
  q='Posso prenotare una sola pulizia?', a='Sì, puoi chiedere una pulizia una tantum, di fondo oppure un servizio periodico (settimanale o ogni due settimane).'),
 dict(slug='pulizie-fine-lavori', nome='Pulizie fine lavori e post ristrutturazione', per='cantieri, ristrutturazioni e nuove costruzioni',
  intro='Dopo i lavori restano polvere di cantiere, residui di vernice, cemento e stucco. Li togliamo e consegniamo l\'ambiente pronto da vivere.',
  voci=['rimozione di polvere fine su superfici e arredi', 'pulizia di vetri e infissi con residui di cantiere', 'pulizia di pavimenti e rivestimenti', 'rimozione di residui di stucco, silicone e vernice', 'pulizia di bagni, cucine e sanitari'],
  q='Quanto tempo serve dopo la fine dei lavori?', a='Dipende da metri quadrati e da quanto è sporco il cantiere. Con foto e metratura si prepara un preventivo e si concorda il giorno.'),
 dict(slug='igienizzazione-sanificazione', nome='Igienizzazione e sanificazione ambienti', per='uffici, negozi, locali e abitazioni',
  intro='Igienizzazione delle superfici e degli ambienti con prodotti professionali, a cicli o dopo un evento particolare.',
  voci=['igienizzazione di superfici ad alto contatto', 'trattamento di sale, locali e bagni', 'cicli programmati per uffici e negozi', 'intervento dopo traslochi o ristrutturazioni'],
  q='Rilasciate un documento dell\'intervento?', a='Nel preventivo indichiamo il tipo di intervento e la documentazione prevista. Per esigenze particolari parlane prima della prenotazione.'),
 dict(slug='pulizia-vetrate-facciate', nome='Pulizia vetrate e facciate', per='vetrate, vetrine, serramenti e facciate',
  intro='Vetri senza aloni, dalle vetrine di negozio alle grandi vetrate di uffici e condomini.',
  voci=['pulizia di vetrate e serramenti', 'vetrine e ingressi di negozi', 'finestre e balconi', 'pulizia dopo lavori', 'interventi periodici programmati'],
  q='Pulite anche i piani alti?', a='Dipende dall\'altezza e dall\'accesso. Mandaci foto e indirizzo: valutiamo l\'intervento e ti diciamo come procedere.'),
 dict(slug='pulizie-industriali', nome='Pulizie industriali e capannoni', per='capannoni, magazzini e ambienti produttivi',
  intro='Ambienti grandi, polvere e sporco difficile: pulizie industriali pianificate con attrezzature adatte alla superficie.',
  voci=['lavaggio meccanico di pavimenti industriali', 'pulizia di magazzini e depositi', 'pulizia di uffici e spogliatoi annessi', 'pulizia di macchinari e superfici (su accordo)', 'interventi straordinari a fine produzione'],
  q='Lavorate anche di notte o nel weekend?', a='Gli orari si concordano con l\'azienda, così la produzione non si ferma.'),
 dict(slug='pulizie-negozi-vetrine', nome='Pulizie negozi e vetrine', per='negozi, showroom e locali commerciali',
  intro='Un negozio pulito vende meglio: pavimenti, vetrine, camerini e bagni in ordine prima dell\'apertura.',
  voci=['pavimenti e superfici di vendita', 'vetrine e ingressi', 'camerini, bagni e retro', 'pulizie prima dell\'apertura', 'pulizie di fondo periodiche'],
  q='Potete venire prima dell\'apertura?', a='Sì, il servizio si può svolgere la mattina presto, la sera dopo la chiusura o nel giorno di riposo.'),
 dict(slug='pulizie-studi-medici', nome='Pulizie studi medici e ambulatori', per='studi medici, dentisti e ambulatori',
  intro='Ambienti sanitari che chiedono attenzione ai dettagli: pulizia ordinaria e igienizzazione concordate con lo studio.',
  voci=['pulizia di sale visita e sale d\'attesa', 'bagni e servizi', 'pavimenti e superfici', 'igienizzazione periodica', 'protocolli concordati con il responsabile dello studio'],
  q='Seguite le procedure del mio studio?', a='Sì, prima di iniziare ci facciamo indicare le procedure dello studio e le mettiamo in un piano di pulizie scritto.'),
 dict(slug='pulizie-hotel-bb-case-vacanza', nome='Pulizie hotel, B&B e case vacanza', per='hotel, B&B, affittacamere e case vacanza',
  intro='Camere e appartamenti pronti per il prossimo ospite: cambio biancheria, pulizia completa e controllo finale tra un soggiorno e l\'altro.',
  voci=['pulizia di camere e bagni tra un ospite e l\'altro', 'cambio biancheria (su accordo)', 'pulizia di parti comuni e colazioni', 'pulizie di fondo a inizio stagione', 'controllo finale con foto'],
  q='Gestite i cambi in giornata?', a='Si può programmare il servizio sugli orari di check-out e check-in. Dicci quante camere e quante partenze hai a settimana.'),
 dict(slug='lavaggio-moquette-tappeti', nome='Lavaggio moquette e tappeti', per='moquette, tappeti e rivestimenti tessili',
  intro='Moquette e tappeti riportati a nuovo con lavaggio profondo e rimozione delle macchie, in ufficio e a casa.',
  voci=['lavaggio di moquette in uffici e negozi', 'lavaggio di tappeti', 'rimozione di macchie', 'trattamento di divani e rivestimenti', 'asciugatura rapida'],
  q='Quanto tempo ci mette ad asciugare?', a='Dipende dal materiale e dall\'ambiente. Indichiamo i tempi nel preventivo, così pianifichi l\'uso dello spazio.'),
 dict(slug='lucidatura-pavimenti-marmo', nome='Lucidatura pavimenti e marmo', per='marmo, graniglia, parquet e pavimenti in pietra',
  intro='Pavimenti opachi o segnati ritrovano luce con levigatura e lucidatura adatte al materiale.',
  voci=['lucidatura di marmo e graniglia', 'trattamento di pavimenti in pietra', 'rimozione di aloni e segni', 'protezione della superficie', 'manutenzione periodica'],
  q='Come scegliete il trattamento?', a='In base al materiale e al suo stato: con foto e metratura valutiamo e proponiamo l\'intervento più adatto.'),
 dict(slug='pulizia-cucine-professionali', nome='Pulizia cucine professionali', per='ristoranti, bar, mense e cucine industriali',
  intro='Cappe, piani di lavoro, forni e pavimenti di cucina puliti a fondo, in orari che non fermano il servizio.',
  voci=['pulizia di piani di lavoro e attrezzature', 'sgrassaggio di forni, piastre e friggitrici', 'pulizia di cappe e filtri', 'pavimenti e scarichi', 'pulizie a fondo programmate'],
  q='Intervenite a locale chiuso?', a='Sì, di solito la sera dopo la chiusura o nel giorno di riposo, per lasciare la cucina pronta all\'apertura.'),
 dict(slug='pulizia-pannelli-fotovoltaici', nome='Pulizia pannelli fotovoltaici', per='impianti fotovoltaici su tetto e a terra',
  intro='Polvere, smog e foglie riducono il rendimento dei pannelli: una pulizia periodica li riporta in efficienza.',
  voci=['lavaggio dei pannelli con acqua trattata', 'pulizia su tetto e a terra', 'rimozione di foglie e residui', 'controllo visivo dell\'impianto', 'interventi periodici'],
  q='Con che frequenza va fatta?', a='Dipende dalla zona e dall\'inclinazione. Di solito una o due volte l\'anno: ne parliamo nel preventivo.'),
]

CITTA = [
 dict(slug='roma', nome='Roma', zone='Roma e quartieri come Eur, Prati, Parioli, Trastevere, Tiburtina e Ostiense', target='uffici, condomini, negozi e strutture ricettive di tutta la città'),
 dict(slug='fiumicino', nome='Fiumicino', zone='Fiumicino, Isola Sacra, Focene e Maccarese', target='attività, case vacanza e strutture ricettive del litorale'),
 dict(slug='pomezia', nome='Pomezia', zone='Pomezia, Torvaianica e Santa Palomba', target='aziende, magazzini e attività della zona industriale e del litorale'),
 dict(slug='guidonia', nome='Guidonia Montecelio', zone='Guidonia Montecelio, Villanova e Setteville', target='condomini, uffici e capannoni della zona est di Roma'),
 dict(slug='tivoli', nome='Tivoli', zone='Tivoli, Villa Adriana e Bagni di Tivoli', target='attività, condomini e strutture ricettive dell\'area tiburtina'),
 dict(slug='monterotondo', nome='Monterotondo', zone='Monterotondo e Monterotondo Scalo', target='condomini, studi, negozi e aziende della zona nord-est di Roma'),
 dict(slug='mentana', nome='Mentana', zone='Mentana, Fonte Nuova e Tor Lupara', target='condomini, uffici, negozi e abitazioni dell\'area nomentana'),
 dict(slug='civitavecchia', nome='Civitavecchia', zone='Civitavecchia, Santa Marinella e Allumiere', target='attività, strutture ricettive e condomini della costa nord'),
]

def q(s):  # testo sicuro dentro doppi apici YAML
    return s.replace('\\', '\\\\').replace('"', "'")

def scrivi(path, testo):
    with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(testo)

def pagina(sv, ct):
    luogo = ct['nome'] if ct else 'Roma e provincia'
    slug = sv['slug'] + ('-a-' + ct['slug'] if ct else '')
    titolo = '%s a %s' % (sv['nome'], luogo)
    exc = '%s a %s: servizio di ditta di pulizie per %s. Richiedi un preventivo.' % (sv['nome'], luogo, sv['per'])
    desc = '%s a %s con ditta di pulizie professionale per %s. Richiedi un preventivo su WhatsApp o dal modulo.' % (sv['nome'], luogo, sv['per'])
    faq = [
      (sv['q'], sv['a']),
      ('Dove lavorate?', ('Operiamo a %s. ' % ct['zone'] if ct else 'Operiamo a Roma e in provincia (Fiumicino, Pomezia, Guidonia, Tivoli, Monterotondo, Mentana, Civitavecchia e dintorni). ') + 'Scrivici indirizzo e tipo di intervento.'),
      ('Come arrivo al preventivo?', 'Ci mandi indirizzo, metri quadrati e qualche foto (anche su WhatsApp). Ti rispondiamo con un preventivo e, se serve, fissiamo un sopralluogo.'),
    ]
    L = ['---', 'layout: single', 'in_home: false', 'title: "%s"' % q(titolo)]
    if ct: L.append('citta: "%s"' % q(ct['nome']))
    L += ['excerpt: "%s"' % q(exc), 'seo_description: "%s"' % q(desc), 'categories:', '  - servizi', 'faq:']
    for dq, da in faq:
        L += ['  - q: "%s"' % q(dq), '    a: "%s"' % q(da)]
    L += ['---', '']
    if ct:
        L.append('%s a %s: lavoriamo per %s. %s' % (sv['nome'], ct['nome'], ct['target'], sv['intro']))
    else:
        L.append('%s a Roma e in provincia, per %s. %s' % (sv['nome'], sv['per'], sv['intro']))
    L += ['', '{% include servizio-cta.html tipo="mini" %}', '', '## Cosa comprende', '']
    L += ['- ' + v for v in sv['voci']]
    L += ['', '## Dove operiamo', '']
    if ct:
        L.append('Interveniamo a %s. Per altre zone consulta le [pulizie a Roma e provincia]({{ \'/servizi/\' | relative_url }}).' % ct['zone'])
    else:
        L.append('Roma e provincia: ' + ', '.join(c['nome'] for c in CITTA) + '. Scegli la tua città dalla pagina [Servizi]({{ \'/servizi/\' | relative_url }}).')
    L.append('')
    scrivi(os.path.join(OUT, slug + '.md'), '\n'.join(L))

for sv in SERVIZI:
    pagina(sv, None)
    for ct in CITTA:
        pagina(sv, ct)

# pagine citta: elenco dei servizi di quella citta
for ct in CITTA:
    t = '\n'.join([
     '---', 'layout: single', 'title: "Pulizie a %s"' % q(ct['nome']),
     'permalink: /servizi/pulizie-%s/' % ct['slug'], 'ref: servizi-%s' % ct['slug'],
     'description: "Pulizie a %s: uffici, condomini, case, negozi e fine lavori. Richiedi un preventivo."' % q(ct['nome']),
     'seo_description: "Ditta di pulizie a %s: uffici, condomini, case, negozi, vetrate e pulizie fine lavori. Richiedi un preventivo."' % q(ct['nome']),
     'author_profile: false', '---', '',
     'Pulizie a **%s**: lavoriamo per %s. Scegli il servizio che ti serve, oppure mandaci su WhatsApp indirizzo e qualche foto.' % (ct['nome'], ct['target']), '',
     '{%- assign lista = site.servizi | where: "citta", "' + ct['nome'] + '" | sort: "title" -%}',
     '{% for s in lista %}',
     '- [{{ s.title }}]({{ s.url | relative_url }}): {{ s.excerpt | strip_html | truncatewords: 22 }}',
     '{% endfor %}', '',
     '[Tutti i servizi]({{ \'/servizi/\' | relative_url }})', ''])
    scrivi(os.path.join(PAGES, 'servizi-pulizie-%s.md' % ct['slug']), t)

# pagina hub /servizi/
hub = '\n'.join([
 '---', 'layout: single', 'title: "Servizi di pulizia a Roma e provincia"', 'permalink: /servizi/', 'ref: servizi', 'author_profile: false',
 'seo_description: "Pulizie uffici, condomini, case, negozi, vetrate, fine lavori e sanificazione a Roma e provincia. Richiedi un preventivo."', '---', '',
 'Ditta di pulizie a **Roma e provincia**: per aziende, condomini e privati. Scegli il servizio, oppure scrivici su WhatsApp con indirizzo e qualche foto.', '',
 '## I servizi', '',
 '{%- assign base = site.servizi | sort: "title" -%}',
 '{% for s in base %}{% unless s.citta %}',
 '- [{{ s.title }}]({{ s.url | relative_url }}): {{ s.excerpt | strip_html | truncatewords: 22 }}',
 '{% endunless %}{% endfor %}', '',
 '## Dove lavoriamo', ''] + ['- [Pulizie a %s]({{ \'/servizi/pulizie-%s/\' | relative_url }})' % (c['nome'], c['slug']) for c in CITTA] + [''])
scrivi(os.path.join(PAGES, 'servizi.md'), hub)
print('servizi:', len(os.listdir(OUT)), 'pagine citta:', len(CITTA))
