# -*- coding: utf-8 -*-
"""Génère index.html (volet débutant) et intermediaire.html (volet intermédiaire)."""
import io, re, os

R = os.path.dirname(os.path.abspath(__file__))
def lire(n): return io.open(os.path.join(R, n), encoding='utf-8').read()

# (type, minute, durée, titre, texte, [(problème, correction)])
I = []

I.append(dict(id="i1", num="I", titre="Nommer le manche",
 objectif="Les notes sur mi grave et la, et la seule règle qui compte : <em>un demi-ton = une case</em>. Sans ça, ni les barrés ni les positions de gamme n'ont de nom, et il joue des formes sans savoir ce qu'il joue.",
 steps=[
  ("cadre",0,4,"Où il en est","Il joue une grille de blues et une boîte de pentatonique. Tu regardes ce qui est acquis pour de vrai.",[]),
  ("montre",4,6,"Do Ré Mi = C D E","La correspondance d'abord, elle prend deux minutes et elle lui manque depuis le début. Les tablatures et les grilles qu'il télécharge sont en notation anglaise, ses cours sont en français.",
    [("Il traduit à chaque fois dans sa tête","Normal pendant un mois. Fais-lui nommer les accords qu'il connaît déjà dans les deux langues, à voix haute, en les jouant.")]),
  ("jeu",10,9,"Tons et demi-tons","Do–Ré 1 ton, Ré–Mi 1 ton, Mi–Fa un demi-ton, puis 1, 1, 1, et Si–Do un demi-ton. Un demi-ton, c'est une case, un ton deux cases. Il les joue sur la corde de Mi grave en montant, et il annonce chaque écart à voix haute.",
    [("Il oublie Mi–Fa et Si–Do","Ce sont les deux seuls endroits où deux notes voisines se touchent. Fais-lui montrer sur le manche : entre Mi et Fa il n'y a rien à sauter."),
     ("Il confond dièse et bémol","Même case, deux noms. Fa♯ et Sol♭ sont la même frette. Lequel on écrit dépend du morceau, pas du son.")]),
  ("jeu",19,15,"Les notes de la corde de Mi grave","Case 0 Mi, 1 Fa, 3 Sol, 5 La, 7 Si, 8 Do, 10 Ré, 12 Mi. Il les nomme à voix haute en jouant, du sillet à la douzième.",
    [("Il récite au lieu de trouver","Interroge-le dans le désordre : « où est le do ? » Puis « un autre do ». Réciter la suite ne sert à rien en situation.")]),
  ("jeu",34,11,"La même chose sur la corde de La","Case 0 La, 2 Si, 3 Do, 5 Ré, 7 Mi, 8 Fa, 10 Sol, 12 La. Ces deux cordes suffisent : ce sont celles qui portent les fondamentales des barrés.",[]),
  ("morceau",45,11,"On s'en sert tout de suite","Tu annonces un accord, il pose le barré au bon endroit. F, G, B♭, D. Forme de E puis forme de A. C'est là qu'il comprend à quoi ça sert.",
    [("Il cherche trois secondes à chaque fois","C'est le but de la semaine. Trois secondes aujourd'hui, une dans quinze jours.")]),
  ("cadre",56,4,"Devoirs","Un exercice quotidien de deux minutes, pas plus. C'est de la mémorisation, ça se fait en petites doses.",[]),
 ],
 pied=["<b>S'il connaît déjà les notes :</b> passe directement à la séance II et garde la douzième case pour l'échauffement. Mais vérifie d'abord dans le désordre — beaucoup croient savoir parce qu'ils savent réciter.",
       "<b>Adulte qui a fait du solfège enfant :</b> il aura le réflexe de la portée. Ne le contrarie pas, mais ramène tout au manche : ici la question est toujours « quelle case ».",
       "<b>Ce n'est pas une séance de théorie.</b> Il doit avoir la guitare en main tout du long, sinon ça ne rentre pas."],
 ft="Séance I — les notes sur le manche",
 fc=['<h5>La gamme de do</h5><pre class="tab">DO   RÉ   MI  FA   SOL  LA   SI  DO\n'
     ' C    D    E   F    G    A    B   C\n'
     '  1t   1t  ½t   1t   1t   1t  ½t</pre>'
     '<p class="cap">½ ton = 1 case. 1 ton = 2 cases. Les deux demi-tons naturels sont Mi–Fa et Si–Do : c\'est tout ce qu\'il y a à retenir.</p>',
     '<h5>Corde de Mi grave (6<sup>e</sup>)</h5><pre class="tab">case  0  1  3  5  7  8 10 12\nnote  MI FA SOL LA SI DO RÉ MI\n       E  F  G  A  B  C  D  E</pre>'
     '<h5>Corde de La (5<sup>e</sup>)</h5><pre class="tab">case  0  2  3  5  7  8 10 12\nnote  LA SI DO RÉ MI FA SOL LA\n       A  B  C  D  E  F  G  A</pre>',
     '<h5>À la maison</h5><div class="devoir"><b>Deux minutes par jour, pas plus.</b><br><br>'
     '<b>1.</b> Une note au hasard, tu la trouves sur mi grave <b>et</b> sur la.<br>'
     '<b>2.</b> Les barrés : je dis « G », tu poses la forme de E case 3.<br>'
     '<b>3.</b> Le piège : Mi–Fa et Si–Do se touchent. Aucune case entre les deux.</div>']))

I.append(dict(id="i2", num="II", titre="La pentatonique sort de sa boîte",
 objectif="Il connaît une position depuis six mois et il tourne dedans. On en ajoute deux, et surtout on apprend à passer de l'une à l'autre sans s'arrêter.",
 steps=[
  ("cadre",0,4,"Accordage, la boîte qu'il connaît","La pentatonique de La mineur, case 5. Montée-descente au métronome, pour voir où elle en est.",[]),
  ("montre",4,8,"Cinq notes, tout le manche","La, Do, Ré, Mi, Sol. Ces cinq notes-là et pas d'autres, de la case 0 à la case 15. Les « positions » ne sont que des façons de les attraper avec quatre doigts.",
    [("Il croit que chaque position est une gamme différente","C'est le contresens le plus fréquent. Fais-lui jouer un la case 5 sur mi grave, puis le même la case 12 sur la corde de La. Même note, deux endroits.")]),
  ("jeu",12,13,"La deuxième position, case 8","Elle démarre sur le do, case 8 de la corde de Mi grave. Montée-descente lentement, en nommant la fondamentale à chaque passage.",
    [("Il plaque la première position deux cases plus haut","Erreur classique. La forme change, ce sont les mêmes notes mais pas le même dessin. Fais-lui vérifier note par note.")]),
  ("jeu",25,14,"La charnière","La case 7 et la case 8 appartiennent aux deux positions. C'est par là qu'on passe. Exercice : monter dans la position V, redescendre dans la position VIII, sans s'arrêter au changement.",
    [("Il s'arrête pile au moment de changer","Le trou s'entend plus que la fausse note. Impose le métronome : il a le droit de se tromper de note, pas de s'arrêter."),
     ("Il regarde sa main gauche pendant la bascule","Fais-lui repérer la case 7 au toucher, avec le repère du manche. La main doit savoir y aller seule.")]),
  ("jeu",39,8,"La douzième case","Même dessin que la position ouverte, une octave plus haut. Il l'a déjà sous les doigts sans le savoir.",[]),
  ("morceau",47,9,"Sur une grille","Tu joues un blues lent en La, il improvise en changeant de position au moins deux fois. Consigne : chaque phrase commence dans une position et finit dans l'autre.",[]),
  ("cadre",56,4,"Devoirs","Et préviens-le : à la séance III on ajoute une note à ces cinq-là.",[]),
 ],
 pied=["<b>Si les trois positions sont trop d'un coup :</b> garde V et VIII, laisse la douzième. Deux positions bien reliées valent mieux que trois juxtaposées.",
       "<b>S'il joue vite et faux :</b> ralentis le métronome jusqu'à ce que ce soit propre, même à 50. La vitesse dans une position ne sert à rien s'il ne peut pas en sortir.",
       "<b>Sur folk :</b> tout marche pareil, mais la douzième case est difficile d'accès si le manche rejoint la caisse à la quatorzième. Reste sur V et VIII."],
 ft="Séance II — trois positions de pentatonique",
 fc=['<h5>Position V — celle que tu connais</h5><pre class="tab">e|-------------------5--8--|\nB|----------------5--8-----|\n'
     'G|-----------5--7----------|\nD|--------5--7-------------|\nA|-----5--7----------------|\nE|--5--8-------------------|</pre>'
     '<p class="cap">Pentatonique de La mineur. Fondamentale : case 5 de la corde de Mi grave.</p>',
     '<h5>Position VIII</h5><pre class="tab">e|--------------------8--10--|\nB|----------------8--10------|\n'
     'G|------------7--9-----------|\nD|--------7--10--------------|\nA|----7--10------------------|\nE|--8--10--------------------|</pre>'
     '<p class="cap">Démarre sur le do, case 8. Ce sont les mêmes cinq notes, un autre dessin.</p>'
     '<h5>La charnière</h5><p class="cap">Les cases 7 et 8 appartiennent aux deux positions. C\'est le seul endroit par lequel passer.</p>',
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> Chaque position seule, au métronome à 60, deux minutes chacune.<br>'
     '<b>2.</b> Monte en position V, redescends en position VIII. Sans t\'arrêter au changement — une fausse note en rythme vaut mieux qu\'un trou.<br>'
     '<b>3.</b> Les cinq notes : <b>La Do Ré Mi Sol</b>. Trouve-les toutes sur la corde de Si.</div>']))

