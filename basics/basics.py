import datetime


class Basics:
    @staticmethod
    def say_hello(name):
        return "Hello {}".format(name)

    @staticmethod
    def string_length(string):
        return len(string)

    @staticmethod
    def print_quote(quote, person):
        return "{} says, \"{}\"".format(person, quote)

    @staticmethod
    def mad_lab(noun, verb, adjective, adverb):
        return "Do you {} your {} {} {}? That's hilarious!".format(verb, adjective, noun, adverb)

    @staticmethod
    def simple_math(first, second):
        return [
            "{} + {} = {}".format(10, 5, int(10 + 5)),
            "{} - {} = {}".format(10, 5, int(10 - 5)),
            "{} * {} = {}".format(10, 5, int(10 * 5)),
            "{} / {} = {}".format(10, 5, int(10 / 5))
        ]

    @staticmethod
    def retirement_calculator(current_age, projected_retirement_age):
        age_difference = projected_retirement_age - current_age
        current_date = datetime.datetime.now().year
        return "You have {} years left. It's {}, so you can retire in {}.".format(
            age_difference, current_date, current_date + age_difference
        )
