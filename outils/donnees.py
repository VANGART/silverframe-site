# Données du site SilverFrame Agency (source unique des pages générées par outils/generer.py).
# Faits : SILVERFRAME/Presentation.html (table FILMS), SILVERFRAME/CLAUDE.md, la consigne de prospection
# (« Ce qu'on peut dire de Yann »), le site du 22/10/2026, et les données publiques de Vimeo (oEmbed :
# date de mise en ligne, durée). Aucun prix : tout est sur devis (règle du 25/10/2026).

SITE = 'https://www.silverframeagency.com'
MAIL = 'silverframeagency@gmail.com'
TEL = '+33677521036'
MAJ = '2026-10-25'

# clé : (vimeo, client, titre fr, titre en, générique fr, générique en, durée, vertical, année, filtre,
#        libellé fr, libellé en, largeur vignette, hauteur vignette, mise en ligne Vimeo, durée en secondes)
FILMS = {
  'ca-fff':       ('1217039625', 'Crédit Agricole × FFF', "Un match de l'équipe de France, avec l'artiste Lorem", 'A France national team match, with the artist Lorem', 'Réalisation, tournage, montage', 'Direction, shoot, edit', '1:06', 1, '2026', 'social', 'Réseaux sociaux', 'Social media', 900, 1600, '2026-08-10', 66),
  'don-papa':     ('1168529161', 'Don Papa Rum', 'Winterlandia, un bar éphémère en station de ski', 'Winterlandia, a pop-up bar in a ski resort', 'Captation, montage vertical', 'Coverage, vertical edit', '0:45', 1, '2026', 'event', 'Événementiel', 'Events', 1280, 720, '2026-02-26', 45),
  'ozur':         ('1188034228', 'Ozur', 'Les maillots, portés par une nageuse olympique', 'The swimwear, worn by an Olympic swimmer', 'Tournage, montage vertical', 'Shoot, vertical edit', '0:49', 1, '2026', 'social', 'Mode', 'Fashion', 1280, 624, '2026-04-30', 49),
  'ink-factory':  ('1188031932', 'The Ink Factory', 'Aftermovie de la convention internationale de tatouage de Lyon', 'Aftermovie of the Lyon international tattoo convention', 'Captation, montage, étalonnage', 'Coverage, edit, grade', '2:34', 0, '2026', 'event', 'Aftermovie', 'Aftermovie', 1280, 624, '2026-04-30', 154),
  'vjm':          ('1176655479', 'VJM', 'Le sertissage, filmé en macro', 'Stone setting, shot in macro', 'Tournage macro, étalonnage', 'Macro shoot, grade', '0:24', 0, '2026', 'corporate', 'Joaillerie', 'Jewellery', 1280, 720, '2026-03-24', 24),
  'sunborn':      ('1156001897', 'Sunborn', '« Glacier », clip', '"Glacier", music video', 'Réalisation, montage, étalonnage', 'Direction, edit, grade', '4:58', 0, '2026', 'clip', 'Clip', 'Music video', 1280, 720, '2026-01-19', 298),
  'keyena':       ('1059359077', 'Keyena × Artik', 'Des pointes peintes à la main, une sprinteuse, un stade de nuit', 'Hand-painted spikes, a sprinter, a stadium at night', 'Réalisation, tournage, étalonnage', 'Direction, shoot, grade', '0:33', 0, '2025', 'marque', 'Film de marque', 'Brand film', 1280, 720, '2025-02-22', 33),
  'ca-candice':   ('1059358866', 'Crédit Agricole', 'Portrait de Candice Chlovy, agricultrice en Auvergne-Rhône-Alpes', 'Portrait of Candice Chlovy, a farmer in Auvergne-Rhône-Alpes', 'Réalisation, tournage, étalonnage', 'Direction, shoot, grade', '3:33', 0, '2025', 'corporate', 'Portrait', 'Portrait', 1280, 624, '2025-02-22', 213),
  'ca-campagne':  ('1059359955', 'Crédit Agricole', 'Campagne régionale « Agissons au cœur de nos territoires »', 'Regional campaign for Crédit Agricole', 'Réalisation, montage, étalonnage', 'Direction, edit, grade', '3:29', 0, '2025', 'corporate', 'Corporate', 'Corporate', 1280, 480, '2025-02-22', 209),
  'telethon':     ('1039204100', 'LOREM × VANGART', 'Une œuvre pour le Téléthon 2024', 'An artwork for the 2024 Téléthon', 'Tournage, montage vertical', 'Shoot, vertical edit', '0:30', 1, '2024', 'social', 'Réseaux sociaux', 'Social media', 1280, 2276, '2024-12-14', 30),
  'ultimate':     ('1039051701', 'Adrien Gonzales ft. EIGA', '« Ultimate », clip', '"Ultimate", music video', 'Réalisation, montage, étalonnage', 'Direction, edit, grade', '3:21', 0, '2024', 'clip', 'Clip', 'Music video', 1280, 720, '2024-12-13', 201),
  'vangart-macro':('794421371',  'VANGART', 'Le fil, de très près', 'Thread, up close', 'Réalisation, effets, étalonnage', 'Direction, VFX, grade', '0:50', 0, '2023', 'marque', 'Publicité', 'Advertising', 1280, 624, '2023-01-31', 50),
  'monfairepart': ('890836795',  'Monfairepart', "Dans l'atelier de fabrication", 'Inside the production workshop', 'Tournage, montage', 'Shoot, edit', '0:34', 0, '2023', 'corporate', 'Corporate', 'Corporate', 1280, 720, '2023-12-03', 34),
  'vangart-fab':  ('691045247',  'VANGART', 'La fabrication des toiles brodées', 'How the embroidered artworks are made', 'Réalisation, tournage, étalonnage', 'Direction, shoot, grade', '1:29', 0, '2022', 'marque', 'Film de marque', 'Brand film', 1280, 624, '2022-03-22', 89),
  'bears':        ('751282874',  "Bear's Towers", '« Hometown », clip', '"Hometown", music video', 'Réalisation, montage, étalonnage', 'Direction, edit, grade', '3:02', 0, '2022', 'clip', 'Clip', 'Music video', 1280, 640, '2022-09-19', 182),
}
ORDRE = ['ca-fff', 'don-papa', 'ozur', 'ink-factory', 'vjm', 'sunborn', 'keyena', 'ca-candice', 'ca-campagne', 'telethon', 'ultimate', 'vangart-macro', 'monfairepart', 'vangart-fab', 'bears']
BANDE = ['ca-fff', 'keyena', 'ink-factory', 'don-papa', 'vangart-macro', 'sunborn', 'ozur', 'ca-candice']
GRILLE = [('vangart-macro', 'g'), ('keyena', ''), ('ca-fff', ''), ('ink-factory', ''), ('don-papa', ''), ('sunborn', ''), ('ca-candice', ''), ('ozur', 'g'), ('vjm', ''), ('ultimate', ''), ('bears', ''), ('monfairepart', ''), ('vangart-fab', ''), ('ca-campagne', ''), ('telethon', ''), ('kosmos', '')]
FILTRES = {'fr': [('tout', 'Tout'), ('marque', 'Marques'), ('corporate', 'Corporate'), ('event', 'Événementiel'), ('social', 'Réseaux sociaux'), ('clip', 'Clips')],
           'en': [('tout', 'All'), ('marque', 'Brands'), ('corporate', 'Corporate'), ('event', 'Events'), ('social', 'Social media'), ('clip', 'Music videos')]}

