# PW3 - Rémi Ancay - Lucas Charbonnier - MIN 2025
Ce rapport répond aux questions posées dans le pdf de données du projet. Les notebook sont aussi disponibles

## Réponse aux questions

### Mastermind
>With your code, what would be the chromosome for the sentence "METHINKS IT IS LIKE A WEASEL"?

Avec l'aphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ " (26 lettres + espace), le chromosome pour la phrase "METHINKS IT IS LIKE A WEASEL" est :

*[12 4 19 7 8 13 10 18 26 8 19 26 8 18 26 11 8 10 4 26 0 26 22 4 0 18 4 11]*

### TSP
>Provide the better route you found and the shortest path in kilometers. Is it the optimal shortest path ? explain.

Avec la distance euclidienne, on trouve la meilleure route suivante :
`[9, 10, 8, 7, 12, 6, 11, 5, 4, 3, 2, 13, 1, 0]`

Il n'est pas trivial de savoir si cela correspond à la meilleure tournée car il existe un **très grand nombre de permutations possibles**. Pour 14 villes, il y a précisement *87'178'291'200* de solutions admissibles. Il existe de nombreuses méthodes permettant de trouver une solution proche de l'optimal et il serait possible de trouver la solution optimale pour ce problème spécifique car il n'y a pas beaucoup de villes. Mais dans un cas plus concret avec par exemple 100 ou 500 villes, cela devient pratiquement impossible.

Cela dit, si on dessine le graphe de la tournée, on peut facilement dire si une solution est proche de l'optimal ou non (pas de croisement et pas de raccourci évident visible à vue d'oeil).

Les résultats varient légèrement d'une itération à une autre (étant donné que les algorithmes génétiques ne sont pas déterministes) mais on trouve les résultats suivants :

- Avec la distance euclidienne : 31.2 km
- Avec la distance de haversine : 3452.8 km

On obtient une distance beaucoup plus grande avec la distance de Haversine car on doit prendre en compte le rayon moyen de la terre (~6370 km).

>Describe your fitness function

Pour la fonction de fitness on prend simplement l'inverse de la distance total de la tournée. Ainsi, une petite distance donnera un bon fitness.

>Explain the way you encoded the solution, give a chromosome example.

Une solution admissible au problème du TSP correspond à une **permutation sans doublons** des indices des villes à visiter, dans l'ordre. Voici un exemple de chromosome :

`Chromosome: [13, 8, 5, 11, 12, 10, 6, 3, 1, 4, 7, 0, 9, 2]`

>Provide the configuration of the GA you finally used to find your better results: mutation, crossover, population size, type of selection, mutation, crossover used, number of generations. Describe the methodology or experiments performed in order to get your better results.

Nous n'avons pas pris le temps d'ajuster les paramètres car comme dit plus haut, il est assez facile de voir à l'oeil nu si la solution trouvée est proche de l'optimale. Si on disposait de la solution optimale, on pourrait faire une recherche approfondie afin de trouver un ensemble de paramètres minimisant le temps (= nb d'epochs) nécessaire pour arriver à la solution optimale.

Ci-dessous, les paramètres de l'algorithme génétique utilisé :
```py
ga_instance = pygad.GA(
    num_generations=500,
    num_parents_mating=20,
    fitness_func=fitness_func,
    sol_per_pop=50,
    num_genes=NUM_CITIES,
    gene_space=gene_space,
    parent_selection_type="sss",
    keep_parents=5,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10,
    allow_duplicate_genes=False,
    stop_criteria=["saturate_100"]
)
```

>Provide relevant plots of your experiments and explanations. 

Plot de la meilleure tournée euclidienne obtenue (31,23 km):

![alt text](best_tour.png)


### Mona Lisa
>The way you extracted the color palette

>Your parameters N_SHAPES_LIST, N_INDIVIDUAL_LIST

>Your parameters to train the genetic algorithm

>How you define the chromosomes (what are the genes you defined and what they represent)

>Initial image you choosed and the resulting image you obtained

>Fitness plots
