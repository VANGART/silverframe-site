# Textes des pages intérieures (services, réalisations, version anglaise).
# Règles : aucun prix (« sur devis »), aucun délai promis, aucun fait qui ne soit pas dans les sources citées
# en tête de donnees.py ou dans une source publique donnée en lien sur la page.

# Services ------------------------------------------------------------------------------------------
# clé : dict(url, nav, titre (balise title), desc (meta), h1, intro (HTML), films, blocs [(lab, h2, html)],
#            sujet (objet du mail), service (nom pour schema.org), type (serviceType), lies, cas)
SERVICES = [
 dict(cle='entreprise', url='/film-entreprise-lyon/', nav="Film d'entreprise", court="Portraits, savoir-faire, ateliers, campagnes",
  titre="Film d'entreprise à Lyon · vidéo corporate | SilverFrame",
  desc="Film d'entreprise et vidéo corporate à Lyon : portraits, savoir-faire, ateliers, campagnes. Yann Volle réalise, tourne, monte et étalonne. Sur devis.",
  h1="Film d'entreprise à Lyon",
  intro="Une agricultrice qui raconte son métier. Un sertissage filmé à quelques millimètres. Un atelier de faire-part en pleine fabrication. <em>Nos films d'entreprise partent de ce que les gens font, sur place.</em>",
  postes=['Portrait', 'Savoir-faire', 'Atelier', 'Campagne', 'Film institutionnel'],
  films=['ca-candice', 'vjm', 'monfairepart'],
  blocs=[
   ('Ce qu\'on filme', "Des gens au travail, plutôt qu'une plaquette lue à voix haute",
    "<p>Un film d'entreprise sert à montrer un métier, une équipe ou une façon de faire à des gens qui ne viendront jamais dans vos locaux : des clients, des candidats, des partenaires. On filme sur place, avec les personnes concernées, et on garde leurs mots.</p>"
    "<p>Le même tournage donne souvent plusieurs films : une version longue pour le site ou une réunion, des extraits verticaux pour LinkedIn ou Instagram, des photos de plateau par Auriane.</p>"),
   ('Une référence', 'Deux films pour le Crédit Agricole',
    "<p>Pour le Crédit Agricole, Yann a réalisé le portrait de Candice Chlovy, agricultrice en Auvergne-Rhône-Alpes (réalisation, tournage, étalonnage, 3 min 33), et le film de la campagne régionale « Agissons au cœur de nos territoires » (réalisation, montage, étalonnage, 3 min 29).</p>"
    "<p>Pour VJM, il a filmé le sertissage en macro, à l'échelle de la pierre : <a class=\"lien\" href=\"/realisations/vjm-sertissage-macro/\">l'histoire de ce film</a>.</p>"),
   ('Comment ça se passe', 'Une seule personne du repérage à l\'étalonnage',
    "<p>On commence par un échange sur ce que le film doit faire, et pour qui. Ensuite Yann repère, tourne, monte et étalonne : rien ne se perd entre le plateau et la post-production.</p>"
    "<p>Pour un portrait ou un atelier, il tourne seul avec son matériel, ce qui dérange peu une équipe au travail. Pour un film plus lourd, il vient avec une équipe image, son et lumière.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Chaque film est chiffré sur devis, après un échange sur le brief : durée du tournage, taille de l'équipe, nombre de versions à livrer. Écrivez à Yann avec ce que vous avez, même incomplet.</p>"),
  ],
  livrables=['Film long 16:9', 'Extraits 9:16 et 1:1', 'Sous-titres', 'Photo de plateau', 'Master 4K'],
  sujet="Film d'entreprise", service="Film d'entreprise et vidéo corporate", type='Production de film d\'entreprise',
  lies=['salon', 'montage', 'marque'], cas=['vjm']),

 dict(cle='evenement', url='/captation-evenement-lyon/', nav='Événement et aftermovie', court='Captation, aftermovie, formats pour les réseaux',
  titre="Captation d'événement et aftermovie à Lyon | SilverFrame",
  desc="Captation d'événement et aftermovie à Lyon : conventions, soirées, lancements, bars éphémères. Film long et formats verticaux pour les réseaux. Sur devis.",
  h1="Captation d'événement et aftermovie à Lyon",
  intro="La convention internationale de tatouage de Lyon. Un bar éphémère en station de ski. <em>Un événement ne se rejoue pas : on le filme pendant qu'il a lieu, pour ceux qui y étaient et pour ceux qui viendront l'an prochain.</em>",
  postes=['Captation', 'Aftermovie', 'Teaser', 'Formats verticaux', 'Photo'],
  films=['ink-factory', 'don-papa', 'ca-fff'],
  blocs=[
   ('Aftermovie', "Le film qu'on montre l'année suivante",
    "<p>L'aftermovie raconte l'événement après coup. Il sert aux participants, aux partenaires qui ont payé un stand ou une visibilité, et à la vente de l'édition suivante.</p>"
    "<p>Pour The Ink Factory, la convention internationale de tatouage de Lyon, Yann a fait la captation, le montage et l'étalonnage d'un aftermovie de 2 min 34. <a class=\"lien\" href=\"/realisations/the-ink-factory-aftermovie/\">Voir comment ce film a été fait</a>.</p>"),
   ('Sur place', 'Des formats verticaux pour raconter en direct',
    "<p>Pour Don Papa Rum, à Winterlandia, un bar éphémère en station de ski, Yann a filmé et monté un format vertical de 45 secondes : <a class=\"lien\" href=\"/realisations/don-papa-winterlandia/\">l'histoire du film</a>.</p>"
    "<p>Sur un événement, on peut préparer en parallèle le film long et des formats courts en 9:16. Le délai de livraison se fixe au devis, selon que vous voulez publier pendant l'événement ou après.</p>"),
   ('À préparer', 'Ce qui nous aide avant le jour J',
    "<ul class=\"points\"><li><b>Le programme heure par heure.</b> Discours, concert, remise de prix : les moments qu'on ne doit pas manquer.</li>"
    "<li><b>Un repérage si possible.</b> La lumière d'une halle ou d'un chalet ne se devine pas sur un plan.</li>"
    "<li><b>Les autorisations.</b> Droit de filmer le lieu, le public, les artistes.</li>"
    "<li><b>Les formats attendus.</b> Film long, versions courtes, photos : tout se tourne en même temps.</li></ul>"),
   ('Tarif', 'Sur devis',
    "<p>La captation d'un événement est chiffrée sur devis, selon sa durée, le nombre de personnes à filmer et les formats à livrer.</p>"),
  ],
  livrables=['Aftermovie 16:9', 'Teasers 9:16', 'Formats 1:1', 'Sous-titres', 'Photo'],
  sujet="Captation d'événement", service="Captation d'événement et aftermovie", type="Captation vidéo d'événement",
  lies=['salon', 'reseaux', 'agences'], cas=['ink-factory', 'don-papa']),

 dict(cle='salon', url='/video-salon-professionnel-lyon/', nav='Salons professionnels', court='Film de stand, formats verticaux, film du salon',
  titre='Vidéo de salon professionnel à Lyon · film de stand',
  desc="Vidéo de salon professionnel à Lyon (Sirha, salons d'Eurexpo, Global Industrie) : film de stand en boucle, formats verticaux pendant le salon, aftermovie.",
  h1='Vidéo de salon professionnel à Lyon',
  intro="Sirha, un salon à Eurexpo, Global Industrie à Lyon ou à Paris : quelques jours pour se montrer, des mois de préparation derrière. <em>On filme ce que votre stand doit montrer, et ce qui s'y passe.</em>",
  postes=['Film de stand', 'Formats verticaux', 'Interviews', 'Aftermovie', 'Photo'],
  films=['vjm', 'don-papa', 'ink-factory'],
  blocs=[
   ('Avant le salon', 'Le film de stand, qui tourne en boucle sur l\'écran',
    "<p>Un film court, tourné chez vous avant le salon : vos produits, vos gestes, votre atelier. Il passe en boucle sur l'écran du stand, souvent sans le son, parce qu'une allée de salon est bruyante. On le monte pour qu'il se comprenne muet, avec des sous-titres si quelqu'un parle.</p>"
    "<p>Le sertissage filmé en macro pour VJM dure 24 secondes : c'est le genre d'image qui fait ralentir quelqu'un dans une allée.</p>"),
   ('Pendant le salon', 'Des formats verticaux pour les réseaux',
    "<p>Sur le stand, on filme les démonstrations, les visiteurs, une ou deux interviews courtes, et on monte en 9:16 pour Instagram, LinkedIn ou TikTok. C'est ce que Yann a fait pour Don Papa Rum à Winterlandia : captation sur place, montage vertical de 45 secondes.</p>"
    "<p>Le délai se fixe au devis : si vous voulez publier pendant le salon, on organise le montage en conséquence.</p>"),
   ('Après le salon', "Le film de l'événement",
    "<p>Un aftermovie sert à l'équipe commerciale, au site, et à l'inscription de l'année suivante. Pour The Ink Factory, la convention de tatouage de Lyon, Yann a signé un aftermovie de 2 min 34.</p>"),
   ('Où', 'Lyon, et les salons ailleurs',
    "<p>SilverFrame est basé à Lyon, rue de la Part-Dieu. On tourne sur les salons lyonnais comme ailleurs en France et à l'étranger.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Chaque salon est chiffré sur devis : nombre de jours sur place, film de stand ou non, nombre de formats à livrer.</p>"),
  ],
  livrables=['Film de stand en boucle', 'Formats 9:16', 'Interviews courtes', 'Aftermovie', 'Sous-titres', 'Photo'],
  sujet='Salon professionnel', service='Vidéo de salon professionnel', type='Production vidéo pour salon professionnel',
  lies=['evenement', 'reseaux', 'entreprise'], cas=['vjm', 'don-papa', 'ink-factory']),

 dict(cle='reseaux', url='/video-reseaux-sociaux-lyon/', nav='Réseaux sociaux', court='Formats verticaux 9:16, déclinaisons 1:1 et 16:9',
  titre='Vidéo pour les réseaux sociaux à Lyon · formats verticaux',
  desc="Vidéos pour Instagram, TikTok et LinkedIn à Lyon : formats verticaux tournés pour le 9:16, déclinaisons 1:1 et 16:9, sous-titres. Sur devis, par Yann Volle.",
  h1='Vidéos pour les réseaux sociaux',
  intro="Le Crédit Agricole avec l'artiste Lorem et l'équipe de France. Des maillots portés par une nageuse olympique. Une œuvre pour le Téléthon. <em>Trois films pensés pour un écran de téléphone, dès le tournage.</em>",
  postes=['9:16', '1:1', '16:9', 'Sous-titres', 'Déclinaisons'],
  films=['ca-fff', 'ozur', 'telethon'],
  blocs=[
   ('Tourner vertical', 'Cadrer pour le 9:16 dès le tournage',
    "<p>Recadrer un film horizontal à la fin fait perdre la moitié de l'image. On cadre pour le téléphone dès le plateau, et on garde de la marge quand une version 16:9 est aussi prévue.</p>"
    "<p>Pour Ozur, Yann a tourné et monté en vertical la collection de maillots, portée par une nageuse olympique (49 secondes) : <a class=\"lien\" href=\"/realisations/ozur-maillots/\">l'histoire du film</a>. Pour le Crédit Agricole, avec l'artiste Lorem et l'équipe de France de football, il a réalisé, tourné et monté un film vertical d'1 min 06 : <a class=\"lien\" href=\"/post/credit-agricole-lorem-equipe-de-france-football/\">les coulisses</a>.</p>"),
   ('Un tournage, plusieurs formats', 'La même matière, déclinée',
    "<p>Un tournage peut donner un film principal et plusieurs formats courts : 9:16 pour les stories et les reels, 1:1 pour un fil, 16:9 pour YouTube ou un site. Les sous-titres sont prévus pour une lecture sans le son.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Le prix dépend du nombre de jours de tournage et du nombre de formats à livrer. C'est sur devis.</p>"),
  ],
  livrables=['9:16', '1:1', '16:9', 'Sous-titres'],
  sujet='Vidéos réseaux sociaux', service='Vidéo pour les réseaux sociaux', type='Production de vidéos pour les réseaux sociaux',
  lies=['marque', 'evenement', 'agences'], cas=['ozur', 'ca-fff']),

 dict(cle='marque', url='/film-de-marque-publicite-lyon/', nav='Film de marque et publicité', court='Produit, geste, image de marque',
  titre='Film de marque et publicité à Lyon | SilverFrame Agency',
  desc="Film de marque et publicité à Lyon : produit, geste, image. Réalisation, tournage avec équipe image, son et lumière, montage et étalonnage. Sur devis.",
  h1='Film de marque et publicité à Lyon',
  intro="Des pointes peintes à la main, une sprinteuse, un stade de nuit. Un fil de broderie filmé de si près qu'on en voit les fibres. <em>Un film de marque montre ce qui rend un produit différent, en images.</em>",
  postes=['Réalisation', 'Tournage', 'Effets', 'Montage', 'Étalonnage'],
  films=['keyena', 'vangart-macro', 'vangart-fab'],
  blocs=[
   ('Deux références', 'Keyena × Artik, et VANGART',
    "<p>Pour Keyena × Artik, Yann a réalisé, tourné et étalonné un film de 33 secondes : des pointes peintes à la main, une sprinteuse, un stade de nuit. <a class=\"lien\" href=\"/realisations/keyena-artik/\">L'histoire du film</a>.</p>"
    "<p>Pour VANGART, il a réalisé « Le fil, de très près » (réalisation, effets, étalonnage, 50 secondes) et « La fabrication des toiles brodées » (1 min 29).</p>"
    "<figure class=\"citation\"><blockquote>« On bosse avec SilverFrame depuis presque 5 ans, et ils ont signé la totalité des vidéos de VANGART. Clairement, ils ont beaucoup joué dans la construction de notre image. »</blockquote><figcaption>BENJAMIN BEAU · VANGART</figcaption></figure>"),
   ('L\'équipe', 'Seul pour un format court, en équipe pour un film de marque',
    "<p>Yann réalise, tourne, monte et étalonne. Pour un film de marque, il vient avec une équipe image, son et lumière. Le même regard tient le film du repérage à l'étalonnage.</p>"),
   ('Livraison', 'Un master, et ses déclinaisons',
    "<p>Un master 4K, puis les versions courtes et verticales pour les réseaux, avec ou sans sous-titres.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Un film de marque est chiffré sur devis, après un échange sur l'idée, l'équipe et les décors.</p>"),
  ],
  livrables=['Master 4K', '16:9 · 9:16 · 1:1', 'Versions courtes', 'Sous-titres'],
  sujet='Film de marque', service='Film de marque et publicité', type='Réalisation de film publicitaire',
  lies=['reseaux', 'agences', 'montage'], cas=['keyena']),

 dict(cle='agences', url='/agences-marque-blanche/', nav='Pour les agences', court='Production en marque blanche, sous votre nom',
  titre='Production vidéo pour agences, en marque blanche · Lyon',
  desc="Production vidéo en marque blanche pour les agences : repérage, tournage, montage, étalonnage, déclinaisons réseaux, sous votre nom si besoin. Lyon, sur devis.",
  h1='Production vidéo pour les agences, en marque blanche',
  intro="Vous gardez le client et l'idée. <em>On prend la production : repérage, tournage, montage, étalonnage, et les déclinaisons pour les réseaux.</em>",
  postes=['Marque blanche', 'Tournage', 'Montage', 'Étalonnage', 'Déclinaisons'],
  films=['ca-fff', 'keyena', 'ink-factory'],
  blocs=[
   ('Comment on travaille', "Votre équipe image, le temps d'un projet",
    "<ul class=\"points\"><li><b>Le même regard du début à la fin.</b> Yann réalise, tourne, monte et étalonne. Rien ne se perd entre le plateau et la post-production.</li>"
    "<li><b>Seul ou en équipe.</b> Seul avec son matériel pour un format court, avec une équipe image, son et lumière pour un film de marque.</li>"
    "<li><b>Sous votre nom si besoin.</b> On peut intervenir pour l'agence, face à son client, sans le démarcher ensuite.</li>"
    "<li><b>Lyon, et ailleurs.</b> Basé à Lyon, on tourne partout en France et à l'étranger.</li></ul>"),
   ('Ils en parlent', 'Deux agences qui travaillent déjà avec Yann',
    "<figure class=\"citation\"><blockquote>« Nous travaillons avec SilverFrame depuis plus d'un an : une structure incroyable et un professionnalisme rarissime. On recommande à 150 %. »</blockquote><figcaption>M&amp;R DIGITAL AGENCY</figcaption></figure>"
    "<figure class=\"citation\"><blockquote>« Très réactif, professionnel et humain. Travail de très grande qualité. »</blockquote><figcaption>ROMAIN UGHETTO · COMING SOON AGENCY</figcaption></figure>"),
   ('Le déroulé', 'Du brief à la livraison',
    "<p>Vous envoyez le brief, même partiel. Yann revient avec une approche et un devis. Il tourne et monte, vous validez les versions, puis il livre le master et les déclinaisons, au nom de l'agence si vous le souhaitez.</p>"
    "<p>Exemple de projet à plusieurs voix : le film du Crédit Agricole avec l'artiste Lorem et l'équipe de France de football. <a class=\"lien\" href=\"/post/credit-agricole-lorem-equipe-de-france-football/\">Les coulisses</a>.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Chaque projet est chiffré sur devis, à partir de votre brief.</p>"),
  ],
  livrables=['Master 4K', '16:9 · 9:16 · 1:1', 'Formats réseaux', 'Sous-titres', 'Photo de plateau', 'Aftermovie'],
  sujet='Agence · production', service='Production vidéo en marque blanche pour les agences', type='Production vidéo en marque blanche',
  lies=['marque', 'evenement', 'reseaux'], cas=['ca-fff', 'keyena', 'ink-factory'], en='/en/agencies/'),

 dict(cle='montage', url='/montage-etalonnage-lyon/', nav='Montage et étalonnage', court='Montage, étalonnage, clips',
  titre='Montage et étalonnage vidéo à Lyon | SilverFrame Agency',
  desc="Montage et étalonnage vidéo à Lyon : films de marque, campagnes, clips. Yann Volle monte et étalonne, sous DaVinci Resolve, les films qu'il tourne. Sur devis.",
  h1='Montage et étalonnage à Lyon',
  intro="La plupart des films qui sortent de chez nous sont étalonnés par Yann, de la campagne régionale du Crédit Agricole aux clips. <em>Le montage donne le rythme, l'étalonnage donne la lumière et la couleur.</em>",
  postes=['Montage', 'Étalonnage', 'Clips', 'Versions courtes', 'Sous-titres'],
  films=['sunborn', 'ca-campagne', 'ultimate'],
  blocs=[
   ('Montage', 'Le rythme, la musique, les versions',
    "<p>Le montage décide de ce qu'on garde et de l'ordre. On monte la version principale, puis les déclinaisons 16:9, 9:16 et 1:1, et les sous-titres pour une lecture sans le son.</p>"
    "<p>Pour la campagne régionale du Crédit Agricole « Agissons au cœur de nos territoires », Yann a assuré la réalisation, le montage et l'étalonnage (3 min 29).</p>"),
   ('Étalonnage', 'La couleur de chaque plan',
    "<p>L'étalonnage règle la lumière et la couleur plan par plan, pour que le film tienne d'un bout à l'autre. Yann étalonne sous DaVinci Resolve.</p>"),
   ('Clips', 'Trois clips, de la réalisation à l\'étalonnage',
    "<p>Sunborn, « Glacier » (4 min 58). Adrien Gonzales ft. EIGA, « Ultimate » (3 min 21). Bear's Towers, « Hometown » (3 min 02). Pour les trois : réalisation, montage, étalonnage.</p>"),
   ('Tarif', 'Sur devis',
    "<p>Le montage et l'étalonnage sont chiffrés sur devis, selon la durée du film et le nombre de versions.</p>"),
  ],
  livrables=['Montage', 'Étalonnage', 'Versions 16:9 · 9:16 · 1:1', 'Sous-titres', 'Master 4K'],
  sujet='Montage et étalonnage', service='Montage et étalonnage vidéo', type='Post-production vidéo',
  lies=['marque', 'entreprise', 'reseaux'], cas=[]),
]
SERVICES[2]['en'] = '/en/trade-show-video/'