I.append(dict(id="i3", num="III", titre="La gamme blues",
 objectif="Une note de plus que la pentatonique : la blue note. Elle ne se pose pas, elle se traverse — et c'est elle qui fait la différence entre jouer des notes justes et jouer du blues.",
 steps=[
  ("cadre",0,4,"Reprise","Les deux positions de la séance II, sur un tempo. Sans commentaire pendant qu'il joue.",[]),
  ("montre",4,7,"Où elle est","La gamme blues de La, c'est la pentatonique plus le Mi♭. Une seule note ajoutée, coincée entre le Ré et le Mi.",
    [("Il cherche une nouvelle gamme","Ce n'est pas une gamme nouvelle, c'est la sienne avec une note en plus. Le dire tout de suite lui économise une semaine de confusion.")]),
  ("jeu",11,12,"La blue note dans la position V","Case 6 de la corde de La, case 8 de la corde de Sol. Deux endroits, pas plus, pour commencer.",
    [("Il s'installe dessus","C'est une note de passage. Tenue, elle sonne faux ; traversée, elle sonne blues. Fais-lui jouer ré–Mi♭–mi enchaînés, puis le Mi♭ tenu quatre temps : la différence s'entend.")]),
  ("jeu",23,12,"Y arriver par le bend","Le vrai geste : partir du Ré, case 7 de la corde de Sol, et tirer d'un demi-ton. La note arrive de dessous, elle n'est pas plaquée.",
    [("Le bend d'un demi-ton dépasse","Un demi-ton, c'est peu, et la main a l'habitude du ton entier. Donne-lui la cible : joue le Mi♭ case 8, puis fais-lui viser ce son en tirant.")]),
  ("jeu",35,10,"Trois phrases","Tu joues trois phrases courtes qui utilisent la blue note, il les répète. Puis il en fabrique une quatrième avec les mêmes ingrédients.",[]),
  ("morceau",45,11,"Sur le blues en La","Tu accompagnes, il improvise. Consigne : au maximum deux blue notes par grille de douze mesures.",
    [("Il en met partout","D'où la consigne. Une blue note toutes les douze mesures s'entend ; une par mesure ne s'entend plus.")]),
  ("cadre",56,4,"Devoirs","",[]),
 ],
 pied=["<b>S'il n'entend pas la différence :</b> joue-lui deux fois la même phrase, avec et sans, sur un accompagnement. À sec, la blue note ne veut rien dire ; c'est le frottement avec l'accord qui la définit.",
       "<b>S'il veut la position VIII aussi :</b> elle y est case 11 de la corde de Mi grave et case 9 de la corde de Si. Mais ne charge pas : la position V suffit pour cette séance."],
 ft="Séance III — la gamme blues de la",
 fc=['<h5>La gamme blues, position V</h5><pre class="tab">e|--------------------------5--8--|\nB|-----------------------5--8-----|\n'
     'G|-----------------5--7--<b>8</b>--------|\nD|--------------5--7--------------|\nA|-----5--<b>6</b>--7--------------------|\nE|--5--8--------------------------|</pre>'
     '<p class="cap">Les deux notes en couleur : case 6 de la corde de La, case 8 de la corde de Sol. C\'est le Mi♭, la blue note.</p>',
     '<h5>Y arriver par le bend</h5><pre class="tab">   demi-ton\nG|--7b(8)--7--5--|</pre>'
     '<p class="cap">Pars du Ré, tire d\'un demi-ton seulement. La note doit arriver par en dessous.</p>'
     '<h5>Les six notes</h5><p>LA · DO · RÉ · <b>MI♭</b> · MI · SOL</p>'
     '<p class="cap">Cinq de la pentatonique, plus une.</p>',
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> Joue ré – Mi♭ – mi enchaînés, en boucle. Puis tiens le Mi♭ quatre temps : écoute comme ça sonne faux. C\'est normal.<br>'
     '<b>2.</b> Le bend d\'un demi-ton, case 7 corde de Sol. Vérifie en jouant la case 8 juste avant.<br>'
     '<b>3.</b> Sur un blues : <b>deux blue notes maximum</b> par grille de douze mesures.</div>']))

