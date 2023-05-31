import sys
import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.questions =[
            {"question": "What is the capital of Egypt?", "answer": "cairo"},
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "What is the tallest mountain in the world?", "answer": "paris"},
            {"question": "Which planet is known as the \"Red Planet\"?", "answer": "mars"},
            {"question": "What is the largest ocean on Earth?", "answer": "pacific ocean"},
            {"question": "Which country is famous for the Great Wall?", "answer": "china"},
            {"question": "What is the largest continent by land area?", "answer": "asia"},
            {"question": "Which city is known as the \"Big Apple\"?", "answer": "new york"},
            {"question": "What is the capital city of Australia?", "answer": "canberra"},
            {"question": "What is the currency of Japan?", "answer": "yen"},
            {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
            {"question": "What is the largest country in the world by land area?", "answer": "russia"},
            {"question": "What is the capital city of Canada?", "answer": "ottawa"},
            {"question": "Which country is known for producing the most coffee in the world?", "answer": "brazil"},
            {"question": "Which country is known for its pyramids?", "answer": "egypt"},
            {"question": "What is the executive capital of South Africa?", "answer": "pretoria"},
            {"question": "What is the capital city of Spain?", "answer": "madrid"},
            {"question": "What is the official language of Germany?", "answer": "deutsch"},
            {"question": "What is the official language of Spain?", "answer": "spanish"},
            {"question": "What is the name of the largest moon of Saturn?", "answer": "titan"},
            {"question": "What is the chemical symbol for the element gold?", "answer": "au"},
            {"question": "What is the capital city of South Korea?", "answer": "seoul"},
            {"question": "What is the chemical symbol for the element silver?", "answer": "ag"},
            {"question": "Which country is famous for its ancient ruins of Machu Picchu?", "answer": "peru"},
            {"question": "Which continent is the South Pole located in?", "answer": "antarctica"},
            {"question": "What is the name of the longest river in the world?", "answer": "amazon river"},
            {"question": "What is the name of the ancient civilization that built the Pyramids of Giza?", "answer": "ancient egyptian civilization"},
            {"question": "Who was the first person to step foot on the moon?", "answer": "neil armstrong"},
            {"question": "Which country is known as the \"Land of the Rising Sun\"?", "answer": "japan"},
            {"question": "Who painted the Mona Lisa?", "answer": " leonardo da vinci"},
            # Add more questions here
        ]
        self.current_question = 0
        self.score = 0

    def check_answer(self, answer):
        if answer.lower() == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_text = self.questions[self.current_question]["question"]
            question_label.config(text=question_text)
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Game Over", f"Your score: {self.score}/{len(self.questions)}")
        window.destroy()

# Create the main window
window = tk.Tk()
window.geometry("500x300")  # تعديل الأبعاد حسب الحاجة
window.title("Questions Game")
# Create a label for the question
question_label = tk.Label(window, text="Question")
question_label.pack()

# Create an entry field for the answer
answer_entry = tk.Entry(window)
answer_entry.pack()

# Create a button to check the answer
check_button = tk.Button(window, text="Check Answer", command=lambda: game.check_answer(answer_entry.get()))
check_button.pack()

# Create an instance of the Game class
game = Game()

# Start the game by displaying the first question
game.display_question()
def display_question(self):
    if self.current_question < len(self.questions):
        question_text = self.questions[self.current_question]["question"]
        question_label.config(text=question_text, font=("Arial", 25 ))  # تعديل حجم الخط هنا
    else:
        self.show_result()


# Run the main window's event loop
window.mainloop()
