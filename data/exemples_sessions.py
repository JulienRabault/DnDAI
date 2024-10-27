import attrs


@attrs.define
class DndSession:
    """Class to represent a D&D session."""
    name: str
    summary: str
    session_text: str


# Extended examples with longer transcripts
example_sessions = [
    DndSession(
        name="L'Appel de l'Aventure",
        session_text="""
        **Narrateur**: Une rumeur étrange se propage dans le village de Valdren. Un ancien artefact, connu sous le nom de la Pierre de Lumière, aurait été retrouvé dans les ruines d'un temple oublié. La nuit tombe alors que le groupe se réunit à la taverne locale, le Feu de l'Aube.

        **Thorin (le guerrier nain)**: (tapotant la table) Je vous le dis, mes amis, cette pierre pourrait être la clé pour vaincre les forces du mal. J'ai entendu dire que des cultistes la recherchent aussi.

        **Lia (l'elfe ranger)**: Nous devons nous mettre en route au plus vite. Qui sait quels dangers nous attendent ? (regardant par la fenêtre) Le ciel s'assombrit, et une tempête approche.

        **Mira (la magicienne)**: (feuilletant un ancien grimoire) J'ai trouvé des informations sur ce temple. Il est protégé par des énigmes et des pièges magiques. Nous devrons être prudents.

        **Fendril (le voleur)**: Je suis bon avec les pièges. Laissez-moi faire, et je m'assurerai que nous ne tombons pas dans leurs griffes. (sourire malicieux)

        **Narrateur**: Vous décidez de partir à l'aube, équipés et déterminés. La route vers les ruines est semée d'embûches, mais la promesse d'aventure vous pousse en avant.

        **(Le lendemain matin)**: Vous vous mettez en route. Les arbres de la forêt semblent murmurer des secrets. Au fur et à mesure que vous avancez, un bruit étrange attire votre attention.

        **Thorin**: (fronçant les sourcils) Qu'est-ce que c'était ? On dirait que quelque chose nous suit.

        **Lia**: (tendant l'oreille) Soyez sur vos gardes. Fendril, peux-tu voir ce qui se cache dans les buissons ?

        **Fendril**: (se faufilant avec agilité) Je vais jeter un œil... (quelques instants plus tard) C'est un groupe de gobelins ! Ils semblent vouloir nous attaquer. Préparez-vous à défendre votre vie !

        **Mira**: (brandissant son bâton) Nous ne pouvons pas les laisser nous prendre de court. Préparez-vous au combat !
        """,
        summary="Le groupe se rassemble à la taverne du village de Valdren pour discuter d'une rumeur concernant un ancien artefact, la Pierre de Lumière. Décidés à le récupérer avant les cultistes, ils se mettent en route. En chemin, ils rencontrent des gobelins, ce qui marque le début d'un combat."
    ),
    DndSession(
        name="La Tempête de Glace",
        session_text="""
        **Narrateur**: Vous avez traversé des forêts denses et des vallées profondes pour arriver dans la région glaciale de Gelmir. La tempête fait rage, et les flocons de neige tombent comme des plumes blanches. Soudain, un cri strident résonne à travers la tempête.

        **Lia**: (en plissant les yeux) Qu'est-ce que c'était ? On dirait une voix humaine, mais elle semble être en détresse.

        **Thorin**: Ne perdons pas de temps. Cela pourrait être un piège, mais nous ne pouvons pas laisser quelqu'un souffrir. Allons voir.

        **Mira**: (prenant un moment pour se concentrer) J'utiliserai un sort de lumière pour nous aider à voir à travers la tempête. (elle incante et une lueur éclatante illumine la neige)

        **Fendril**: (avec un sourire) Quelle bonne idée, Mira. Allons-y, je suis prêt à désarmer tous les pièges qu'ils pourraient avoir mis en place.

        **Narrateur**: En suivant le cri, vous arrivez à une petite cabane en bois, battue par les vents. À l'intérieur, vous trouvez une femme liée et gelée par le froid.

        **Lia**: (courant vers elle) Je suis là, je vais te libérer. Qui t'a fait ça ?

        **Femme**: (tremblant) C'est un sorcier fou ! Il a pris mon fils. Je vous en prie, aidez-moi à le retrouver !

        **Thorin**: Nous allons t'aider. Où se trouve ce sorcier ?

        **Femme**: Dans la grotte au sommet de la montagne. Mais il est protégé par des créatures terrifiantes.

        **Mira**: (regardant le groupe) Alors, c'est notre prochaine destination. Nous devons nous préparer à un combat.
        """,
        summary="Dans la région glaciale de Gelmir, le groupe suit un cri strident et découvre une femme en détresse. Elle leur parle d'un sorcier fou qui a kidnappé son fils et se cache dans une grotte, protégée par des créatures. Ils décident de l'aider et se préparent pour une confrontation."
    ),
    DndSession(
        name="Le Labyrinthe des Ombres",
        session_text="""
        **Narrateur**: Après une longue quête, vous arrivez devant les portes massives du Labyrinthe des Ombres, un ancien donjon dont on dit qu'il est hanté par des esprits perdus.

        **Thorin**: Je n'aime pas cet endroit. Les légendes parlent de ceux qui n'en sont jamais sortis.

        **Fendril**: (rire nerveux) Ne soyez pas superstitieux, Thorin. C'est juste un bâtiment en pierre. Nous avons vu pire ensemble.

        **Lia**: (s'approchant de la porte) Soyons prudents. Le labyrinthe peut être plein de pièges et d'illusions. Mira, pourrais-tu utiliser ta magie pour nous guider ?

        **Mira**: Oui, j'ai un sort qui peut nous permettre de voir les passages cachés. (elle commence à incanter, une lumière scintillante émane de ses mains)

        **Narrateur**: À l'intérieur, le labyrinthe est sombre et humide. Des bruits étranges résonnent dans les couloirs, et les murs semblent se mouvoir.

        **Thorin**: (regardant autour) Restez groupés. Je vais prendre la tête, ma hache est prête.

        **Fendril**: Je vais vérifier les murs pour des pièges. (il s'avance prudemment)

        **Mira**: (tenant sa lumière) Les murs semblent avoir des inscriptions anciennes. Elles pourraient nous donner des indices sur la sortie.

        **Lia**: (examinant une inscription) Elle parle d'un cœur de l'ombre. Cela pourrait être l'objet que nous cherchons.

        **Narrateur**: Soudain, une ombre se projette sur le mur, et une silhouette apparaît devant vous.

        **Esprit**: (d'une voix désincarnée) Qui ose troubler mon repos ? Si vous voulez sortir, vous devez répondre à ma question.

        **Thorin**: (se préparant au combat) Que veux-tu savoir, esprit ?
        """,
        summary="Le groupe se rend au Labyrinthe des Ombres, un ancien donjon réputé pour ses dangers. Alors qu'ils avancent, ils rencontrent un esprit qui leur demande de répondre à une énigme pour sortir. Ils doivent également trouver un objet mystérieux connu sous le nom de 'cœur de l'ombre'."
    ),
    DndSession(
        name="Le Mystère du Château Enchanté",
        session_text="""
        **Narrateur**: Vous arrivez au château de Verenthia, enveloppé de brouillard. On dit qu'il est hanté par les âmes des nobles disparus. Les portes grincent en s'ouvrant.

        **Lia**: (regardant autour) Ce château a l'air... sinistre. Est-ce que quelqu'un a déjà vu des fantômes ici ?

        **Thorin**: (soupirant) Les histoires sont peut-être exagérées. Mais soyez prudents, nous devons explorer chaque pièce.

        **Mira**: J'ai un sort de détection magique qui pourrait nous aider à trouver ce qui ne va pas ici. (elle incante et une lueur bleue apparaît)

        **Fendril**: (espiègle) Je vais vérifier les salles à manger. Peut-être qu'il y a des trésors à voler !

        **Narrateur**: En explorant le château, vous découvrez une grande salle de bal où des ombres dansent. Un air mélancolique flotte dans l'air.

        **Lia**: (s'approchant des ombres) Regardez ces âmes. Elles semblent piégées.

        **Mira**: (troublée) Nous devons les libérer. Ils doivent avoir une histoire à raconter.

        **Thorin**: (prenant son arme) Préparez-vous. S'ils sont piégés, cela signifie que quelque chose de maléfique les retient ici.

        **Narrateur**: En s'approchant, les ombres se matérialisent en nobles en pleurs, leurs visages marqués par la douleur.

        **Noble**: (pleurant) Aidez-nous, âmes errantes ! Nous avons été trahis par un sorcier qui a pris possession de ce château. Libérez-nous de ce sort !

        **Fendril**: Que devons-nous faire pour vous aider ?

        **Noble**: Trouvez le cœur du château, la gemme de lumière, et brisez le sort. Elle est gardée par une bête féroce au sous-sol.

        **Mira**: Alors, nous devons aller au sous-sol. Allons-y, mais restons vigilants. Je sens une forte magie ici.
        """,
        summary="Le groupe explore le château de Verenthia, connu pour être hanté. Ils découvrent des âmes de nobles piégées, qui leur demandent de les libérer en détruisant un sort maléfique lié à une gemme de lumière. Ils doivent se rendre au sous-sol pour affronter une bête féroce."
    ),
    DndSession(
        name="Le Secret du Mont Noir",
        session_text="""
        **Narrateur**: Vous gravissez le Mont Noir, une montagne redoutée pour ses tempêtes de neige et ses bêtes sauvages. Alors que vous atteignez le sommet, une silhouette apparaît au loin.

        **Thorin**: (fronçant les sourcils) Qu'est-ce que c'est ? Une silhouette se déplace là-bas.

        **Lia**: Restez sur vos gardes. Cela pourrait être une créature des neiges.

        **Mira**: (murmurant une incantation) Je vais préparer un sort pour nous protéger.

        **Fendril**: (se penchant en avant) Allons voir de plus près. Je suis curieux !

        **Narrateur**: En vous approchant, vous découvrez un groupe de cultistes en train de discuter autour d'un feu. L'un d'eux tient un artefact scintillant.

        **Cultiste**: (en chuchotant) Nous devons terminer le rituel avant qu'ils n'arrivent. La puissance de l'artefact nous appartiendra bientôt !

        **Thorin**: (chuchotant) Nous devons les empêcher d'achever leur rituel. Préparons-nous à attaquer.

        **Mira**: (déterminée) Je vais lancer un sort de feu. Fendril, tu devras les prendre par surprise.

        **Fendril**: Je suis prêt. (s'approchant silencieusement)

        **Narrateur**: En un éclair, Mira lance son sort, et une boule de feu éclate, illuminant la nuit. Les cultistes poussent des cris de surprise.

        **Lia**: (sautant dans la mêlée) Pour Valdren ! Nous ne vous laisserons pas faire !

        **Thorin**: (frappant avec sa hache) Faites attention, ils sont nombreux !
        """,
        summary="Le groupe monte le Mont Noir, où ils rencontrent des cultistes menant un rituel autour d'un artefact mystérieux. Pour empêcher le rituel de se terminer, Mira lance un sort de feu pour prendre les cultistes par surprise, tandis que le groupe se prépare au combat."
    )
]

if __name__ == "__main__":
    for session in example_sessions:
        print(f"Session Name: {session.name}")
        print("Session Text:")
        print(session.session_text)
        print("Summary:")
        print(session.summary)
        print("\n" + "-" * 80 + "\n")