I.append(dict(id="i4", num="IV", titre="Le mouvement perpétuel",
 objectif="La main droite en aller-retour strict, qui ne s'interrompt jamais, même en changeant de corde. C'est la séance la plus ingrate des dix et celle qui débloque tout le reste.",
 steps=[
  ("cadre",0,4,"L'annonce","Rien de neuf à la main gauche aujourd'hui. Une heure sur le médiator.",[]),
  ("montre",4,7,"La règle","Le médiator descend sur les temps, remonte sur les contretemps. Toujours. Peu importe la note, peu importe la corde. Si la main s'arrête, le tempo s'arrête.",[]),
  ("jeu",11,14,"Le chromatique, corde de Mi grave","Un doigt par case. 0-1-2-3, puis 2-3-4-5, puis 3-4-5-6, puis 4-5-6-7. Métronome à 60, une note par temps, puis deux.",
    [("Il repart vers le bas après une corde à vide","Le réflexe le plus tenace. Fais-lui compter à voix haute « bas-haut-bas-haut » pendant qu'il joue, deux minutes."),
     ("L'auriculaire décroche","Il ne suit pas encore. Descends le tempo jusqu'à ce qu'il tienne, même à 40. Ce doigt-là se gagne en trois semaines.")]),
  ("jeu",25,13,"Le changement de corde","Le même exercice en traversant les six cordes. C'est au passage d'une corde à l'autre que l'aller-retour saute.",
    [("Le poignet se bloque et il joue du coude","Repose-lui l'avant-bras sur la caisse et fais-lui jouer très petit, à deux millimètres des cordes. L'amplitude est l'ennemi de la régularité.")]),
  ("jeu",38,9,"Sur la pentatonique","Les positions de la séance II, en aller-retour strict. Deux notes par corde, donc un changement de corde toutes les deux notes : c'est le cas le plus difficile.",[]),
  ("morceau",47,9,"Sur un morceau","Un riff qu'il connaît déjà, rejoué en aller-retour strict au lieu de tout attaquer vers le bas. Il va détester, et il va gagner en vitesse dans le mois.",
    [("Ça sonne moins bien qu'avant","Vrai, sur le moment. Les coups vers le haut sont plus faibles tant que la main n'est pas réglée. C'est le prix, et ça se corrige tout seul.")]),
  ("cadre",56,4,"Devoirs","Le chiffre de la semaine : le tempo auquel le chromatique reste propre.",[]),
 ],
 pied=["<b>S'il trouve la séance inutile :</b> demande-lui de jouer sa pentatonique deux fois plus vite. Il n'y arrivera pas en attaquant tout vers le bas. La démonstration vaut mieux que l'argument.",
       "<b>Sur électrique, avec de la saturation :</b> coupe la disto. En son clair il entend l'irrégularité entre les coups vers le bas et vers le haut, et c'est exactement ce qu'on travaille."],
 ft="Séance IV — l'aller-retour",
 fc=['<h5>Le chromatique</h5><pre class="tab">e|-------------------------------|\nB|-------------------------------|\n'
     'G|-------------------------------|\nD|-------------------------------|\nA|-------------------------------|\n'
     'E|--0--1--2--3--2--3--4--5-------|\n   ↓  ↑  ↓  ↑  ↓  ↑  ↓  ↑\n\n'
     'E|--3--4--5--6--4--5--6--7-------|\n   ↓  ↑  ↓  ↑  ↓  ↑  ↓  ↑</pre>'
     '<p class="cap">Un doigt par case. Puis la même chose sur les six cordes.</p>',
     '<h5>La règle</h5><ul><li>Le médiator <b>descend sur les temps</b>, remonte sur les contretemps.</li>'
     '<li>Y compris après une corde à vide.</li><li>Y compris en changeant de corde.</li>'
     '<li>Amplitude minimale : deux millimètres. Plus grand, c\'est plus lent.</li></ul>'
     '<h5>Le piège</h5><p class="cap">Deux notes par corde, comme dans la pentatonique : c\'est le cas où l\'aller-retour saute le plus facilement.</p>',
     '<h5>À la maison</h5><div class="devoir"><b>Cinq minutes par jour, au métronome.</b><br><br>'
     '<b>1.</b> Le chromatique à 60, une note par temps. Puis deux notes par temps.<br>'
     '<b>2.</b> La pentatonique en aller-retour strict, lentement.<br>'
     '<b>3.</b> Note le tempo le plus rapide où c\'est encore <b>propre</b> → <span class="mono">______</span></div>']))

I.append(dict(id="i5", num="V", titre="Le blues en accords de sixte",
 objectif="Arrêter de gratter des accords sur un blues et commencer à l'accompagner. Trois notes qui bougent, une basse à vide, et le shuffle à ♩=100.",
 steps=[
  ("cadre",0,4,"Reprise","La grille de douze mesures en la, en accords ouverts. C'est le point de départ qu'on va remplacer.",[]),
  ("montre",4,8,"Pourquoi la sixte","Un accord de blues n'a pas besoin de six cordes. Trois notes bien placées et une basse suffisent — et ça laisse de la place au chanteur ou au soliste.",[]),
  ("jeu",12,15,"Le va-et-vient sur la","La corde de La à vide en basse, et trois notes sur Ré-Sol-Si qui alternent entre la case 7 et la case 5. C'est tout l'accompagnement du premier accord.",
    [("Il fait sonner les cordes graves inutiles","La main droite n'attaque que la basse puis le bloc de trois. C'est un geste en deux temps, pas un grattage."),
     ("Le bloc de trois ne sonne pas ensemble","Les trois doigts se posent en même temps, pas l'un après l'autre. Fais-lui poser-lever dix fois sans jouer.")]),
  ("jeu",27,12,"Le shuffle, à 100","Ternaire. Le premier temps long, le second court. Chante-le pendant qu'il joue, ne l'explique pas.",
    [("Ça redevient binaire quand il accélère","Reste à 80 jusqu'à ce que ce soit installé. Le tempo du morceau imprimé, c'est 100 — il y viendra.")]),
  ("jeu",39,9,"Les deux autres degrés","Même principe sur D et sur E, mais le bloc se joue sur les trois cordes aiguës. D case 7, C case 5, E case 9.",[]),
  ("morceau",48,8,"La grille entière","Douze mesures d'affilée, sans s'arrêter. Puis tu improvises dessus pendant qu'il accompagne — c'est son vrai métier de guitariste rythmique qui commence là.",[]),
  ("cadre",56,4,"Devoirs","",[]),
 ],
 pied=["<b>C'est une séance qui peut prendre deux cours.</b> Le va-et-vient sur la corde de La est un geste entièrement nouveau. Ne passe pas aux autres degrés tant que le premier n'est pas fluide.",
       "<b>Sur folk :</b> ça marche très bien, c'est même l'idiome du blues acoustique. Attaque au médiator ou au pouce, comme il préfère.",
       "<b>S'il a du mal à tenir la basse :</b> laisse tomber la basse pendant dix minutes et ne fais que les blocs. Tu la rajoutes après."],
 ft="Séance V — le blues en sixtes",
 fc=['<h5>Le premier degré (A)</h5><pre class="tab">   A6       G6\ne|-----------------|\nB|--7--------5-----|\n'
     'G|--6--------4-----|\nD|--7--------5-----|\nA|--0--0-----0--0--|\nE|-----------------|</pre>'
     '<p class="cap">Basse à vide, puis le bloc de trois. Va-et-vient entre case 7 et case 5.</p>',
     '<h5>Les autres degrés</h5><pre class="tab">   D6    C6      E6\ne|--7-----5-------9--|\n'
     'B|--7-----5-------9--|\nG|--7-----5-------9--|\nD|--0-----0----------|\nA|----------------0--|\nE|-------------------|</pre>'
     '<p class="cap">Même idée, sur les trois cordes aiguës. Basse de Ré à vide, puis de Mi à vide.</p>'
     '<h5>La grille</h5><div class="grille"><span>A</span><span>A</span><span>A</span><span>A</span>'
     '<span>D</span><span>D</span><span>A</span><span>A</span><span>E</span><span>D</span><span>A</span><span>A</span></div>',
     '<h5>Le shuffle</h5><p>Ternaire, ♩ = 100. Le premier temps long, le second court. Si tu ne peux pas le chanter en jouant, tu joues trop vite.</p>'
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> Le va-et-vient sur la seule, deux minutes sans t\'arrêter, à 80.<br>'
     '<b>2.</b> Pose les trois doigts <b>en même temps</b>. Pose-lève dix fois sans jouer.<br>'
     '<b>3.</b> La grille entière à 80, puis à 90. Le 100 viendra.</div>']))

