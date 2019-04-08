# ComputorV1

> A simple python script that solves simple polynomial equations. 

The script will take in parameter a polynomial equation and display its solution(s). 
It also parses natural language, that is to say
"4x + 5 - X^2 = 8" is accepted as well as "4 * X^1 + 5 * X^0 - 1 * X^2 = 8 * X^2".

Why polynomials? Because it's one of the simplest and most powerful mathematical tools. It is used in all areas and at all levels to simplify and express many things. For example, the function *sin*, *cos*, and *tans* are calculated using polynomials

## Installation

```bash 
git clone https://github.com/Alhuin/computorV1/
```

### Usage
```bash
python3.7 computor [-h][equation][-d]
          -h print help and usage
          'equation' -d print detailed resolution
```

## Examples

```bash
$ python3.7 computor.py "5X^0 + 4X - 9.3 * X^2 = 1" -d

<span style="color:green">[details]</span> natural parsing :  5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 

Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2

[details] Simplified form : 4X - 9.3X^2 = -4
[details] Calculating discriminant : 4^2 - 4 * -9.3 * 4 = 164.8

Discriminant is strictly positive, the two solutions are:

[details] Calculating solution 1 : (-4 - 164.8^0.5) / -18.6
[details] Calculating solution 2 : (-4 + 164.8^0.5) / -18.6

0.9052389907905898
-0.47513146390886934

$ python3.7 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:-0.25

$ python3.7 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is stricly greater than 2, I can't solve.
```

## License

Copyright © 2019 iomonad