# Réalisations (études de cas) ---------------------------------------------------------------------
CAS = [
 dict(cle='ca-fff', film='ca-fff', url='/post/credit-agricole-lorem-equipe-de-france-football/', date='2026-08-12',
  titre='Crédit Agricole × Lorem × Équipe de France : le film',
  desc="Les coulisses du film de SilverFrame pour le lancement de la carte Mozaïc du Crédit Agricole, avec l'artiste Lorem et l'Équipe de France de football.",
  h1='Crédit Agricole × Lorem × Équipe de France de football', resume="La carte Mozaïc, l'artiste Lorem et l'équipe de France dans un seul film vertical",
  ancien=True, services=['reseaux', 'agences', 'marque']),
 dict(cle='don-papa', film='don-papa', url='/realisations/don-papa-winterlandia/', date='2026-10-25',
  titre='Don Papa Rum, Winterlandia : bar éphémère en station',
  desc="Don Papa Rum à Winterlandia, un bar éphémère en station de ski : captation sur place et montage vertical de 45 secondes par Yann Volle, SilverFrame Agency.",
  h1='Don Papa Rum : Winterlandia, un bar éphémère en station de ski', resume='Captation sur place et montage vertical de 45 secondes',
  contexte="<p>Pour Don Papa Rum, la marque de rhum philippine, Yann a filmé Winterlandia, un bar éphémère en station de ski.</p>"
           "<p class=\"source\">Sur la marque : <a href=\"https://www.thespiritsbusiness.com/?p=718499\" rel=\"noopener\" target=\"_blank\">The Spirits Business</a> (la canne à sucre de Don Papa vient de l'île de Negros, aux Philippines).</p>",
  defi="<p>Un bar éphémère ne dure qu'une saison. Le film doit donner envie d'y monter, sur un téléphone, en quelques secondes, avec ce qui se passe vraiment dans le bar.</p>",
  approche="<p>Yann a filmé sur place puis monté le film en vertical, au format des stories et des reels : 45 secondes, mises en ligne sur Vimeo en février 2026.</p>",
  services=['evenement', 'salon', 'reseaux']),
 dict(cle='keyena', film='keyena', url='/realisations/keyena-artik/', date='2026-10-25',
  titre='Keyena × Artik : pointes peintes à la main, film de marque',
  desc="Keyena × Artik : des pointes peintes à la main, une sprinteuse, un stade de nuit. Film de marque de 33 secondes réalisé, tourné et étalonné par Yann Volle.",
  h1='Keyena × Artik : des pointes peintes à la main, un stade de nuit', resume='Réalisation, tournage et étalonnage d\'un film de marque de 33 secondes',
  contexte="<p>Keyena est une marque d'équipement pour l'athlétisme, créée par l'ancienne athlète Coralie Gassama : elle fabrique la Key One, une sur-semelle qui protège les pointes. Le film, réalisé pour la collaboration Keyena × Artik, montre des pointes peintes à la main.</p>"
           "<p class=\"source\">Sur Keyena : <a href=\"https://le10sport.com/omnisport/coralie-gassama-et-la-revolution-keyena-653815\" rel=\"noopener\" target=\"_blank\">Le 10 Sport</a> et <a href=\"https://stadion-actu.fr/athletisme-le-footballeur-dayot-upamecano-investit-dans-la-start-up-keyena/\" rel=\"noopener\" target=\"_blank\">Stadion Actu</a>.</p>",
  defi="<p>Trente-trois secondes pour montrer deux choses qui vont à des vitesses opposées : un objet peint à la main, qu'on veut regarder de près, et une sprinteuse lancée sur la piste, de nuit.</p>",
  approche="<p>Yann a réalisé, tourné et étalonné le film. L'étalonnage fait tenir ensemble la nuit du stade et les couleurs des pointes peintes.</p>",
  services=['marque', 'reseaux', 'agences']),
 dict(cle='ink-factory', film='ink-factory', url='/realisations/the-ink-factory-aftermovie/', date='2026-10-25',
  titre="The Ink Factory : aftermovie de la convention de tatouage",
  desc="The Ink Factory, convention internationale de tatouage de Lyon : aftermovie de 2 min 34, captation, montage et étalonnage par Yann Volle, SilverFrame Agency.",
  h1="The Ink Factory : l'aftermovie de la convention de tatouage de Lyon", resume='Captation, montage et étalonnage d\'un aftermovie de 2 min 34',
  contexte="<p>The Ink Factory est la convention internationale de tatouage de Lyon : trois jours de tatouage devant le public. Pour l'édition de septembre 2026, les organisateurs annonçaient plus de 350 artistes.</p>"
           "<p class=\"source\">Édition 2026 : <a href=\"https://lebonbon.fr/lyon/loisirs/lyon-capitale-mondiale-tatouage-350-tatoueurs/\" rel=\"noopener\" target=\"_blank\">Le Bonbon Lyon</a>.</p>",
  defi="<p>Des centaines de tatoueurs au travail en même temps, du bruit, de la foule. L'aftermovie doit garder cette densité sans perdre celui qui regarde, et donner envie de venir à l'édition suivante.</p>",
  approche="<p>Yann a fait la captation pendant la convention, puis le montage et l'étalonnage : un aftermovie de 2 min 34, mis en ligne sur Vimeo en avril 2026.</p>",
  services=['evenement', 'salon', 'agences']),
 dict(cle='vjm', film='vjm', url='/realisations/vjm-sertissage-macro/', date='2026-10-25',
  titre='VJM : le sertissage filmé en macro · étude de cas SilverFrame',
  desc="VJM : le sertissage d'une pierre filmé en macro, à quelques millimètres. Tournage macro et étalonnage d'un film de 24 secondes par Yann Volle, SilverFrame Agency.",
  h1='VJM : le sertissage, filmé en macro', resume='Tournage macro et étalonnage d\'un film de 24 secondes',
  contexte="<p>Le sertissage est le geste qui fixe une pierre sur un bijou. Pour VJM, Yann l'a filmé en macro, à l'échelle de la pierre.</p>",
  defi="<p>À cette échelle, la zone nette ne fait que quelques millimètres et le moindre mouvement de la main sort du cadre. Il faut suivre le geste sans le gêner.</p>",
  approche="<p>Tournage macro et étalonnage, pour un film de 24 secondes, mis en ligne sur Vimeo en mars 2026. Un format court qui peut tourner en boucle sur un écran de boutique ou de stand.</p>",
  services=['entreprise', 'salon', 'marque']),
 dict(cle='ozur', film='ozur', url='/realisations/ozur-maillots/', date='2026-10-25',
  titre='Ozur : maillots portés par une nageuse olympique · SilverFrame',
  desc="Ozur : la collection de maillots, portée par une nageuse olympique. Tournage et montage vertical d'un film de 49 secondes par Yann Volle, SilverFrame Agency.",
  h1='Ozur : les maillots, portés par une nageuse olympique', resume='Tournage et montage vertical d\'un film de 49 secondes',
  contexte="<p>Ozur a présenté sa collection de maillots, portée par une nageuse olympique, dans un film pensé pour les réseaux.</p>",
  defi="<p>Montrer un maillot sur une sportive de haut niveau, pour un écran de téléphone : le cadre vertical laisse peu de place, il faut choisir chaque plan.</p>",
  approche="<p>Yann a tourné et monté le film en vertical : 49 secondes, mises en ligne sur Vimeo en avril 2026.</p>",
  services=['reseaux', 'marque', 'agences']),
]
