# This program defines and calls two functions

# This function displays the days of the week
def days_of_week():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"]
    for x in days:
        print(x)


# This function replaces the second word of a sentence with hello
def hello(string):
    second_word = string.split(" ")[1]
    new_string = string.replace(second_word, "Hello")
    print(new_string)


days_of_week()
print()
sentence = input("enter a sentence: ")
hello(sentence)
