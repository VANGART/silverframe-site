#!/usr/bin/env python3
"""Génère les pages du site SilverFrame Agency à partir de outils/donnees.py, pages.py, pages_en.py
et outils/modele-accueil.html : accueil FR et EN, pages services, réalisations, sitemap.xml, robots.txt,
llms.txt, llms-full.txt. Puis vérifie le JSON-LD, les longueurs de titre/description et les liens internes.

Lancer depuis la racine du dépôt :  python3 outils/generer.py
"""
import html, json, os, re, sys
from urllib.parse import quote

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAC, 'outils'))
from donnees import *            # noqa
from pages import SERVICES, CAS  # noqa
from pages_en import SERVICES_EN, ACCUEIL, FAQ  # noqa

E = lambda s: html.escape(s, quote=True)
SV = {s['cle']: s for s in SERVICES}
CASK = {c['cle']: c for c in CAS}
FILM_CAS = {c['film']: c for c in CAS}
ECRITS = []

def typo_fr(h):
    """Typographie française (26/10/2026) : espace insécable avant : ; ? ! » et après «, dans le texte visible
    et les attributs (title, description, alt, aria-label), jamais dans <style> ni <script> (le JSON-LD garde ses espaces)."""
    def fix(t):
        t = re.sub(r' ([:;?!»])', '\u00a0\\1', t)
        return re.sub(r'« ', '«\u00a0', t)
    morceaux = re.split(r'(<(?:style|script)\b.*?</(?:style|script)>)', h, flags=re.S)
    for i in range(0, len(morceaux), 2):
        morceaux[i] = re.sub(r'>([^<]+)<', lambda m: '>' + fix(m.group(1)) + '<', morceaux[i])
        morceaux[i] = re.sub(r'((?:content|alt|aria-label|title|data-titre|data-nom)=")([^"]*)"', lambda m: m.group(1) + fix(m.group(2)) + '"', morceaux[i])
    return ''.join(morceaux)

def ecrire(chemin, contenu):
    if '<html lang="fr"' in contenu: contenu = typo_fr(contenu)
    p = os.path.join(RAC, chemin.lstrip('/'))
    if p.endswith('/'): p += 'index.html'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(contenu)
    ECRITS.append(p)

def nom_client(nom, lang):
    return NOM_EN.get(nom, nom) if lang == 'en' else nom

def titre_film(k, lang, court=False):
    f = FILMS[k]
    if court and k in COURT[lang]: return COURT[lang][k]
    return f[2] if lang == 'fr' else f[3]

def duree_iso(s):
    m, s = divmod(s, 60)
    return f'PT{m}M{s}S' if m else f'PT{s}S'

def duree_txt(k, lang):
    d = FILMS[k][6]; m, s = d.split(':')
    if m == '0': return f'{int(s)} s'
    return f'{int(m)} min {s}' if lang == 'fr' else f'{int(m)} min {s} s'

def picture(k, sizes, alt, lazy=True, cls='', base='films'):
    f = FILMS.get(k)
    w, h = (f[12], f[13]) if f else (1280, 624)
    src = f'/media/{base}/{k}'
    lz = ' loading="lazy"' if lazy else ''
    c = f' class="{cls}"' if cls else ''
    return (f'<picture{c}><source type="image/webp" srcset="{src}-640.webp 640w, {src}.webp {w}w" sizes="{sizes}">'
            f'<img src="{src}.jpg" alt="{E(alt)}" width="{w}" height="{h}"{lz} decoding="async"></picture>')

# ---------------------------------------------------------------- schema.org
ORG_ID = SITE + '/#organisation'
YANN_ID = SITE + '/#yann-volle'
def organisation():
    return {
        '@type': ['Organization', 'ProfessionalService'], '@id': ORG_ID,
        'name': 'SilverFrame Agency', 'alternateName': 'SilverFrame', 'legalName': 'SilverFrame Agency',
        'description': "Production vidéo à Lyon : réalisation, tournage, montage et étalonnage pour les marques, les entreprises et les agences.",
        'url': SITE + '/', 'logo': SITE + '/media/logo-silverframe.png', 'image': SITE + '/media/og.jpg',
        'email': MAIL, 'telephone': TEL, 'vatID': 'FR21107762056',
        'identifier': {'@type': 'PropertyValue', 'propertyID': 'SIREN', 'value': '107762056'},
        'address': {'@type': 'PostalAddress', 'streetAddress': '99 rue de la Part-Dieu', 'postalCode': '69003', 'addressLocality': 'Lyon', 'addressRegion': 'Auvergne-Rhône-Alpes', 'addressCountry': 'FR'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': 45.759944, 'longitude': 4.850957},
        'areaServed': [{'@type': 'City', 'name': 'Lyon'}, {'@type': 'AdministrativeArea', 'name': 'Auvergne-Rhône-Alpes'}, {'@type': 'Country', 'name': 'France'}],
        'founder': {'@id': YANN_ID}, 'employee': [{'@id': YANN_ID}],
        'contactPoint': {'@type': 'ContactPoint', 'contactType': 'customer service', 'email': MAIL, 'telephone': TEL, 'availableLanguage': ['fr']},
        'knowsAbout': ['Réalisation vidéo', 'Film d\'entreprise', 'Captation d\'événement', 'Aftermovie', 'Vidéo de salon professionnel', 'Vidéo pour les réseaux sociaux', 'Film de marque', 'Montage vidéo', 'Étalonnage'],
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Services de production vidéo',
                            'itemListElement': [{'@type': 'Offer', 'itemOffered': {'@id': SITE + s['url'] + '#service'}} for s in SERVICES]},
        'sameAs': ['https://www.instagram.com/silverframe.agency/', 'https://www.linkedin.com/company/silverframe-agency/', 'https://vimeo.com/user90211483'],
    }

