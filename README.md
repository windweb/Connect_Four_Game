# Project description

This project is a demonstration of my understanding of arrays and vectors in the NumPy library and my ability to apply these concepts to a game. The game I created is Connect Four, a classic two-player game in which players take turns throwing colored checkers onto the board. The goal of the game is to get four checkers in a row horizontally, vertically, or diagonally before your opponent does.

To implement the game, I used a two-dimensional NumPy array to represent the playing field, with each element representing a place on the field. I also created functions that allow you to throw checkers onto the board, check for correct moves, and check for winning moves.

Overall, this project demonstrates my ability to use NumPy to work with arrays and vectors, and my ability to apply these concepts to create a fun and engaging game. It also demonstrates my problem-solving skills, as I had to think through the logic of the game and create functions to implement it in code.

---
## Detailed description of the game rules

Connect Four is a 2-player game played on a 6x7 board. Each player has checkers corresponding to his letter: player 1 has X and player 2 has O. The goal of Connect Four is to get 4 of your checkers in a row—horizontally, vertically, or diagonally—before your opponent does.

On each turn, a player chooses a column from 0 to 6 to drop their checker into the open slot at the top of that column. The checker will fall to the bottom-most open slot in that column. If the chosen column is already full, the player must choose a different column.

The game ends when one player gets 4 checkers in a row or when all slots are filled, meaning the game ends in a stalemate. If the game ends in a win, the winning player is announced. If the game ends in a stalemate, both players are declared winners.

### Game tips:

- Try to block your opponent's potential winning moves, as well as creating your own potential winning moves.
- Keep an eye on the entire board, not just your own pieces. Look for opportunities to create multiple potential winning moves in different areas of the board.
- Be aware of the different ways to win, including horizontal, vertical, and diagonal lines of four pieces.
- Try to anticipate your opponent's moves and plan your own moves accordingly.
- Remember to have fun and enjoy the game!



---
# Описание проекта

Этот проект - демонстрация моего понимания массивов и векторов в библиотеке NumPy и способности применить эти понятия в игре. Созданная мной игра - Connect Four, классическая игра для двух игроков, в которой игроки по очереди бросают цветные шашки на доску. Цель игры - собрать четыре шашки в ряд по горизонтали, вертикали или диагонали до того, как это сделает ваш противник.

Для реализации игры я использовал двумерный массив NumPy для представления игрового поля, каждый элемент которого представляет место на поле. Я также создал функции, позволяющие бросать шашки на доску, проверять правильность ходов и проверять выигрышные ходы.

В целом, этот проект демонстрирует мое умение использовать NumPy для работы с массивами и векторами, а также способность применять эти понятия для создания веселой и увлекательной игры. Он также демонстрирует мои навыки решения проблем, поскольку мне пришлось продумать логику игры и создать функции для ее реализации в коде.

---
## Подробное описание правил игры

Connect Four - это игра для двух игроков, которая проводится на доске размером 6х7. У каждого игрока есть шашки, соответствующие его букве: у игрока 1 - X, у игрока 2 - O. Цель игры Connect Four - поставить 4 свои шашки в ряд - по горизонтали, вертикали или диагонали - раньше, чем это сделает ваш соперник.

На каждом ходу игрок выбирает столбец от 0 до 6 и опускает свою шашку в открытое гнездо в верхней части столбца. Шашка упадет в самый нижний открытый слот в этой колонке. Если выбранная колонка уже заполнена, игрок должен выбрать другую колонку.

Игра заканчивается, когда один из игроков получает 4 шашки подряд или когда все слоты заполнены, то есть игра заканчивается в патовой ситуации. Если игра заканчивается победой, объявляется победивший игрок. Если игра заканчивается патовой ситуацией, победителями объявляются оба игрока.

### Игровые советы:

- Старайтесь блокировать потенциальные выигрышные ходы противника, а также создавать свои собственные потенциальные выигрышные ходы.
- Следите за всей доской, а не только за своими фигурами. Ищите возможности для создания нескольких потенциальных выигрышных ходов в различных областях доски.
- Помните о различных способах победы, включая горизонтальные, вертикальные и диагональные линии из четырех фигур.
- Старайтесь предугадывать ходы противника и планировать свои ходы соответствующим образом.
- Не забывайте веселиться и наслаждаться игрой!