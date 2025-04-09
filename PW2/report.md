## Réponses qux questions

> Identify and copy the python code that performs the value function adaptation 
> (i.e., the modification of Q-values). Is is the same as the one presented in the 
> lesson ? does it correspond to SARSA or Q-learning ? what is the difference 
> between those learning algorithms ? Explain.

```
new_value = ((1 - alpha) * old_value) + (alpha * (reward + gamma * next_max))
q_table[state, action] = new_value
```

C'est la formule d'adaptation de l'algorithme Q-Learning. La différence entre les algorithmes SARSA et Q-Learning se situe au niveau de la prochaine Q-value qui est prise. SARSA va choisir la Q-Value la plus probable étant donné sa politique alors que Q-Learning va prendre la Q-Value maximale du prochain état.

> Using a 4x4 environment modify the code to stop the learning process every 100
> epochs to evaluate the performance of the agent. To do this, you can run 100
> episodes (Each time the agent is placed in a starting position and tries to reach
> the target. Take note of how many times it reaches the target) while putting
> alpha to zero (no learning) and epsilon to zero (no exploration). Generate a plot
> of the evolution of the performance as a function of interations.

![plot](./plot-rapport.png)

> Modify gamma (the discount factor) to 0.9, and alpha (learning rate) to 0.05 and 
0.01. Compare the resulting plots of performance vs. epochs of the 6 
combinations of hyper-parameters and provide your observations.

Nous avons modifié les paramètres de départ pour effectuer un total de 300 epochs et enregistrer les performances toutes les 5 epochs. Nous avons fait cela car avec 10000 epochs et un enregistrement toutes les 100 epochs, nous ne voyions rien d'intéressant sur les graphiques.

Après avoir généré les 6 graphiques, on observe que les résultats sont très aléatoires. Visiblement, dès que le modèle trouve le chemin, le score devient très élevé et le reste sans vraiment augmenter ou baisser. C'est très "binaire". Cela est en partie dû au fait que l'agent commence toujours dans les mêmes conditions initiales, il y a donc une "bonne solution" très facile à trouver.

> Run a 5x5 environment. Track the learning process to determine the minimum 
number of epochs needed to allow the agent to have a good performance. Can 
it reach a perfect performance ? Is it more rapid that the exhaustive search? 
Explain. 

L'entraînement prend plus de temps mais les résultats sont similaires. Dès que l'agent a trouvé la solution, le score monte à ~90 et reste autour de cette valeur.
Oui l'apprentissage reste quand même beaucoup plus rapide que l'apprentissage par brute-force. Cependant, l'agent n'atteint pas de performance "parfaite" car il y a une certaine part d'exploration, donc un certain aléatoire.

> Try to modify the reward function by providing the agent with a punishment of 
r=-0.1 for each step it takes to try to reach the target instead of giving it a reward 
r=+1 when it reaches the target.

C'est une manière alternative d'entraîner l'agent. Dans tous les cas, il maximise son reward en étant à l'arrivée. Cette approche est peut-être meilleure dans le sens où il a intérêt à y arriver rapidement.

TODO next question