def personne():
    return {'@type': 'Person', '@id': YANN_ID, 'name': 'Yann Volle', 'alternateName': 'Yannis Volle',
            'jobTitle': 'Réalisateur, cadreur, monteur, étalonneur', 'image': SITE + '/media/yann.jpg',
            'worksFor': {'@id': ORG_ID}, 'url': SITE + '/#studio',
            'address': {'@type': 'PostalAddress', 'addressLocality': 'Lyon', 'addressCountry': 'FR'},
            'knowsAbout': ['Réalisation', 'Tournage', 'Montage', 'Étalonnage'],
            'sameAs': ['https://vimeo.com/user90211483']}

def video(k, lang, page_url):
    f = FILMS[k]
    return {'@type': 'VideoObject', '@id': f'{SITE}{page_url}#film-{k}',
            'name': f'{nom_client(f[1], lang)} · {titre_film(k, lang)}',
            'description': (f"{titre_film(k, 'fr')}. {f[4]} : Yann Volle, SilverFrame Agency." if lang == 'fr'
                            else f"{titre_film(k, 'en')}. {f[5]}: Yann Volle, SilverFrame Agency."),
            'thumbnailUrl': f'{SITE}/media/films/{k}.jpg', 'embedUrl': f'https://player.vimeo.com/video/{f[0]}',
            'uploadDate': f[14], 'duration': duree_iso(f[15]), 'inLanguage': lang,
            'creator': {'@id': YANN_ID}, 'productionCompany': {'@id': ORG_ID}}

def ariane(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}