I.append(dict(id="i6", num="VI", titre="Le turnaround",
 objectif="Les deux dernières mesures d'un blues. C'est ce qui sépare quelqu'un qui joue douze mesures de quelqu'un qui joue un blues — et c'est court, donc apprenable en une heure.",
 steps=[
  ("cadre",0,4,"Reprise","La grille en sixtes de la séance V. Tu comptes les mesures à voix haute, il joue.",[]),
  ("montre",4,8,"À quoi ça sert","Les mesures 11 et 12 ramènent au début. Sans turnaround, la grille s'arrête et repart ; avec, elle tourne. Fais-lui entendre les deux.",[]),
  ("jeu",12,14,"Le turnaround descendant","Deux notes qui descendent chromatiquement par-dessus la basse de la, à vide. Quatre positions, une par temps.",
    [("Il descend trop vite","Une position par temps, pas deux. C'est une mesure entière, elle doit durer une mesure."),
     ("La basse à vide disparaît","Le pouce ou le médiator la relance à chaque temps. C'est elle qui tient l'harmonie pendant que le reste descend.")]),
  ("jeu",26,12,"L'accord d'arrivée","La septième de la, avec la montée sur la corde de Mi aigu. C'est la ponctuation : sans elle le turnaround reste en suspens.",
    [("Il enchaîne directement sur le début","Il manque un temps. Fais-lui compter : le turnaround occupe la mesure 11, l'accord d'arrivée la mesure 12.")]),
  ("jeu",38,10,"Dans la grille","Les douze mesures en entier, turnaround compris, trois fois d'affilée sans s'arrêter. C'est là qu'on voit s'il sait où il en est.",
    [("Il se perd et reprend au hasard","Compte avec lui les premières fois, puis tais-toi. Se perdre est normal ; s'arrêter ne doit plus l'être.")]),
  ("morceau",48,8,"À deux","Tu improvises, il tient la grille avec turnaround. Puis vous échangez — et c'est lui qui doit sentir le turnaround arriver sans le voir venir.",[]),
  ("cadre",56,4,"Devoirs","",[]),
 ],
 pied=["<b>Il en existe des dizaines.</b> N'en donne qu'un. Un turnaround qu'il joue vraiment vaut mieux que quatre qu'il reconnaît.",
       "<b>S'il joue en groupe :</b> c'est le moment de lui dire que le turnaround est un signal, pas une décoration. Les autres musiciens l'entendent et savent que ça repart."],
 ft="Séance VI — le turnaround en la",
 fc=['<h5>Le turnaround descendant</h5><pre class="tab">e|-----------------------|\nB|--5---4---3---2--------|\n'
     'G|--6---5---4---3--------|\nD|-----------------------|\nA|-----------------------|\nE|--0---0---0---0--------|</pre>'
     '<p class="cap">Une position par temps, quatre temps. La basse de mi à vide relancée à chaque fois.</p>',
     '<h5>L\'accord d\'arrivée</h5><pre class="tab">   A7\ne|--0---2---3--|\nB|--2---2---2--|\n'
     'G|--0---0---0--|\nD|--2---2---2--|\nA|--0---0---0--|\nE|-------------|</pre>'
     '<p class="cap">Mesure 12. La montée sur la corde aiguë est la ponctuation.</p>'
     '<h5>Où ça tombe</h5><div class="grille"><span>1</span><span>2</span><span>3</span><span>4</span>'
     '<span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span></div>'
     '<p class="cap">Le turnaround occupe la mesure 11. L\'accord d\'arrivée, la 12.</p>',
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> Le turnaround seul, très lentement, une position par temps.<br>'
     '<b>2.</b> Les douze mesures en entier, <b>trois fois d\'affilée sans t\'arrêter</b>. Si tu te perds, tu continues.<br>'
     '<b>3.</b> Compte les mesures à voix haute la première fois, puis en silence.</div>']))

I.append(dict(id="i7", num="VII", titre="Hey Joe, ou la grille qui monte",
 objectif="Cinq accords : <em>C, G, D, A, E</em>. Chacun est la quinte du précédent. Une fois qu'il voit ça, il ne l'oublie plus et il la retrouve dans la moitié de ce qu'il écoute.",
 steps=[
  ("cadre",0,4,"Accordage, turnaround de la semaine","",[]),
  ("jeu",4,10,"La grille","C, G, D, A, E. Une mesure chacun, deux sur le mi, et ça recommence. Il l'écrit dans son carnet avant de la jouer.",
    [("Il se perd dans une boucle de cinq accords","On compte quatre par réflexe. Fais-lui dire le nom de l'accord suivant à voix haute pendant qu'il joue le précédent.")]),
  ("montre",14,8,"Pourquoi ça tourne","Chaque accord est à la quinte du précédent. Do vers sol, sol vers ré, ré vers la, la vers mi. Montre-le sur la corde de Mi grave : à chaque fois, on monte de sept cases, ou on descend de cinq.",
    [("Il veut la théorie complète","Non. Une seule idée aujourd'hui : quinte après quinte, ça tire vers l'avant. Le reste attendra.")]),
  ("jeu",22,14,"Les enchaînements","Le passage difficile est D vers A, puis A vers E : trois accords ouverts d'affilée qui se ressemblent. Isole-le.",
    [("Les changements traînent","Deux temps par accord au lieu de quatre, pendant cinq minutes. Puis on revient à quatre : ça paraît facile.")]),
  ("jeu",36,10,"La version barrée","La même grille en formes mobiles, C case 8 et G case 3 sur la corde de Mi grave. C'est là que la séance I paye.",[]),
  ("morceau",46,10,"Le morceau","La grille en boucle, tempo lent. Tu joues la mélodie ou tu chantes, il tient. Puis l'inverse.",[]),
  ("cadre",56,4,"Le mi de la fin","Annonce la séance VIII : le dernier accord de la boucle n'est pas un E ordinaire.",[]),
 ],
 pied=["<b>S'il connaît déjà le morceau :</b> tant mieux, la plupart le jouent de travers. Vérifie qu'il fait bien deux mesures sur le mi et pas une.",
       "<b>Ado en électrique :</b> son clair, ou une saturation légère. La grille est simple, c'est le placement qui compte.",
       "<b>Si les barrés ne passent pas :</b> reste en accords ouverts toute la séance. La version barrée reviendra."],
 ft="Séance VII — la grille de quintes",
 fc=['<h5>La grille</h5><div class="grille"><span>C</span><span>G</span><span>D</span><span>A</span><span>E</span><span>E</span></div>'
     '<p class="cap">Une mesure par case, deux sur le mi, et ça recommence. En français : Do, Sol, Ré, La, Mi.</p>'
     '<h5>Pourquoi ça tourne</h5><p>Chaque accord est à la <b>quinte</b> du précédent.</p>'
     '<pre class="tab">C  →  G  →  D  →  A  →  E\n  +7    +7   +7   +7   cases</pre>',
     '<h5>Les accords</h5><div class="accords"><span class="accord" data-chord="C"></span>'
     '<span class="accord" data-chord="G"></span><span class="accord" data-chord="D"></span>'
     '<span class="accord" data-chord="A"></span><span class="accord" data-chord="E"></span></div>'
     '<h5>En barrés</h5><pre class="tab">C   forme de A, case 3\nG   forme de E, case 3\nD   forme de A, case 5\nA   forme de E, case 5\nE   forme de E, case 12</pre>',
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> La grille à 70, quatre temps par accord. Dis le nom de l\'accord <b>suivant</b> pendant que tu joues le précédent.<br>'
     '<b>2.</b> Isole D → A → E. C\'est le passage qui traîne.<br>'
     '<b>3.</b> Puis deux temps par accord. Puis retour à quatre : ça paraîtra lent.</div>']))

