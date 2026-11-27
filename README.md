Run a Leitner box on your computer !

A Leitner box is a tool you can use to improve the memorisation of information in long-term memory.
It is a real life tool countaining a set of cards. Each card corresponds to a piece of information you want to memorise. On the front is the question, on the back is the answer.

The cards are stored in different compartments studied with a different frequency. For example :
=> The first compartment corresponds to cards that are studied everyday.
=> The second compartment corresponds to card that are studied every two days.
=> ... every week
=> ... every two weeks
=> every month

For each work session, you take each card in the box you have to study, and read the question. You try to answer. You read the answer. If your answer is correct, you can put the card in the n+1 compartment.
Day after day, week after week, cards will progress in the compartments. Another rule is the following one : if you could not answer, you put the card in the n-1 compartment.
This way, you will work on failed cards more often, and work on the ones you know the answer to a longer time later.

=> Forgotten cards are studied shortly after, the piece of information will slowly enter the medium-term memory.
=> Known cards are studied on a regular basis, allowing the corresponding piece of information to enter the long-term memory after several work sessions.

==========================================================================

My program works with cards priority score, rather than with a time associated with the card.

For each information in a text file is written : a question, an answer, and a score.
Questions are sorted according to their score in the file (the first question has the highest score).

For each work session (and every time you launch the program) questions are prepared to be asked in the order of the file - the order of the score.

1) The terminal asks you the question. You try to answer. What you write is not important for the program itself, but to check you answer for the next step. Press enter.
2) The terminal gives the answer, and asks if you were right. You can then type "y" for yes. The program resets the score of the question to 0. If you type something else, it considers you have failed and adds 1 to the current score of the question. You can also type "exit" to exit the program properly.
3) Next question.

At the end of the work session, the questions are sorted again according to their score. This way, for each work session, you always work first on the questions you failed before.

==========================================================================

How to run on Windows

On Windows, it is preferable to use the exe file (dist folder). A terminal is going to open, allowing the Leitner Box to be used.

==========================================================================

How to run on Linux

Use the .py file with a Python IDE. The program will work in terminal mode.

==========================================================================

Important : the questionsAswers text file.

This file must remain in the same directory than the exe or py file, depending of the one you use.

When you want to add another card to the box, add a line with the following format :
Question/Answer/0/

For example :
Who was the first french president ?/Louis-Napoléon Bonaparte/0/

A score of 0 indicates that this is a new question you don't master yet. The highest priority will be given to cards with a score of 0.