# Titres courts de l'accueil (index), repris du site du 22/10/2026
COURT = {'fr': {'ca-fff': "Un match de l'équipe de France, avec l'artiste Lorem", 'ink-factory': 'Aftermovie de la convention de tatouage', 'ozur': 'Les maillots, portés par une nageuse olympique',
                'sunborn': '« Glacier »', 'keyena': 'Des pointes peintes à la main, un stade de nuit', 'ca-candice': 'Candice Chlovy, agricultrice', 'ca-campagne': 'Campagne régionale',
                'telethon': 'Une œuvre pour le Téléthon', 'ultimate': '« Ultimate »', 'bears': '« Hometown »', 'don-papa': 'Winterlandia, un bar éphémère en station'},
         'en': {'ca-fff': 'A France national team match, with the artist Lorem', 'ink-factory': 'Aftermovie of the tattoo convention', 'sunborn': '"Glacier"', 'keyena': 'Hand-painted spikes, a stadium at night',
                'ca-candice': 'Candice Chlovy, farmer', 'ca-campagne': 'Regional campaign', 'telethon': 'An artwork for the Téléthon', 'ultimate': '"Ultimate"', 'bears': '"Hometown"'}}

LOGOS = [('credit-agricole', 'Crédit Agricole', 600, 122), ('fff', 'Équipe de France', 235, 300), ('deutsche-welle', 'Deutsche Welle', 533, 300), ('wella', 'Wella', 406, 300),
         ('don-papa', 'Don Papa Rum', 600, 182), ('chapoutier', 'M. Chapoutier', 600, 199), ('aluna', 'Aluna Festival', 283, 300), ('ink-factory', 'The Ink Factory', 290, 300),
         ('kosmos', 'Kosmos', 600, 246), ('mjh', 'MJH Life Sciences', 600, 130), ('monfairepart', 'Monfairepart', 600, 129), ('vangart', 'VANGART', 371, 300)]
NOM_EN = {'Équipe de France': 'France national football team'}

PAROLES = {
  'fr': [("Nous travaillons avec SilverFrame depuis plus d'un an : une structure incroyable et un professionnalisme rarissime. On recommande à 150 %.", 'M&R DIGITAL AGENCY'),
         ("On bosse avec SilverFrame depuis presque 5 ans, et ils ont signé la totalité des vidéos de VANGART. Clairement, ils ont beaucoup joué dans la construction de notre image.", 'BENJAMIN BEAU · VANGART'),
         ("Très réactif, professionnel et humain. Travail de très grande qualité.", 'ROMAIN UGHETTO · COMING SOON AGENCY'),
         ("La vidéo est exceptionnelle et répond parfaitement à nos attentes.", 'MARYLINE JULLIEN · MARGARON')],
  'en': [("We have worked with SilverFrame for over a year: an incredible outfit and a rare level of professionalism. We recommend them 150%.", 'M&R DIGITAL AGENCY'),
         ("We've worked with SilverFrame for almost five years, and they made every single VANGART video. They clearly played a big part in building our image.", 'BENJAMIN BEAU · VANGART'),
         ("Very responsive, professional and human. Work of very high quality.", 'ROMAIN UGHETTO · COMING SOON AGENCY'),
         ("The video is exceptional and meets our expectations perfectly.", 'MARYLINE JULLIEN · MARGARON')],
}