I.append(dict(id="i8", num="VIII", titre="L'accord de Hendrix",
 objectif="E7♯9, qu'on dit « mi sept dièse neuf ». Un accord qui contient sa tierce majeure et sa tierce mineure en même temps — ce qui devrait sonner faux, et qui sonne comme le blues électrique tout entier.",
 steps=[
  ("cadre",0,4,"La grille de la séance VII","En boucle, pour se remettre dedans.",[]),
  ("jeu",4,14,"La forme","Case 7 sur la corde de La pour la fondamentale, puis ré, sol, si. Quatre doigts, quatre cordes, et on n'attaque que celles-là.",
    [("Les cordes de Mi sonnent","Elles n'ont rien à faire là. L'index qui tient la fondamentale s'incline pour étouffer le mi grave ; l'auriculaire couche légèrement pour étouffer le mi aigu."),
     ("L'accord sonne bouché","Les doigts sont à plat. Sur quatre cordes serrées il faut jouer sur la pointe, sinon tout s'étouffe.")]),
  ("montre",18,8,"Ce qu'il y a dedans","Mi, Sol♯, ré, sol. Le Sol♯ est la tierce majeure, le sol la tierce mineure. Les deux ensemble : c'est exactement le frottement de la blue note, mais plaqué dans un accord.",
    [("Il demande pourquoi ça ne sonne pas faux","Parce que le sol est écrit un octave plus haut et joué comme une neuvième. C'est la seule explication à donner aujourd'hui.")]),
  ("jeu",26,12,"Le déplacer","La forme est mobile. Case 5 pour un ré, case 10 pour un sol. La séance I sert encore.",[]),
  ("jeu",38,9,"Le geste rythmique","Cet accord ne se tient pas. Il se plaque, il s'étouffe, il repart. Travaille-le en aller-retour avec la main droite qui ne s'arrête pas — la séance IV sert ici.",
    [("Il le laisse sonner quatre temps","Il devient lourd tout de suite. Court et sec, avec du silence entre.")]),
  ("morceau",47,9,"La grille du solo","E7♯9, puis G, puis A. Trois accords qui tournent, et c'est là-dessus qu'on improvisera à la séance X.",[]),
  ("cadre",56,4,"Devoirs","",[]),
 ],
 pied=["<b>Si l'écartement ne passe pas :</b> il existe une version à trois cordes, sans la fondamentale, que le bassiste ou la corde grave assurent. Mais fais l'effort deux semaines avant de plier.",
       "<b>Sur folk :</b> l'accord existe mais il sonne dur en acoustique. Garde-le pour l'électrique, et remplace-le par un E7 ordinaire si l'élève n'a qu'une folk.",
       "<b>Réglage :</b> une saturation moyenne, pas maximale. Cet accord a besoin qu'on entende ses quatre notes séparément, sinon son intérêt disparaît."],
 ft="Séance VIII — E7♯9",
 fc=['<h5>La forme</h5><div class="accords"><span class="accord" data-chord="E7s9"></span></div>'
     '<pre class="tab">e|--x--|  ne pas jouer\nB|--8--|  Sol   ← la neuvième augmentée\n'
     'G|--7--|  Ré    ← la septième\nD|--6--|  Sol♯  ← la tierce majeure\nA|--7--|  Mi    ← la fondamentale\nE|--x--|  ne pas jouer</pre>',
     '<h5>Ce qu\'il y a dedans</h5><p>Une tierce <b>majeure</b> (Sol♯) et une tierce <b>mineure</b> (sol) dans le même accord. C\'est le frottement de la blue note, plaqué.</p>'
     '<h5>Il est mobile</h5><pre class="tab">case 5   →  D7♯9\ncase 7   →  E7♯9\ncase 10  →  G7♯9</pre>'
     '<p class="cap">La fondamentale est sur la corde de La. Les notes de la séance I servent ici.</p>',
     '<h5>La grille du solo</h5><div class="grille"><span>E7♯9</span><span>G</span><span>A</span></div>'
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> L\'accord seul, corde par corde : les quatre sonnent-elles ?<br>'
     '<b>2.</b> Étouffe les deux cordes de Mi. L\'index s\'incline, l\'auriculaire couche.<br>'
     '<b>3.</b> <b>Court et sec.</b> Plaque, étouffe, repars. Ne le laisse jamais sonner quatre temps.</div>']))

I.append(dict(id="i9", num="IX", titre="Bends, vibrato, harmoniques",
 objectif="Le vocabulaire expressif. Jusqu'ici il joue les bonnes notes ; à partir d'ici il les fait parler. C'est la séance qui change le plus le son sans changer une seule note.",
 steps=[
  ("cadre",0,4,"Réglage","Saturation moyenne. Et montre-lui le bouton de volume de la guitare : c'est la pédale la plus utile qu'il possède déjà.",[]),
  ("jeu",4,12,"Le bend d'un ton","Corde de Sol, case 7, poussée vers le haut jusqu'à sonner comme la case 9. Trois doigts poussent ensemble, le poignet tourne comme une clé.",
    [("Le bend n'arrive pas à la note","Donne-lui la cible : joue la case 9 d'abord, il vise ce son. Un bend se règle à l'oreille, pas à la distance."),
     ("Il pousse avec l'annulaire seul","Le majeur et l'index viennent derrière, sur la même corde. Sinon c'est le tendon qui travaille et ça finit par faire mal.")]),
  ("jeu",16,10,"Le quart de ton","Le petit tiré du blues : on ne monte pas jusqu'à la note suivante, on s'arrête entre les deux. Ça n'existe pas sur un piano, et c'est la moitié du son blues.",
    [("Il monte trop haut","C'est presque rien. Fais-lui viser un quart de la distance du bend d'un ton.")]),
  ("jeu",26,11,"Le vibrato","Il part du poignet, pas du doigt. Petit, régulier, et il commence après la note, pas en même temps.",
    [("Le vibrato tremble au lieu d'osciller","Trop rapide et irrégulier. Fais-lui faire quatre oscillations exactement, au métronome, avant de le laisser libre.")]),
  ("jeu",37,10,"Le slide et l'harmonique pincée","Le slide relie deux notes sans réattaquer. L'harmonique pincée : le pouce de la main droite effleure la corde juste après le médiator.",
    [("L'harmonique ne sort pas","C'est une question de millimètres et de position sur la corde. Fais-lui balayer lentement la zone entre le micro et le chevalet jusqu'à ce que ça crie.")]),
  ("morceau",47,9,"Tout dans une phrase","Une phrase de quatre notes, jouée quatre fois : à plat, puis avec un bend, puis avec le vibrato, puis avec les deux. Même notes, quatre résultats.",[]),
  ("cadre",56,4,"Devoirs","",[]),
 ],
 pied=["<b>Si la corde résiste :</b> regarde le tirant. En 11-49 ou plus, les bends d'un ton sont durs en position basse. Un jeu 10-46 change tout, et ce n'est pas de la triche.",
       "<b>Sur folk :</b> le bend d'un ton est difficile, celui d'un demi-ton passe très bien. Le vibrato et le slide fonctionnent parfaitement.",
       "<b>Ne fais pas les cinq techniques à fond.</b> Le bend d'un ton et le vibrato suffisent pour cette heure. Le reste est montré, pas travaillé."],
 ft="Séance IX — les articulations",
 fc=['<h5>Les gestes</h5><pre class="tab">   ton      1/4 ton   vibrato   slide\nG|--7b(9)--|--7b--|--7~~~--|--5/7--|</pre>'
     '<ul><li><b>b</b> — bend. Trois doigts poussent, le poignet tourne.</li>'
     '<li><b>1/4</b> — le petit tiré blues. On s\'arrête entre les deux notes.</li>'
     '<li><b>~</b> — vibrato. Il part du poignet et commence <b>après</b> la note.</li>'
     '<li><b>/</b> — slide. On ne réattaque pas la seconde note.</li></ul>',
     '<h5>Régler le bend à l\'oreille</h5><pre class="tab">G|--9-----------|  la note cible\nG|--7b(9)-------|  tu vises ce son</pre>'
     '<p class="cap">Joue la cible d\'abord. Un bend se règle à l\'oreille, jamais à la distance.</p>'
     '<h5>L\'harmonique pincée</h5><p class="cap">Le pouce de la main droite effleure la corde juste après le médiator. Balaie lentement la zone entre le micro et le chevalet jusqu\'à ce que ça crie.</p>',
     '<h5>À la maison</h5><div class="devoir"><b>1.</b> Bend d\'un ton case 7 corde de Sol. Vérifie avec la case 9 avant chaque essai.<br>'
     '<b>2.</b> Vibrato : <b>quatre oscillations exactement</b>, au métronome. Ensuite seulement, joue-le librement.<br>'
     '<b>3.</b> Une phrase de quatre notes, jouée à plat / avec bend / avec vibrato / avec les deux.</div>']))

