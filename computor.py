#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import functions as fn

regex_pattern = re.compile("(\-?\s*\d+(?:\.\d+)?)\s*\*\s*X\^(\d+)")
details = False


def compute(line, elements, side):
    if details:
        print("\n\033[0;32m[details]\033[0m natural parsing : " + line + "\n")
    lineSplit = line.split('=')
    if len(lineSplit) == 1:
        fn.error("Mauvaise syntaxe : pas de '='")
    reduced = "Reduced form: "
    detailString = "\n\033[0;32m[details]\033[0m Simplified form : "
    res = 0
    first = True
    detailsFirst = True
    degree = 0
    count = 0

    while side < 2:
        exp = re.findall(regex_pattern, lineSplit[side])
        for i in range(len(exp)):
            pwr = int(exp[i][1].replace(' ', ''))
            num = float(exp[i][0].replace(' ', ''))
            try:
                if elements[pwr] is None:
                    elements[pwr] = 0
                elements[pwr] += num if side == 0 else -num
            except KeyError:
                elements[pwr] = num if side == 0 else -num
        side += 1

    for key, value in elements.items():
        if value is not None:
            if value == 0:
                count += 1
            else:
                if key > degree:
                    degree = key

            if first:
                reduced += fn.strIntFloat(value) + " * X^" + str(key)
                first = False
            else:
                reduced += (" + " + fn.strIntFloat(value) if value >= 0 else " - " + fn.strIntFloat(-value)) + " * X^" + str(key)
            if detailsFirst:
                valueStr = fn.strIntFloat(value)
                if key != 0:
                    detailsFirst = False
            else:
                valueStr = (" + " + fn.strIntFloat(value) if value >= 0 else " - " + fn.strIntFloat(-value))

            if key == 0:
                res -= value
            if key == 1:
                detailString += valueStr + "X"
            if key > 1:
                detailString += valueStr + "X^" + str(key)
        else:
            count += 1
            elements[key] = 0

    print(reduced + " = 0")

    if degree == 0:
        if elements[0] == 0:
            print("This equation accepts all real numbers as solution.")
        else:
            print("This equation has no solution.")
    elif count == len(elements):
        print("This equation accepts all real numbers as solution.")
    else:
        print("Polynomial degree: " + str(degree))
        if degree < 3 and details:
            print(detailString + " = " + fn.strIntFloat(res))

        if degree <= 2:
            b = elements[1]
            c = elements[0]
            if degree == 1:
                if b == 0:
                    fn.error("Division by 0.")
                else:
                    x = -c / b
                    if details:
                        print("\033[0;32m[details]\033[0m X = " + fn.strIntFloat(-c) + "/" + fn.strIntFloat(b) + "\n")
                    print("The solution is:")
                    fn.printSolution(x, -c, b)

            elif degree == 2:
                a = elements[2]
                delta = b * b - 4 * a * c
                if details:
                    print("\033[0;32m[details]\033[0m Calculating discriminant : " + fn.strIntFloat(b) + "^2 - 4 * " +fn.strIntFloat(a)+" * "+fn.strIntFloat(c) + " = " +fn.strIntFloat(delta)+"\n")
                if delta > 0:
                    x1 = (-b - delta ** (0.5)) / (2 * a)
                    x2 = (-b + delta ** (0.5)) / (2 * a)
                    print("Discriminant is strictly positive, the two solutions are:")
                    if details:
                        print("\n\033[0;32m[details]\033[0m Calculating solution 1 : ("+fn.strIntFloat(-b)+" - "+fn.strIntFloat(delta)+"^0.5) / "+fn.strIntFloat(2 * a))
                        print("\033[0;32m[details]\033[0m Calculating solution 2 : ("+fn.strIntFloat(-b)+" + "+fn.strIntFloat(delta)+ "^0.5) / "+fn.strIntFloat(2 * a)+"\n")
                    fn.printSolution(x1, (-b - delta ** (0.5)), (2 * a))
                    fn.printSolution(x2, (-b + delta ** (0.5)), (2 * a))

                elif delta < 0:
                    print("The discriminant is strictly negative, the equation has no real solution, only 2 complex solutions:")
                    print("("+fn.strIntFloat(-b)+" − i√"+fn.strIntFloat(-delta)+") / "+fn.strIntFloat(2 * a))
                    print("("+fn.strIntFloat(-b)+" + i√"+fn.strIntFloat(-delta)+") / "+fn.strIntFloat(2 * a))

                else:
                    if a == 0:
                        fn.error("Division by 0.")
                    x = -b / (2 * a)
                    print("The discriminant is 0, the equation has one solution:")
                    if details:
                        print("\033[0;32m\n[details]\033[0m Calculating solution : " + fn.strIntFloat(-b) + "/" + fn.strIntFloat(2 * a)+"\n")
                    fn.printSolution(x, -b, c)
        else:
            print("The polynomial degree is strictly greater than 2, I can't solve.")


def read_in():
    global details
    nbArgs = len(sys.argv)
    if nbArgs > 1:
        line = sys.argv[1]
        if nbArgs > 2 and sys.argv[2] == "-d":
                details = True
    elif not sys.stdin.isatty():
        line = sys.stdin.readline()
    else:
        line = ""
    return line.replace('\n', '')


def main():
    line = read_in()
    if len(line) == 0:
        fn.error("Empty input.")
    elif line == "-h":
        print("Usage : python computor.py [-h][equation][-d]")
        print("python computor.py -h : Print usage and options")
        print("python computor.py [equation] -d : Print detailed resolution")
    elif line == "-d":
        print("Enter an equation to see the detailed resolution. see -h for help")
    else:
        elements = {0: None, 1: None, 2: None}
        compute(fn.formatLine(line), elements, 0)


main()
