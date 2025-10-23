# -*- coding: utf-8 -*-
class Intern:
    """Intern class with a name, ability to make coffee and to 'work'."""

    def __init__(self, name: str = "My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self) -> str:
        return self.Name

    class Coffee:
        """Simple Coffee class whose string representation matches the spec."""

        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Intern.Coffee()


def main():
    # Instantiate twice: once without a name, once with "Mark"
    intern_default = Intern()
    intern_mark = Intern("Mark")

    # Display names
    print(intern_default)
    print(intern_mark)

    # Ask Mark to make coffee and display the result
    coffee = intern_mark.make_coffee()
    print(coffee)

    # Ask the other intern to work and handle the exception
    try:
        intern_default.work()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