I.append(dict(id="i10", num="X", titre="Improviser sur les changements",
 objectif="Tout ce qui précède, mis ensemble. Une gamme pour toute une grille, puis viser les notes de l'accord qui passe. Et repartir avec trois phrases à soi, enregistrées.",
 steps=[
  ("cadre",0,4,"Rien de neuf","On assemble. Dis-le en arrivant.",[]),
  ("jeu",4,10,"L'échauffement des dix séances","Chromatique en aller-retour, les deux positions de pentatonique, la blue note, un bend réglé à l'oreille. Dix minutes, et c'est sa routine pour la suite.",[]),
  ("jeu",14,12,"Une gamme pour toute la grille","Sur la grille de la séance VII, la pentatonique de Mi mineur passe du début à la fin. Il n'a rien à changer quand les accords bougent.",
    [("Il change de gamme à chaque accord","Pas encore. Une gamme sur toute la grille d'abord ; suivre les accords viendra dans un an.")]),
  ("morceau",26,14,"Suivre quand même l'accord","Une seule chose : sur chaque changement, il vise la fondamentale de l'accord qui arrive, sur le premier temps. Le reste, il fait ce qu'il veut.",
    [("Il arrive en retard sur le changement","Il doit décider de sa note cible une mesure à l'avance. Compte à voix haute les premières fois."),
     ("Il joue sans arrêt","Impose deux mesures de silence sur les douze. Le silence se travaille comme le reste.")]),
  ("morceau",40,12,"Sur la grille du solo","E7♯9, G, A. Plus court, plus dur, plus gratifiant. La gamme blues de la séance III y trouve tout son sens.",[]),
  ("jeu",52,4,"Trois phrases gardées","Il en choisit trois qui lui plaisent et les rejoue à l'identique. Improviser, c'est aussi se constituer un vocabulaire.",[]),
  ("cadre",56,4,"Enregistrement et suite","Une prise complète sur son téléphone, écoutée à deux. Puis la feuille de route.",[]),
 ],
 pied=["<b>Techniquement, ce qui manque après ces dix heures :</b> les deux positions de pentatonique restantes, les accords de septième mineurs et majeurs, le jeu en <b>doubles-cordes</b> — deux notes jouées ensemble au lieu d'une, ce qui remplit le son quand on joue seul — et l'arpège de l'accord plutôt que la gamme, c'est-à-dire viser les notes de l'accord qui passe au lieu de dérouler une gamme par-dessus tout.",
       "<b>Musicalement :</b> jouer sur des grilles qui ne sont pas des blues. C'est le vrai saut suivant, et il est plus grand que tout ce qu'on a fait ici.",
       "<b>Le reste :</b> jouer avec un batteur, ne serait-ce qu'une fois. Une heure avec une batterie apprend plus sur le placement que six mois de métronome."],
 ft="Séance X — improviser",
 fc=['<h5>L\'échauffement à garder</h5><ul><li><b>1.</b> Chromatique en aller-retour strict — 3 min</li>'
     '<li><b>2.</b> Les deux positions de pentatonique, reliées — 3 min</li>'
     '<li><b>3.</b> La blue note, atteinte au bend — 2 min</li>'
     '<li><b>4.</b> Un bend d\'un ton réglé sur la note cible — 2 min</li></ul>',
     '<h5>Les deux grilles</h5><div class="grille"><span>C</span><span>G</span><span>D</span><span>A</span><span>E</span><span>E</span></div>'
     '<p class="cap">Pentatonique de <b>mi mineur</b> du début à la fin. Ne change pas de gamme quand l\'accord change.</p>'
     '<div class="grille" style="margin-top:12px"><span>E7♯9</span><span>G</span><span>A</span></div>'
     '<p class="cap">Plus court, plus dur. La gamme blues y trouve son sens.</p>',
     '<h5>Les deux consignes</h5><div class="devoir"><b>1.</b> Sur chaque changement d\'accord, vise la <b>fondamentale</b> sur le premier temps. Décide-la une mesure à l\'avance.<br><br>'
     '<b>2.</b> <b>Deux mesures de silence</b> sur douze. Le silence se travaille comme le reste.<br><br>'
     '<b>3.</b> Enregistre une prise entière. Garde <b>trois phrases</b> et rejoue-les à l\'identique : c\'est ton vocabulaire.</div>']))

RECAP_I = [
 ("I","<b>Les notes du manche</b>, tons et demi-tons","—","Poser un barré sur un accord annoncé","Trouver une note sur mi et sur la"),
 ("II","<b>Pentatonique positions V et VIII</b>","—","Impro blues en changeant de position","Monter en V, descendre en VIII sans trou"),
 ("III","<b>La blue note</b> (Mi♭), atteinte au bend","—","Blues en la, deux blue notes maximum","Le bend d'un demi-ton, juste"),
 ("IV","Rien à la main gauche","<b>Aller-retour strict, mouvement perpétuel</b>","Un riff connu, rejoué en aller-retour","Le tempo où le chromatique reste propre"),
 ("V","<b>Accords de sixte</b> A6 G6 D6 C6 E6","Le shuffle à ♩=100","La grille de douze mesures, accompagnée","La grille entière sans s'arrêter"),
 ("VI","<b>Le turnaround</b> descendant","Une position par temps","Douze mesures, trois fois d'affilée","Le nombre d'arrêts. Objectif zéro"),
 ("VII","<b>La grille de quintes</b> C G D A E","—","« Hey Joe », en ouvert puis en barrés","Cinq accords en boucle sans se perdre"),
 ("VIII","<b>E7♯9</b>, l'accord de Hendrix","Court et sec, jamais tenu","La grille E7♯9 – G – A","Quatre cordes qui sonnent, deux étouffées"),
 ("IX","<b>Bend, quart de ton, vibrato, slide</b>","Le poignet, pas le doigt","Une phrase jouée de quatre façons","Un bend d'un ton réglé à l'oreille"),
 ("X","Rien, on assemble","L'échauffement à garder","Impro sur les deux grilles, enregistrée","<b>Deux mesures de silence sur douze</b>"),
]

