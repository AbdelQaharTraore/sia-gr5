# sia-gr5

# les architectures comportementales des Systèmes Intelligents Autonomes

### Abdel-Qahar Traore (SI5-IAID)

### Sana DIBE (SI5-IAID)

## Partie 1 du rendu

### Explication du choix d’architecture et la procédure d’installation de notre démo:

Dans l’implémentation que nous avons fourni, notre robot Khepera2 utilise un contrôleur Braitenberg. Il utilise la bibliothèque "controller" de Webots pour contrôler le robot.
Lors de l'initialisation, nous configurons les moteurs des roues et les capteurs de lumière et de distance. Les valeurs des capteurs sont lues à chaque tour de boucle, puis le comportement du robot est déterminé en utilisant ces valeurs.
Le comportement est basé sur la logique Braitenberg, qui consiste à contrôler la vitesse des moteurs en fonction des valeurs des capteurs de lumière. Le code utilise également des valeurs des capteurs de distance pour éviter les obstacles.
La vitesse des moteurs gauche et droit est déterminée par la somme des valeurs des capteurs, qui sont pondérées en fonction de leur emplacement sur le robot. La vitesse est ensuite limitée à une vitesse maximale définie, et les vitesses des moteurs sont définies en conséquence.
Le code se poursuit en boucle jusqu'à ce qu'une valeur négative soit obtenue, indiquant que la simulation est terminée.

En termes d'architecture, nous avons adopté une approche de "subsumption", ce qui signifie que les comportements de détection de la source lumineuse (ConstructionLamp) et d'évitement des obstacles (3 CardboardBoxes) sont implémentés de manière séparée, mais hiérarchisés en termes de priorité. Dans notre cas, le comportement d'évitement des obstacles est prioritaire sur le comportement de détection de la source lumineuse, ce qui se reflète dans le code où la vitesse des roues est modifiée en fonction de la détection d'un obstacle, même si une source lumineuse est détectée en même temps.

Pour lancer la démonstration de notre solution, vous devez d'abord ouvrir le logiciel Webots. Une fois Webots ouvert, accédez au menu "File" et sélectionnez "Open World " . Vous devrez alors sélectionner le fichier "V1/worlds/gr5.wbt". Une fois ce fichier sélectionné, vous pouvez lancer la simulation en appuyant sur le bouton "Run the simulation as fast as possible" en haut de la fenêtre. Ce bouton permet de lancer la simulation aussi rapidement que possible. Avec ces étapes simples, vous pouvez maintenant voir la démonstration de notre solution en action.

Nb: Le détecteur de source lumineuse ne fonctionne pas correctement. Nous avons rencontré des problèmes avec les capteurs de lumière, ce qui nous a pris beaucoup de temps. Nous obtenons toujours des valeurs proches de 10, même après avoir essayé les solutions trouvées sur internet.

## Partie 2 du rendu

Dans cette seconde partie nous avons essayé d'implémenter une architecture logicielle basée sur les micro-services en utilisant Docker. Cela implique l'utilisation d'un serveur Webots et le containerisation de chaque comportement ainsi que du mécanisme de coordination. L'objectif étant de fournir une solution flexible et scalable pour les systèmes complexes.
Les micro-services permettent de diviser l'application en plusieurs parties plus petites et indépendantes qui peuvent être développées, déployées et gérées de manière distincte.

Pour cela, nous avons alors séparer notre solution en trois conteneurs : coordination_container, obstacle_avoidance_container et seeking_light_container.

coordination_container a les fichiers suivants :

- coordination.py : un script Python qui contient le code pour la composante de coordination de notre solution.
- Dockerfile : un fichier qui contient les instructions pour construire une image Docker pour le coordination_container.
- docker-compose.yml : un fichier YAML qui définit la configuration pour le service coordination_container lors de l'utilisation de Docker Compose.

obstacle_avoidance_container a les fichiers suivants :

- obstacle_avoidance.py : un script Python qui contient le code pour la composante d'évitement d'obstacles de notre solution.
- Dockerfile : un fichier qui contient les instructions pour construire une image Docker pour le obstacle_avoidance_container.
- docker-compose.yml : un fichier YAML qui définit la configuration pour le service obstacle_avoidance_container lors de l'utilisation de Docker Compose.

seeking_light_container a les fichiers suivants :

- light_seeker.py : un script Python qui contient le code pour la composante de recherche de lumière de notre solution.
- Dockerfile : un fichier qui contient les instructions pour construire une image Docker pour le seeking_light_container.
- docker-compose.yml : un fichier YAML qui définit la configuration pour le service seeking_light_container lors de l'utilisation de Docker Compose.

Nous avons conçu cette architecture, nous n'avons pas encore pu la tester en raison de contraintes de temps. Cependant, nous avons déjà une idée de la façon dont cela devrait fonctionner.
