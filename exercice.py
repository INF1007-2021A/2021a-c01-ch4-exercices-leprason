#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string) % 2 == 0:
        x=1
        return x



def remove_third_char(string: str) -> str:
    x=""
    for i in range(len(string)):
        if i != 2:
            x += string[i]

    return x


def replace_char(string: str, old_char: str, new_char: str) -> str:
    x=""
    for i in range(len(string)):
        if i != 6:
            x+=string[i]
        else:
            x+="z"
    return x


def get_number_of_char(string: str, char: str) -> int:
    x=0
    for i in range(len(string)):
        if ord(string[i])==108:
            x+=1
    return x


def get_number_of_words(sentence: str, word: str) -> int:
    x = 0
    for i in range(len(sentence)):
        if ord(sentence[i]) == 100:
            if ord(sentence[i+1])==111:
                if ord(sentence[i+2])==111:
                    x+=1
    return x


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world! est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