INTRO_I = '''<section class="intro" id="avant">
 <div class="wrap">
  <div class="lede-bloc">
    <p class="lede">Ce volet commence exactement là où l'autre s'arrête.</p>
    <div>
      <p class="lede-sous">À l'entrée : il tient ses accords ouverts, il connaît une grille de blues, il a une boîte de pentatonique sous les doigts et son barré sonne à peu près. À la sortie : il nomme les notes du manche, il relie trois positions de gamme, il accompagne un blues autrement qu'en grattant, et il improvise sur deux grilles.</p>
      <p class="lede-sous">Même format que le volet débutant : une heure, minutée, les problèmes accrochés à la minute où ils arrivent, et une feuille détachable à donner en partant. Ce qui change, c'est que l'élève sait maintenant travailler seul — donc les séances demandent plus entre deux cours qu'elles n'en donnent pendant.</p>
    </div>
  </div>

  <h3 class="h-sec">Ce qu'il faut avoir avant de commencer</h3>
  <div class="paire">
    <div class="p-col">
      <h4>Acquis attendus</h4>
      <ul>
        <li>Les accords ouverts enchaînés sans regarder, en rythme.</li>
        <li>La grille de blues en douze mesures, tenue jusqu'au bout sans se perdre.</li>
        <li>Une position de pentatonique, même approximative.</li>
        <li>Un barré qui sonne sur au moins quatre cordes.</li>
        <li>Une pratique régulière : dix minutes par jour tenues depuis quelques mois.</li>
      </ul>
    </div>
    <div class="p-col">
      <h4>Ce qui change dans le rythme</h4>
      <ul>
        <li>Une séance peut prendre deux ou trois cours. C'est normal, et c'est même souhaitable sur les séances IV et V.</li>
        <li>Le travail à la maison devient le vrai moteur. Sans cinq minutes quotidiennes de métronome, la séance IV ne sert à rien.</li>
        <li>On chronomètre toujours, mais on chronomètre autre chose : un tempo, un nombre d'arrêts, un nombre de cordes qui sonnent.</li>
        <li>L'électrique devient utile. Sur folk tout reste jouable, sauf E7♯9 qui sonne dur.</li>
      </ul>
    </div>
  </div>

  <h3 class="h-sec">D'où vient ce volet</h3>
  <div class="paire">
    <div class="p-col">
      <h4>Les feuilles de cours</h4>
      <ul>
        <li>La feuille manuscrite de théorie : structure ton / demi-ton de la gamme, dièses et bémols, et les positions de pentatonique reliées aux cases V, VIII et XII. Elle donne les séances I, II et X.</li>
        <li>La feuille de tablatures : pentatonique de La mineur, gamme blues, grille de « Hey Joe », et l'exercice chromatique de main droite noté « mouvement perpétuel ». Elle donne les séances III, IV et VII.</li>
      </ul>
    </div>
    <div class="p-col">
      <h4>Les partitions de travail</h4>
      <ul>
        <li>L'arrangement de blues en accords de sixte, ♩=100 en shuffle, avec sa basse qui marche et son turnaround. Il donne les séances V et VI.</li>
        <li>La transcription de « Purple Haze » : accord E7♯9, slides, quarts de ton, bends, harmoniques pincées, et la grille du solo notée à la main en bas de page. Elle donne les séances VIII et IX.</li>
        <li><em>Les tablatures de ces deux partitions ne sont pas reproduites ici : elles sont protégées. Ce volet en enseigne les techniques avec ses propres exercices, et donne les grilles d'accords, qui ne le sont pas.</em></li>
      </ul>
    </div>
  </div>
 </div>
</section>'''

def bloc_seance(s):
    o = ['<section class="seance" id="%s">\n <div class="wrap">' % s["id"]]
    o.append('  <header class="s-head"><div class="s-num">%s</div>'
             '<div class="s-titre"><h2>%s</h2><p class="objectif">%s</p></div>'
             '<div class="s-meta"><span class="m-lab">Guitare en main</span><span class="m-val">—</span></div></header>'
             % (s["num"], s["titre"], s["objectif"]))
    o.append('  <div class="heure">')
    for (typ, frm, dur, h4, txt, notes) in s["steps"]:
        o.append('   <div class="etape" data-type="%s" data-dur="%d" style="--dur:%d">' % (typ, dur, dur))
        o.append('    <div class="tick"><span>%d</span></div>' % frm)
        o.append('    <div class="corps"><h4>%s</h4><p>%s</p></div>' % (h4, txt))
        o.append('    <div class="marge">' + ''.join(
            '<div class="note"><b>%s</b>%s</div>' % (b, f) for (b, f) in notes) + '</div>')
        o.append('   </div>')
    o.append('   <div class="fin-heure"><div class="tick"><span>60</span></div><div></div></div>')
    o.append('  </div>')
    o.append('  <div class="s-pied"><div class="p-lab">Si ça ne se passe pas comme prévu</div>'
             '<div class="p-body">' + ''.join('<p>%s</p>' % p for p in s["pied"]) + '</div></div>')
    o.append('  <div class="feuille">')
    o.append('   <div class="f-cut"><span>à détacher</span></div>')
    o.append('   <div class="f-head"><span class="f-lab">Feuille élève</span><span class="f-t">%s</span>'
             '<button class="f-print" type="button">Exporter cette feuille en PDF</button></div>' % s["ft"])
    o.append('   <div class="f-cols">' + ''.join('<div class="f-col">%s</div>' % c for c in s["fc"]) + '</div>')
    o.append('  </div>')
    o.append(' </div>\n</section>')
    return '\n'.join(o)

def bloc_recap(lignes, titre, chapo):
    LBL = [None, "Ce qu'on ajoute", "Main droite", "Le morceau", "Ce qu'on chronomètre"]
    o = ['<section class="recap-sec" id="recap"><div class="wrap">']
    o.append('<header class="s-head"><div class="s-num">&#8635;</div>'
             '<div class="s-titre"><h2>%s</h2><p class="objectif">%s</p></div>'
             '<div class="s-meta"></div></header>' % (titre, chapo))
    o.append('<div class="tablewrap"><table class="recap"><thead><tr>'
             '<th>N°</th><th>Ce qu\'on ajoute</th><th>Main droite</th><th>Le morceau</th>'
             '<th>Ce qu\'on chronomètre</th></tr></thead><tbody>')
    for r in lignes:
        tds = []
        for i, c in enumerate(r):
            tds.append('<td>%s</td>' % c if LBL[i] is None else '<td data-label="%s">%s</td>' % (LBL[i], c))
        o.append('<tr>' + ''.join(tds) + '</tr>')
    o.append('</tbody></table></div></div></section>')
    return '\n'.join(o)

# --- feuille de correspondance, en tête des deux volets ---
FEUILLE_ZERO = '''<section class="reference" id="notes">
 <div class="wrap">
  <div class="feuille">
   <div class="f-cut"><span>à détacher</span></div>
   <div class="f-head"><span class="f-lab">À envoyer avant le premier cours</span>
    <span class="f-t">Notes et accords — la correspondance</span>
    <button class="f-print" type="button">Exporter cette feuille en PDF</button></div>
   <div class="f-cols">
    <div class="f-col">
     <h5>Les sept notes</h5>
     <pre class="tab">français   Do  Ré  Mi  Fa  Sol  La  Si
anglais     C   D   E   F   G    A   B</pre>
     <p class="cap">Do commence à C, puis on avance dans l\'alphabet. Il n\'y a rien d\'autre à retenir.</p>
     <h5>Les altérations</h5>
     <pre class="tab">Do♯ = C♯      Ré♭ = D♭
Ré♯ = D♯      Mi♭ = E♭
Fa♯ = F♯      Sol♭ = G♭
Sol♯ = G♯     La♭ = A♭
La♯ = A♯      Si♭ = B♭</pre>
     <p class="cap">♯ dièse : une case plus haut. ♭ bémol : une case plus bas. La même case porte les deux noms.</p>
     <p class="cap"><b>Attention :</b> entre Mi et Fa, et entre Si et Do, il n\'y a pas de case intermédiaire. Ce sont les deux seuls endroits.</p>
    </div>
    <div class="f-col">
     <h5>Les six cordes à vide</h5>
     <pre class="tab">6e  la plus grosse   Mi    E
5e                   La    A
4e                   Ré    D
3e                   Sol   G
2e                   Si    B
1re la plus fine     Mi    E</pre>
     <h5>Comment se dit un nom d\'accord</h5>
     <pre class="tab">écrit       on dit
C           « do »
Cm          « do mineur »
C7          « do sept »
Cmaj7       « do majeur sept »
Csus4       « do sus quatre »
Cadd9       « do add neuf »
C6          « do six »
E7♯9        « mi sept dièse neuf »
C♯          « do dièse »
D♭          « ré bémol »</pre>
     <p class="cap">La lettre donne la note de départ, ce qui suit décrit la couleur de l\'accord. Une lettre seule veut toujours dire majeur.</p>
     <p class="cap"><b>On écrit la lettre anglaise, on dit la note française.</b> Tout le monde écrit C7 et dit « do sept ». À l\'oral on abrège : « sept », pas « septième ».</p>
    </div>
    <div class="f-col">
     <h5>Tous les accords des vingt séances</h5>
     <pre class="tab">Em      Mi mineur
Am      La mineur
Dm      Ré mineur
Bm      Si mineur

C       Do majeur
D       Ré majeur
E       Mi majeur
G       Sol majeur
A       La majeur
F       Fa majeur

A7      La septième
D7      Ré septième
E7      Mi septième
Cadd9   Do add9

A6 G6   La et Sol sixte
D6 C6   Ré et Do sixte
E6      Mi sixte
E7♯9    Mi septième dièse neuf</pre>
     <div class="devoir">Sur tout le site, <b>les accords sont écrits en lettres</b>, comme sur les tablatures que tu trouveras partout. <b>Les notes et les cordes restent en français.</b> C\'est la seule convention à connaître, et c\'est celle de la quasi-totalité des guitaristes.</div>
    </div>
   </div>
  </div>
 </div>
</section>'''