def jsonld(noeuds):
    return json.dumps({'@context': 'https://schema.org', '@graph': noeuds}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

# ---------------------------------------------------------------- morceaux communs
def hreflang(fr, en):
    if not en: return f'<link rel="alternate" hreflang="fr" href="{SITE}{fr}">'
    return (f'<link rel="alternate" hreflang="fr" href="{SITE}{fr}">\n<link rel="alternate" hreflang="en" href="{SITE}{en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}{fr}">')

def plan_site(lang):
    """Pied de page sobre (26/10/2026) : une ligne de liens vers les services et les réalisations (maillage interne), puis l'identité."""
    if lang == 'fr':
        liens = [(s['url'], s['nav'], '') for s in SERVICES] + [('/realisations/', 'Réalisations', ''), ('/mentions-legales/', 'Mentions légales', ''), ('/en/', 'English', 'en')]
        nom = 'Plan du site'
    else:
        liens = [(s['url'], s['nav'], '') for s in SERVICES_EN] + [('/en/#services', 'All services', ''), ('/realisations/', 'Case studies (FR)', 'fr'), ('/mentions-legales/', 'Legal notice (FR)', 'fr'), ('/', 'Français', 'fr')]
        nom = 'Site map'
    nav = ''.join(f'<a href="{u}"{(" hreflang=" + chr(34) + h + chr(34) + " lang=" + chr(34) + h + chr(34)) if h else ""}>{E(n)}</a>' for u, n, h in liens)
    return (f'<footer class="pied"><nav aria-label="{nom}">{nav}</nav>'
            f'<span>© 2026 SilverFrame Agency · EURL · SIREN 107 762 056 · 99 rue de la Part-Dieu, 69003 Lyon</span></footer>')

def entete(lang, actif, autre):
    if lang == 'fr':
        liens = [('/#films', 'Films', 'o'), ('/#services', 'Services', ''), ('/realisations/', 'Réalisations', 'o'), ('/agences-marque-blanche/', 'Agences', 'o'), ('#contact', 'Contact', '')]
        lg = f'<a class="langue" href="{autre or "/en/"}" hreflang="en" lang="en" aria-label="English version">EN</a>'
        lab, menu = 'SilverFrame Agency, accueil', 'Menu principal'
        acc = '/'
    else:
        liens = [('/en/#films', 'Films', 'o'), ('/en/#services', 'Services', ''), ('/en/agencies/', 'Agencies', 'o'), ('/en/trade-show-video/', 'Trade shows', 'o'), ('#contact', 'Contact', '')]
        lg = f'<a class="langue" href="{autre or "/"}" hreflang="fr" lang="fr" aria-label="Version française">FR</a>'
        lab, menu = 'SilverFrame Agency, home', 'Main menu'
        acc = '/en/'
    nav = ''.join(f'<a{" class=" + chr(34) + c + chr(34) if c else ""} href="{u}"{" aria-current=" + chr(34) + "page" + chr(34) if u == actif else ""}>{n}</a>' for u, n, c in liens)
    return (f'<a class="saut" href="#contenu">{"Aller au contenu" if lang == "fr" else "Skip to content"}</a>'
            f'<header class="haut"><div class="in"><a class="wm" href="{acc}" aria-label="{lab}"><img src="/media/logo-silverframe-blanc.png" alt="" width="108" height="200"><span>SILVERFRAME</span></a>'
            f'<nav aria-label="{menu}">{nav}{lg}</nav></div></header>')

def fil(items, lang):
    lis = ''.join((f'<li><a href="{u}">{E(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{E(n)}</li>') for i, (n, u) in enumerate(items))
    return f'<nav class="ariane" aria-label="{"Fil d’Ariane" if lang == "fr" else "Breadcrumb"}"><ol>{lis}</ol></nav>'

def bloc_contact(lang, sujet):
    sub = quote(sujet)
    if lang == 'fr':
        return (f'<section class="contact" id="contact"><p class="mono">Un brief, une date, une idée</p>'
                f'<a class="mail" href="mailto:{MAIL}?subject={sub}">Écrire à Yann ↗</a>'
                '<p class="devis">Sur devis. Envoyez le brief, même incomplet : Yann revient avec une approche et un chiffrage.</p>'
                f'<div class="coord"><div><span class="mono">Mail</span><a href="mailto:{MAIL}?subject={sub}">{MAIL}</a></div><div><span class="mono">Téléphone</span><a href="tel:{TEL}">06 77 52 10 36</a></div>'
                '<div><span class="mono">Studio</span>99 rue de la Part-Dieu<br>69003 Lyon</div><div><span class="mono">Ailleurs</span><a href="https://vimeo.com/user90211483" rel="noopener" target="_blank">Vimeo</a> · <a href="https://www.instagram.com/silverframe.agency/" rel="noopener" target="_blank">Instagram</a></div></div></section>')
    return (f'<section class="contact" id="contact"><p class="mono">A brief, a date, an idea</p>'
            f'<a class="mail" href="mailto:{MAIL}?subject={sub}">Email Yann ↗</a>'
            '<p class="devis">Quote on request. Send the brief, even a rough one, and Yann will come back to you with an approach and a quote.</p>'
            f'<div class="coord"><div><span class="mono">Email</span><a href="mailto:{MAIL}?subject={sub}">{MAIL}</a></div><div><span class="mono">Phone</span><a href="tel:{TEL}">+33 6 77 52 10 36</a></div>'
            '<div><span class="mono">Studio</span>99 rue de la Part-Dieu<br>69003 Lyon, France</div><div><span class="mono">Elsewhere</span><a href="https://vimeo.com/user90211483" rel="noopener" target="_blank">Vimeo</a> · <a href="https://www.instagram.com/silverframe.agency/" rel="noopener" target="_blank">Instagram</a></div></div></section>')

SVG_PLAY = '<svg viewBox="0 0 12 14" aria-hidden="true"><path d="M0 0l12 7-12 7z"/></svg>'
def figure_film(k, lang, lien_cas=True, legende=True):
    f = FILMS[k]
    nom = nom_client(f[1], lang); ti = titre_film(k, lang)
    gen = f[4] if lang == 'fr' else f[5]
    sep = ' : ' if lang == 'fr' else ': '
    lire = 'LIRE' if lang == 'fr' else 'PLAY'
    aria = (f'Lire le film {nom}, {ti} ({duree_txt(k, lang)})' if lang == 'fr' else f'Play the film {nom}, {ti} ({duree_txt(k, lang)})')
    lien = ''
    if lien_cas and k in FILM_CAS:
        c = FILM_CAS[k]
        lien = (f'<a href="{c["url"]}">L\'histoire du film →</a>' if lang == 'fr' else f'<a href="{c["url"]}" hreflang="fr">The story of the film (FR) →</a>')
    sizes = '(max-width: 820px) 100vw, 270px' if f[7] else '(max-width: 820px) 100vw, 45vw'
    return (f'<figure class="film{" v" if f[7] else ""}"><div class="cadre"><button type="button" class="lance" data-vimeo="{f[0]}" data-titre="{E(nom + " · " + ti)}" aria-label="{E(aria)}">'
            f'{picture(k, sizes, "")}<span class="jouer"><i>{SVG_PLAY}</i>{lire} · {f[6]}</span></button></div>'
            + (f'<figcaption><b>{E(nom)}</b><span>{E(ti)}</span><span class="mono">{E(gen)}{sep}Yann Volle · {f[8]}</span>{lien}</figcaption>' if legende else '') + '</figure>')

def page(lang, url, titre, desc, corps, noeuds, fr=None, en=None, og='website', image=None, actif=None):
    alt = hreflang(fr or url, en) if (fr or en) else f'<link rel="alternate" hreflang="{lang}" href="{SITE}{url}">'
    if lang == 'en' and fr: alt = hreflang(fr, url)
    img = image or SITE + '/media/og.jpg'
    autre = (en if lang == 'fr' else fr)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(titre)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{url}">
{alt}
<link rel="icon" href="/media/icone.png"><link rel="apple-touch-icon" href="/media/icone.png">
<meta property="og:type" content="{og}"><meta property="og:site_name" content="SilverFrame Agency"><meta property="og:locale" content="{"fr_FR" if lang == "fr" else "en_GB"}">
<meta property="og:title" content="{E(titre)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{SITE}{url}">
<meta property="og:image" content="{img}"><meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/media/polices/syne-700-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/media/pages.css?v=4">
<script type="application/ld+json">{jsonld(noeuds)}</script>
</head>
<body>
{entete(lang, actif or url, autre)}
<main id="contenu">
{corps}
</main>
{plan_site(lang)}
<script src="/media/pages.js?v=2" defer></script>
</body>
</html>
'''

def liste_liens(titre, items, lang):
    rangs = ''.join(f'<a class="rang" href="{u}"{h}><b>{E(n)}</b><i aria-hidden="true">→</i></a>' for u, n, d, h in items)
    return f'<section class="liste"><div class="t"><h2>{E(titre)}</h2></div>{rangs}</section>'

def blocs_html(blocs):
    return ''.join(f'<section class="bloc"><h2>{E(h2)}</h2>{html_}</section>' for h2, html_ in blocs)

# ---------------------------------------------------------------- pages services
def page_service(s, lang):
    url = s['url']
    fr_url = url if lang == 'fr' else s['fr']
    en_url = s.get('en') if lang == 'fr' else url
    acc = '/' if lang == 'fr' else '/en/'
    items = [('Accueil' if lang == 'fr' else 'Home', acc), (s['h1'], url)]
    livr = ' · '.join(E(l) for l in s['livrables'])
    corps = (fil(items, lang) +
             f'<div class="tete"><h1>{E(s["h1"])}</h1><p class="intro">{s["intro"]}</p><p class="livr mono">{"Livrables" if lang == "fr" else "Deliverables"} · {livr}</p></div>' +
             f'<section class="films" aria-label="Films">' + ''.join(figure_film(k, lang, lien_cas=(lang == 'en')) for k in s['films']) + '</section>' +
             blocs_html(s['blocs']))
    if lang == 'fr':
        lies = [(SV[k]['url'], SV[k]['nav'], SV[k]['court'], '') for k in s['lies']]
        cas = [(CASK[k]['url'], FILMS[CASK[k]['film']][1], CASK[k]['resume'], '') for k in s.get('cas', []) if k in CASK]
        if cas: corps += liste_liens('Réalisations', cas, lang)
        corps += liste_liens('Autres services', lies, lang)
    else:
        autres = [(x['url'], x['nav'], '', '') for x in SERVICES_EN if x['url'] != url] + [('/en/#services', 'All services', 'Corporate, events, social media, brand films, editing and grading', '')]
        corps += liste_liens('Other services', autres, lang)
    corps += bloc_contact(lang, s['sujet'])
    noeuds = [{'@type': 'WebPage', '@id': SITE + url, 'url': SITE + url, 'name': s['titre'], 'description': s['desc'], 'inLanguage': lang,
               'isPartOf': {'@id': SITE + '/#site'}, 'about': {'@id': SITE + url + '#service'}, 'breadcrumb': {'@id': SITE + url + '#ariane'}},
              {'@type': 'Service', '@id': SITE + url + '#service', 'name': s['service'], 'serviceType': s['type'], 'description': s['desc'], 'url': SITE + url,
               'provider': {'@id': ORG_ID}, 'areaServed': [{'@type': 'City', 'name': 'Lyon'}, {'@type': 'AdministrativeArea', 'name': 'Auvergne-Rhône-Alpes'}, {'@type': 'Country', 'name': 'France'}],
               'subjectOf': [{'@id': f'{SITE}{url}#film-{k}'} for k in s['films']]},
              dict(ariane(items), **{'@id': SITE + url + '#ariane'}),
              organisation(), personne()] + [video(k, lang, url) for k in s['films']]
    return page(lang, url, s['titre'], s['desc'], corps, noeuds, fr=fr_url, en=en_url)

# ---------------------------------------------------------------- réalisations
def page_cas(c):
    k = c['film']; f = FILMS[k]; url = c['url']
    items = [('Accueil', '/'), ('Réalisations', '/realisations/'), (f[1], url)]
    gen = f[4]
    dl = (f'<dl><dt>Client</dt><dd>{E(f[1])}</dd><dt>Film</dt><dd>{E(f[2])}</dd><dt>Ce que Yann a fait</dt><dd>{E(gen)}</dd>'
          f'<dt>Durée</dt><dd>{duree_txt(k, "fr")}</dd><dt>Format</dt><dd>{"Vertical 9:16" if f[7] else "Horizontal 16:9"}</dd><dt>Année</dt><dd>{f[8]}</dd>'
          f'<dt>Sur Vimeo</dt><dd><a class="lien" href="https://vimeo.com/{f[0]}" rel="noopener" target="_blank">vimeo.com/{f[0]}</a></dd></dl>')
    if c.get('ancien'):
        texte = ANCIEN_CA
    else:
        texte = (f'<section class="bloc"><h2>Le projet</h2>{c["contexte"]}<h3>Ce qui le rendait difficile</h3>{c["defi"]}'
                 f'<h3>Comment Yann l\'a filmé</h3>{c["approche"]}</section>')
    corps = (fil(items, 'fr') +
             f'<div class="tete"><h1>{E(c["h1"])}</h1><p class="intro">{E(c["resume"])}.</p></div>' +
             f'<section class="films" aria-label="Le film">{figure_film(k, "fr", lien_cas=False, legende=False)}</section>' + texte +
             f'<section class="bloc"><h2>Le film en bref</h2>{dl}</section>' +
             liste_liens('Services liés', [(SV[x]['url'], SV[x]['nav'], '', '') for x in c['services']], 'fr') +
             liste_liens('Autres réalisations', [(o['url'], FILMS[o['film']][1], '', '') for o in CAS if o['cle'] != c['cle']], 'fr') +
             bloc_contact('fr', 'Projet · ' + f[1]))
    noeuds = [{'@type': 'Article', '@id': SITE + url + '#article', 'headline': c['h1'][:110], 'description': c['desc'], 'url': SITE + url, 'mainEntityOfPage': SITE + url,
               'inLanguage': 'fr', 'datePublished': c['date'], 'dateModified': MAJ, 'image': [f'{SITE}/media/films/{k}.jpg'],
               'author': {'@id': YANN_ID}, 'publisher': {'@id': ORG_ID}, 'about': {'@id': f'{SITE}{url}#film-{k}'}},
              dict(ariane(items), **{'@id': SITE + url + '#ariane'}), organisation(), personne(), video(k, 'fr', url)]
    return page('fr', url, c['titre'], c['desc'], corps, noeuds, og='article', image=f'{SITE}/media/films/{k}.jpg')

ANCIEN_CA = ('<section class="bloc"><h2>Trois mondes dans un film</h2>'
 '<p>Pour lancer sa carte Mozaïc, le Crédit Agricole voulait un film qui tienne trois choses à la fois&nbsp;: le design de l\'artiste Lorem, l\'énergie de l\'Équipe de France de football et le sérieux d\'une grande banque. Sur le papier, ces trois mondes n\'ont pas grand-chose à se dire. C\'est ce qui nous a plu.</p>'
 '<h3>Le vrai problème était éditorial</h3>'
 '<p>Laisser de la place au geste de Lorem sans faire une vitrine graphique, montrer le terrain sans cliché sportif, et garder la rigueur qu\'une banque attend.</p>'
 '<h3>Comment on l\'a fait</h3>'
 '<p>On a filmé le design de Lorem en train de se faire, en réponse à l\'énergie du match. La marque tient l\'ensemble sans prendre toute la place. Cadrage, rythme, musique, étalonnage&nbsp;: tout s\'est réglé plan par plan, pour le film entier et jamais pour un seul des trois univers.</p>'
 '<p>Le film parle aux fans de foot comme aux clients de la banque, et garde la signature visuelle de Lorem. Vous avez un film avec plusieurs marques ou partenaires à faire travailler ensemble&nbsp;?</p></section>')

def page_realisations():
    url = '/realisations/'
    items = [('Accueil', '/'), ('Réalisations', url)]
    cartes = ''.join(f'<a href="{c["url"]}">{picture(c["film"], "(max-width: 820px) 100vw, 33vw", "")}<b>{E(FILMS[c["film"]][1])}</b><span>{E(FILMS[c["film"]][2])}</span><span class="mono">{E(FILMS[c["film"]][4])} · {FILMS[c["film"]][6]} · {FILMS[c["film"]][8]}</span></a>' for c in CAS)
    corps = (fil(items, 'fr') +
             '<div class="tete"><h1>Réalisations : six films racontés</h1>'
             '<p class="intro">Le contexte, la difficulté, le tournage et ce qui a été livré. <em>Les quinze films sont sur l\'accueil.</em></p></div>'
             f'<section class="cas" aria-label="Études de cas">{cartes}</section>' +
             liste_liens('Services', [(s['url'], s['nav'], '', '') for s in SERVICES], 'fr') +
             bloc_contact('fr', 'Projet'))
    desc = "Six films de SilverFrame Agency racontés en détail : Crédit Agricole × FFF, Don Papa Rum, Keyena × Artik, The Ink Factory, VJM, Ozur. Contexte, défi, livrables."
    noeuds = [{'@type': 'CollectionPage', '@id': SITE + url, 'url': SITE + url, 'name': 'Réalisations · SilverFrame Agency, production vidéo à Lyon', 'description': desc, 'inLanguage': 'fr',
               'isPartOf': {'@id': SITE + '/#site'}, 'breadcrumb': {'@id': SITE + url + '#ariane'},
               'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + c['url'], 'name': c['h1']} for i, c in enumerate(CAS)]}},
              dict(ariane(items), **{'@id': SITE + url + '#ariane'}), organisation(), personne()]
    return page('fr', url, 'Réalisations · études de cas vidéo | SilverFrame Lyon', desc, corps, noeuds, actif='/realisations/')

# ---------------------------------------------------------------- accueil FR / EN
def accueil(lang):
    T = dict(ACCUEIL[lang])
    modele = open(os.path.join(RAC, 'outils', 'modele-accueil.html'), encoding='utf-8').read()
    def attr(k):
        f = FILMS[k]; nom = nom_client(f[1], lang); ti = titre_film(k, lang, court=True)
        return f'data-film data-v="{f[7]}" data-vimeo="{f[0]}" data-nom="{E(nom + " · " + ti)}"'
    lire = 'Lire le film' if lang == 'fr' else 'Play the film'
    # le film à la une (Crédit Agricole × Équipe de France × Lorem)
    k = UNE; f = FILMS[k]; c = FILM_CAS.get(k)
    coulisses = (f'<a class="lien" href="{c["url"]}">{"Les coulisses →" if lang == "fr" else "Behind the scenes (in French) →"}</a>' if c else '')
    T['UNE'] = (f'<div class="une"><button class="affiche" type="button" {attr(k)} aria-label="{E(lire + " " + T["une_client"])}">'
                f'{picture(k, "(max-width: 820px) 300px, 340px", "")}</button>'
                f'<div><p class="cl">{E(T["une_client"])}</p><p class="ti">{E(titre_film(k, lang))}</p>'
                f'<p class="mono">{E(f[4] if lang == "fr" else f[5])} · {duree_txt(k, lang)} · {f[8]}</p>'
                f'<div class="actions"><button class="jouer" type="button" {attr(k)}><i aria-hidden="true">{SVG_PLAY}</i>{lire.upper()}</button>{coulisses}</div></div></div>')
    T['GRILLE'] = ''.join(
        f'<li><button class="vign" type="button" {attr(k)} aria-label="{E(lire + " " + nom_client(FILMS[k][1], lang) + ", " + titre_film(k, lang, True))}">'
        f'{picture(k, "(max-width: 820px) 50vw, 25vw", "")}<b>{E(nom_client(FILMS[k][1], lang))}</b><span>{E(titre_film(k, lang, True))} · {FILMS[k][8]}</span></button></li>'
        for k in ORDRE if k != UNE)
    if lang == 'fr':
        T['SERVICES'] = ''.join(f'<a class="rang" href="{s["url"]}"><b>{E(s["nav"])}</b><span>{E(s["court"])}</span><i aria-hidden="true">→</i></a>' for s in SERVICES)
    else:
        en_serv = [('/en/agencies/', 'For agencies', 'White-label production, under your name', ''), ('/en/trade-show-video/', 'Trade shows', 'Stand film, vertical formats, aftermovie', ''),
                   (SV['entreprise']['url'], 'Corporate films', 'Portraits, craft, workshops (page in French)', 'fr'), (SV['evenement']['url'], 'Events and aftermovies', 'Coverage, aftermovie, social formats (page in French)', 'fr'),
                   (SV['reseaux']['url'], 'Social media', '9:16, 1:1 and 16:9 formats (page in French)', 'fr'), (SV['marque']['url'], 'Brand films and ads', 'Product, craft, brand image (page in French)', 'fr'),
                   (SV['montage']['url'], 'Editing and colour grading', 'Editing, grading, music videos (page in French)', 'fr')]
        T['SERVICES'] = ''.join(f'<a class="rang" href="{u}"{" hreflang=" + chr(34) + h + chr(34) if h else ""}><b>{E(n)}</b><span>{E(d)}</span><i aria-hidden="true">→</i></a>' for u, n, d, h in en_serv)
    T['LOGOS'] = ''.join(f'<li{" class=" + chr(34) + "fort" + chr(34) if i < 5 else ""}><picture><source type="image/webp" srcset="/media/logos/{l}.webp"><img src="/media/logos/{l}.png" alt="{E(nom_client(n, lang))}" width="{w}" height="{h}" decoding="async"></picture></li>' for i, (l, n, w, h) in enumerate(LOGOS))
    # deux témoignages visibles (les autres restent dans llms-full.txt)
    T['PAROLES'] = ''.join(f'<figure><blockquote class="citation">{"« " + E(q) + " »" if lang == "fr" else "“" + E(q) + "”"}</blockquote><figcaption class="auteur">{E(a)}</figcaption></figure>' for q, a in [PAROLES[lang][i] for i in PAROLES_ACCUEIL])
    T['SVG_PLAY'] = SVG_PLAY
    T['PLAN'] = plan_site(lang)
    if lang == 'fr':
        T['nav'] = '<a class="o" href="#films">Films</a><a href="#services">Services</a><a class="o" href="/agences-marque-blanche/">Agences</a><a class="o" href="#studio">Studio</a><a href="#contact">Contact</a><a href="/en/" hreflang="en" lang="en" aria-label="English version">EN</a>'
    else:
        T['nav'] = '<a class="o" href="#films">Films</a><a href="#services">Services</a><a class="o" href="/en/agencies/">Agencies</a><a class="o" href="#studio">Studio</a><a href="#contact">Contact</a><a href="/" hreflang="fr" lang="fr" aria-label="Version française">FR</a>'
    T['hreflang'] = hreflang('/', '/en/')
    url = '/' if lang == 'fr' else '/en/'
    T['jsonld'] = jsonld([
        {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'SilverFrame Agency', 'alternateName': 'SilverFrame', 'inLanguage': ['fr', 'en'], 'publisher': {'@id': ORG_ID}},
        {'@type': 'WebPage', '@id': SITE + url, 'url': SITE + url, 'name': T['title'], 'description': T['desc'], 'inLanguage': lang, 'isPartOf': {'@id': SITE + '/#site'}, 'about': {'@id': ORG_ID}, 'primaryImageOfPage': SITE + '/media/og.jpg'},
        organisation(), personne(),
        {'@type': 'VideoObject', '@id': SITE + url + '#film-silverframe', 'name': 'SilverFrame · le film' if lang == 'fr' else 'SilverFrame · the film',
         'description': ("Le film d'une minute de SilverFrame Agency : extraits des films de Yann Volle." if lang == 'fr' else 'The one-minute SilverFrame Agency reel: excerpts from Yann Volle\'s films.'),
         'thumbnailUrl': SITE + '/media/boucle.jpg', 'contentUrl': SITE + '/media/' + T['film_fichier'] + '.mp4', 'duration': 'PT1M', 'inLanguage': lang, 'productionCompany': {'@id': ORG_ID}},
    ] + [video(k, lang, url) for k in ORDRE])
    out = modele
    for k, v in T.items():
        out = out.replace('{{' + k + '}}', v)
    reste = re.findall(r'\{\{\w+\}\}', out)
    assert not reste, reste
    return out

# ---------------------------------------------------------------- fichiers pour les robots
def toutes_les_pages():
    p = [('/', '/en/'), ('/en/', '/')]
    for s in SERVICES: p.append((s['url'], s.get('en')))
    for s in SERVICES_EN: p.append((s['url'], s['fr']))
    p.append(('/realisations/', None))
    for c in CAS: p.append((c['url'], None))
    p.append(('/mentions-legales/', None))
    return p

def sitemap():
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u, autre in toutes_les_pages():
        alt = ''
        if autre:
            fr, en = (u, autre) if not u.startswith('/en/') else (autre, u)
            alt = (f'<xhtml:link rel="alternate" hreflang="fr" href="{SITE}{fr}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>'
                   f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{fr}"/>')
        lignes.append(f'<url><loc>{SITE}{u}</loc><lastmod>{MAJ}</lastmod>{alt}</url>')
    lignes.append('</urlset>')
    return '\n'.join(lignes) + '\n'

ROBOTS = """# SilverFrame Agency : les moteurs de recherche et les assistants IA sont les bienvenus (le but est d'être trouvé et cité).
User-agent: *
Allow: /
Disallow: /outils/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

User-agent: MistralAI-User
Allow: /

User-agent: DuckAssistBot
Allow: /

Sitemap: https://www.silverframeagency.com/sitemap.xml
"""

def texte_brut(h):
    h = re.sub(r'<li>', '- ', h); h = re.sub(r'</(p|li|figure|blockquote)>', '\n', h)
    h = re.sub(r'<[^>]+>', '', h)
    return html.unescape(re.sub(r'\n{2,}', '\n', h)).strip()

def llms():
    L = ['# SilverFrame Agency', '',
         '> Production vidéo à Lyon (France). Yann Volle, réalisateur depuis 2016, réalise, tourne, monte et étalonne des films pour les marques, les entreprises et les agences : films d\'entreprise, captation d\'événement et aftermovies, vidéos de salon professionnel, formats verticaux pour les réseaux sociaux, films de marque et publicité, montage et étalonnage. Tarifs : sur devis.', '',
         '- Société : SilverFrame Agency, EURL, SIREN 107 762 056, 99 rue de la Part-Dieu, 69003 Lyon, France',
         f'- Contact : {MAIL}, +33 6 77 52 10 36',
         '- Zone : Lyon, Auvergne-Rhône-Alpes, toute la France et l\'étranger',
         '- Équipe : Yann Volle (réalisation, tournage, montage, étalonnage) ; Auriane (photographe, formée à l\'école Émile Cohl, photos de plateau)',
         '- Clients : Crédit Agricole, Équipe de France de football (avec l\'artiste Lorem et le Crédit Agricole), Deutsche Welle, Wella, Don Papa Rum, M. Chapoutier, Aluna Festival, The Ink Factory, Kosmos, MJH Life Sciences, Monfairepart, VANGART',
         '- Agences qui travaillent avec lui : M&R Digital Agency, Coming Soon Agency (production en marque blanche possible)',
         '- Langues du site : français, anglais (/en/)', '', '## Services', '']
    for s in SERVICES: L.append(f'- [{s["h1"]}]({SITE}{s["url"]}) : {s["desc"]}')
    L += ['', '## English', '']
    L += [f'- [Home]({SITE}/en/) : video production in Lyon, France']
    for s in SERVICES_EN: L.append(f'- [{s["h1"]}]({SITE}{s["url"]}) : {s["desc"]}')
    L += ['', '## Réalisations (études de cas)', '', f'- [Toutes les réalisations]({SITE}/realisations/)']
    for c in CAS: L.append(f'- [{c["h1"]}]({SITE}{c["url"]}) : {c["desc"]}')
    L += ['', '## Films', '']
    for k in ORDRE:
        f = FILMS[k]; L.append(f'- {f[1]} · {f[2]} ({f[8]}, {f[6]}) : {f[4]}. https://vimeo.com/{f[0]}')
    L += ['', '## Optional', '', f'- [Texte complet du site]({SITE}/llms-full.txt)', f'- [Mentions légales]({SITE}/mentions-legales/)', '']
    full = ['# SilverFrame Agency · texte complet du site', '', L[2], '']
    for s in SERVICES:
        full += [f'## {s["h1"]}', f'URL : {SITE}{s["url"]}', '', texte_brut(s['intro']), '']
        for h2, h in s['blocs']: full += [f'### {h2}', texte_brut(h), '']
        full += ['Livrables : ' + ', '.join(s['livrables']), '']
    for c in CAS:
        if c.get('ancien'): full += [f'## {c["h1"]}', f'URL : {SITE}{c["url"]}', texte_brut(ANCIEN_CA), '']
        else: full += [f'## {c["h1"]}', f'URL : {SITE}{c["url"]}', texte_brut(c['contexte']), texte_brut(c['defi']), texte_brut(c['approche']), '']
    full += ['## Questions fréquentes', ''] + [f'### {q}\n{r}\n' for q, r in FAQ['fr']]
    full += ['## Témoignages', ''] + [f'- « {q} » ({a})' for q, a in PAROLES['fr']] + ['']
    return '\n'.join(L), '\n'.join(full)

# ---------------------------------------------------------------- génération + contrôles
def main():
    ecrire('/', accueil('fr'))
    ecrire('/en/', accueil('en'))
    for s in SERVICES: ecrire(s['url'], page_service(s, 'fr'))
    for s in SERVICES_EN: ecrire(s['url'], page_service(s, 'en'))
    for c in CAS: ecrire(c['url'], page_cas(c))
    # mentions légales (page écrite à la main) : seul le pied de page est remis à jour par le générateur
    ml = os.path.join(RAC, 'mentions-legales/index.html'); h = open(ml, encoding='utf-8').read()
    open(ml, 'w', encoding='utf-8').write(typo_fr(re.sub(r'<footer.*?</footer>', lambda m: plan_site('fr'), h, count=1, flags=re.S).replace('/media/pages.css?v=3', '/media/pages.css?v=4')))
    ecrire('/realisations/', page_realisations())
    open(os.path.join(RAC, 'sitemap.xml'), 'w').write(sitemap())
    open(os.path.join(RAC, 'robots.txt'), 'w').write(ROBOTS)
    a, b = llms()
    open(os.path.join(RAC, 'llms.txt'), 'w').write(a)
    open(os.path.join(RAC, 'llms-full.txt'), 'w').write(b)
    controler()

def controler():
    erreurs = []
    pages = [p for p in ECRITS] + [os.path.join(RAC, 'mentions-legales/index.html')]
    titres, descs = {}, {}
    for p in pages:
        h = open(p, encoding='utf-8').read(); r = os.path.relpath(p, RAC)
        for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try: json.loads(bloc)
            except Exception as e: erreurs.append(f'{r} : JSON-LD invalide ({e})')
        t = html.unescape(re.search(r'<title>(.*?)</title>', h).group(1)); d = html.unescape(re.search(r'<meta name="description" content="(.*?)">', h).group(1))
        titres.setdefault(t, []).append(r); descs.setdefault(d, []).append(r)
        print(f'{r:62} titre {len(t):3}  desc {len(d):3}  h1 {len(re.findall("<h1", h))}')
        if not (45 <= len(t) <= 62): erreurs.append(f'{r} : titre {len(t)} car.')
        if not (130 <= len(d) <= 165): erreurs.append(f'{r} : description {len(d)} car.')
        for u in [x for x in re.findall(r'(?:href|src)="(/[^"#?]*)', h) if '$' not in x]:
            cible = os.path.join(RAC, u.lstrip('/'))
            if u.endswith('/'): cible = os.path.join(cible, 'index.html')
            if not os.path.exists(cible): erreurs.append(f'{r} : lien cassé {u}')
        for u in re.findall(r'srcset="([^"]+)"', h):
            for part in u.split(','):
                s = part.strip().split(' ')[0]
                if s.startswith('/') and not os.path.exists(os.path.join(RAC, s.lstrip('/'))): erreurs.append(f'{r} : image manquante {s}')
    for t, ps in titres.items():
        if len(ps) > 1: erreurs.append(f'titre en double : {t} {ps}')
    for d, ps in descs.items():
        if len(ps) > 1: erreurs.append(f'description en double : {ps}')
    print('\n'.join(erreurs) or 'Contrôles : tout est bon.')
    return not erreurs

if __name__ == '__main__':
    main()
