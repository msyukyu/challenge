# entree

```
f (x, y) | x = nombre lapins, y = nombre lapins par groupe
```

## trivial

si y = {0, 1} le cas est trivial, chaque lapin possede {0, 1} clef et cette clef est unique

## postulats

### 1

si on prend `a` les combinaisons de `y - 1` parmis `x` on a le nombre d'ensembles distincts 2 a 2

```
a = nCr(x, y - 1)
```

### 2

si on prend `b` les combinaisons de y parmis x on a le nombre d'ensembles identiques

```
b = nCr(x, y)
```

### 3

soit `n` le nombre de clefs differentes necessaires pour pouvoir creer au moins `b` dictionnaires differents (dont les clefs sont issues du meme ensemble et les valeurs sont min = `1` et max = `min(y, x - y + 1)`) et la somme totale des valeurs d'un dictionnaire doit etre divisible par `y` (pas certain) et commune entre les dictionnaires (pas certain). Minimum une clef unique dans chaque groupe -> minimum y clefs uniques dans chaque groupe ?

une fois qu'on a au moins `b` dictionnaires differents et `n` , il faut deduire les lapins dans l'ordre alphabetique