VOLETS = [("index.html", "debutant", "Volet 1", "Débutant"),
          ("intermediaire.html", "intermediaire", "Volet 2", "Intermédiaire")]

def page(fichier, volet, titre, sous_titre, bandeau, intro, seances, recap, ids, desc):
    nav = ['<nav class="nav" aria-label="Séances"><div class="wrap">'
           '<span class="navlabel">Sommaire</span>'
           '<a href="#notes">Notes &amp; accords</a><a href="#avant">Avant</a>']
    for num, ident in ids:
        nav.append('<a href="#%s">%s</a>' % (ident, num))
    nav.append('<a href="#recap">Récap</a></div></nav>')

    onglets = ['<nav class="volets" aria-label="Volets">']
    for f, v, lab, nom in VOLETS:
        cur = ' aria-current="page"' if v == volet else ''
        onglets.append('<a class="volet" href="%s"%s><span class="v-lab">%s</span>'
                       '<span class="v-nom">%s</span></a>' % (f, cur, lab, nom))
    onglets.append('</nav>')

    html = '''<!doctype html>
<html lang="fr" data-volet="%(volet)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(titre)s</title>
<meta name="description" content="%(desc)s">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Guitare">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#F4F8F6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B1210" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="%(titre)s">
<meta property="og:description" content="%(desc)s">
<link rel="stylesheet" href="assets.css">
</head>
<body>
<header class="masthead">
  <div class="wrap">
    <p class="kicker">Méthode de guitare — cours particulier — tablature</p>
    <h1>%(titre)s</h1>
    <p class="sub">%(sous)s</p>
    %(onglets)s
  </div>
</header>
<div class="mast-strip"><div class="wrap">%(bandeau)s</div></div>
%(nav)s
<main>
%(zero)s
%(intro)s
%(seances)s
%(recap)s
</main>
<footer><div class="wrap">
  <span>Volet %(volet_lab)s. Guitare folk ou électrique, cours individuel.</span>
  <span>Les tablatures des morceaux cités ne sont pas reproduites : seules les grilles et les exercices le sont.</span>
</div></footer>
<script src="app.js"></script>
</body>
</html>
''' % dict(volet=volet, titre=titre, sous=sous_titre, desc=desc, onglets='\n    '.join(onglets),
           bandeau=bandeau, nav='\n'.join(nav), intro=intro, seances=seances, recap=recap,
           zero=FEUILLE_ZERO,
           volet_lab=("1 sur 2 — débutant" if volet == "debutant" else "2 sur 2 — intermédiaire"))
    io.open(os.path.join(R, '..', fichier), 'w', encoding='utf-8').write(html)
    return len(html)

BANDEAU_D = ('<div class="cell"><b>Pour qui</b>Ados et adultes qui n\'ont jamais touché une guitare. '
             'Folk ou électrique, les deux sont prévus.</div>'
             '<div class="cell"><b>Comment ça se lit</b>L\'heure descend en colonne. Les problèmes sont '
             'accrochés dans la marge, à la minute où ils arrivent.</div>'
             '<div class="cell"><b>La feuille du bas</b>Elle se détache, s\'exporte en PDF et se donne '
             'à l\'élève en partant.</div>')
BANDEAU_I = ('<div class="cell"><b>Pour qui</b>Un élève qui a fini le premier volet, ou qui joue depuis '
             'six mois à deux ans sans avoir jamais nommé une note.</div>'
             '<div class="cell"><b>Ce qui change</b>Le travail à la maison devient le moteur. Une séance '
             'peut tenir sur deux ou trois cours.</div>'
             '<div class="cell"><b>D\'où ça vient</b>De feuilles de cours manuscrites et de deux '
             'partitions de travail. Le détail est plus bas.</div>')

# --- volet débutant : contenu existant, préservé ---
seances_d = lire('debutant-seances.html')
recap_d = lire('debutant-recap.html').replace(' style="color:var(--brass)"', '')
ids_d = [(m.group(1), m.group(2)) for m in
         re.finditer(r'<section class="seance" id="(?:(s\d+))">.*?<div class="s-num">(\d+)</div>', seances_d, re.S)]
ids_d = [(num, ident) for ident, num in
         re.findall(r'<section class="seance" id="(s\d+)">\s*<div class="wrap">\s*<header class="s-head"><div class="s-num">(\d+)</div>', seances_d)]

n1 = page('index.html', 'debutant', 'Les dix premières heures',
          "Dix séances d'une heure. De la première prise en main jusqu'à un morceau joué en entier.",
          BANDEAU_D, lire('debutant-intro.html'), seances_d, recap_d, ids_d,
          "Dix séances d'une heure pour démarrer un guitariste débutant : déroulé minuté côté prof, feuille détachable côté élève, tout en tablature.")

# --- volet intermédiaire ---
seances_i = '\n'.join(bloc_seance(s) for s in I)
recap_i = bloc_recap(RECAP_I, "Les dix séances sur une page",
                     "À imprimer et à glisser dans la housse. La colonne de droite change de nature dans ce volet : "
                     "on ne chronomètre plus des changements d'accord, mais un tempo, un nombre d'arrêts, un nombre de cordes qui sonnent.")
ids_i = [(s["num"], s["id"]) for s in I]
n2 = page('intermediaire.html', 'intermediaire', 'Les dix heures suivantes',
          "Le manche nommé, la pentatonique reliée, le blues accompagné, et la première vraie improvisation.",
          BANDEAU_I, INTRO_I, seances_i, recap_i, ids_i,
          "Dix séances d'une heure pour un guitariste qui a passé le stade débutant : notes du manche, positions de gamme, blues en sixtes, E7♯9 et improvisation.")

# --- contrôles ---
for s in I:
    tot = sum(d for (_, _, d, _, _, _) in s["steps"])
    main = sum(d for (t, _, d, _, _, _) in s["steps"] if t in ("jeu", "morceau"))
    assert tot == 60, "séance %s : %d minutes au lieu de 60" % (s["num"], tot)
    print("  séance %-4s %2d min en main   %d notes en marge"
          % (s["num"], main, sum(len(n) for (_, _, _, _, _, n) in s["steps"])))
print()
print("index.html          : %d Ko" % (n1 // 1024))
print("intermediaire.html  : %d Ko" % (n2 // 1024))

# --- feuille de style servie : polices en base64, puis identité ---
_css = lire('fonts.css') + "\n" + lire('style.css')
io.open(os.path.join(R, '..', 'assets.css'), 'w', encoding='utf-8').write(_css)
print("assets.css          : %d Ko" % (len(_css.encode()) // 1024))
