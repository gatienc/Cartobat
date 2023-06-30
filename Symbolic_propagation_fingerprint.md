# Symbolic propagation fingerprint

## Description

Cette idée de méthode provient du fait que les murs sont des éléments absorbant pour le signal, ils sont donc à prendre en compte dans la modélisation de la propagation du signal.
Malheureusement, l'absorption du signal par un mur dépend de sa composition, de son épaisseur, de sa longueur, de sa hauteur, de sa position dans le batiment, etc. Il ne serait pas souhaitable d'avoir à remplir tout ces paramètres avant l'implémentation de CartoBat dans le batîment.
L'idée serait donc de remplacer le modèle de propagation par un modèle obtenu en pratique avec une méthode de type fingerprinting.

En se plaçant d'une salle à une autre on suppose que le signal est atténué par les murs. On peut donc mesurer l'intensité du signal reçu en fonction de la salle pour chaque CartoModule.

## Manipulation

Pour évaluer la méthode, on a réalisé une manipulation dans le bâtiment 4A. Consistant à réaliser des mesures de signal reçu en fonction de chaque salle. Pour cela, on s'est déplacé de salle en salle en restant au minimum 5 minutes dans chaque salle. Le CartoTag sera porté au-dessus de la tête ce qui permettra de limiter l'absorption du signal par le corps du porteur. Le porteur du CartoTag se déplacera au sein de la pièce ce qui permettra d'avoir une représentation de l'absorption pour l'ensemble de la pièce et pas seulement de la position à laquelle le porteur est resté.

## Résultats obtenus
 
Pour le CartoModule : A8032A311F6A placé en 4A435, on obtient les résultats suivants :

![représentation en boîte à moustache du signal reçue en fonction de la salle.](output/RoomComparison.png "représentation en boîte à moustache du signal reçue en fonction de la salle")

On remarque que les 1er et 3ème quartiles permettent de différencier certaines salles. Bien que certaines salles pourraient s'avérer difficiles à différencier (par exemple la salle de l'ascenseur et la 4A346) il faudra donc corréler les résultats obtenus avec d'autres CartoModules pour obtenir une localisation précise.

De plus, on remarque de nombreux outliers. Il faudra donc réaliser la mesure de positions à l'aide de plusieurs mesures reçues par les CartoModule.

## Utilisation

 A l'aide des données mesurées, si la moyenne des n dernières intensités reçues appartient au box plot d'une salle (entre le premier et le troisième quartile), alors on peut en déduire que le CartoTag peut se trouver dans cette salle. On réalise cela pour l'ensemble des CartoModules. On obtient donc une carte avec les salles possibles selon chaque CartoModule. On peut ensuite choisir la salle la plus probable, comme la salle ayant le plus d'intersection entre les salles possibles de chaque CartoModule.

 ![Visualisation du choix de salle](output/map.png "Visualisation du choix de salle")

Les zones hachurées sont les zones possibles pour le CartoModule ayant la couleur correspondante à la couleur de la zone hachurée.

 ## Problèmes à prévoir 

 La manière de porter le CartoTag peut influencer les résultats. En effet, si le CartoTag est porté dans la poche, il y aura une absorption du signal par la poche. D'après une première manipulation, il semble que l'absorption soit comme attendu de quelques dB. Il faudrait donc trouver un moyen de prendre cela en compte dans le modèle.

Une première approche serait de corriger la perte de signal par la poche en ajoutant un offset à la mesure de signal reçue. Cependant, il faudrait évaluer cet offset ce qui pourrait être compliqué. La première approche consiste à recalibrer l'offset à chaque fois que le porteur est proche d'un CartoModule. Cela pourrait cependant être compliqué à mettre en place.

Une deuxième approche qui pourrait être utilisée dans un cas où le nombre de CartoModule est grand (similaire à la situation de Palaiseau) serait de réaliser, au moment de la sélection de la salle, la sélection globale de la salle de manière itérative en ajoutant plus de décibel sur l'ensemble des mesures des CartoModules. Sur l'ensemble des salles, celle ayant le plus d'intersection et de proximité avec les valeurs de calibrage devrait être la salle la plus probable.

## Résultat obtenus:

en se plaçant dans les mêmes conditions que la manipulation précédente, i.e règle portant le CartoTag au dessus de la tête.

en analysant le résultat [résultat](output/spfmap.html)

je me suis dis qu'il y avait un truc à faire pour coupler le résultat obtenus avec la WC localization. (Car quand on reçoit fort on sait qu'on est proche d'un récepteur) alors que quand on reçoit faiblement on sait pas (peut être loin ou peut être absorbé par un aléa)