"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   a) Abstraction: Abstraction means that you can use parts of your code without
      needing to understand the details of what it is doing.

   b) Encapsulation: Encapsulation means keeping your code bundled into individual
      sections in order to make it easier to understand.

   c) Polymorphism: Polymorphism makes it possible to interact with various objects
      and get the expected result without having to worry about their types or
      implementations.


2. What is a class?

   A class is a category that objects can belong to. It holds information about what
   kinds of attributes the objects in that class can have and how they can be used
   (ie what methods they have).

3. What is an instance attribute?

   An instance attribute is an attribute that belongs specifically to a single
   object of a class.

4. What is a method?

   A method is a function that belongs to a class. It is meant to be used only on
   objects that belong to that class.

5. What is an instance in object orientation?

   An instance is a distinct occurence of a class that is instantiated at run time.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is something that is assigned to the class, so every instance
   of the class will have the same attribute at instantiation. These are best reserved
   for situations in which you will not be changing the attribute or want a universal
   attribute for all the instances of that class.
   An instance attribute is something assigned specifically to an instance of a class,
   either in the __init__ or elsewhere.
   A good use for a class attribute is one we saw in lab earlier this week; each
   class had an attribute describing what kind of melon order it was: 'international',
   'domestic' or 'government'. This was good as a class attribute because it was
   something that would be true for all instances of that class. On the other hand,
   the number of melons in the order was a better instance attribute. Every order
   would end of having that attribute, but each one had a different value and therefore
   it makes sense that it would be attached to the individual instances.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student class containing first name, last name and address"""

    def __init__(self, first_name, last_name, address):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions and answers for exam questions"""

    def __init__(self, question, answer):

        self.question = question
        self.correct_answer = answer

    def ask_and_evaluate(self):

        response = raw_input(self.question + ' > ').strip().lower()
        return response == self.correct_answer


class Exam(object):
    """Exam class that has various questions and can administer the entire exam"""

    def __init__(self, name):

        self.name = name
        self.questions = []

    def add_question(self, question, answer):

        self.questions.append(Question(question, answer))

    def administer(self):

        correct_responses = 0.0

        # if there are no tests on the exam, return a failing grade
        if len(self.questions) == 0:
            return correct_responses

        for question in self.questions:

            if question.ask_and_evaluate():
                correct_responses += 1

        return correct_responses/len(self.questions)


class Quiz(Exam):
    """Extension of the exam class, doesn't have a score, only Pass/Fail"""

    def administer(self):

        score = super(Quiz, self).administer()
        return score >= 0.5


def take_test(student, exam):
    """"""

    score = exam.administer()
    student.score = score

    print score


def example():
    """Example of creating and taking a test"""

    final_exam = Exam('Final')

    questions = {"What is the capital of Alberta?": "Edmonton",
                 "Who is the author of Python?": "Guido Van Rossum",
                 "Who is Ubermelon's competition?": "Squysh",
                 "What is Balloonicorn's favorite color?": "Sparkles", }

    for question, answer in questions.items():
        final_exam.add_question(question, answer.strip().lower())

    student = Student('Marina', 'Balloonicorn', '20 Hackbright Hill')

    take_test(student, final_exam)


example()
