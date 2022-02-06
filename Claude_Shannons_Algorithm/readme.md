## ** Claude Shannon's Algorithm **

This algorithm is a simple mind reading algorithm. It will predict a players next move (0 or 1) based on their previous two inputs

There are **8** cases that are involved in this algorithm

1. Player wins, then plays the same and wins
2. Player wins, then plays the same and loses
3. Player wins, then plays differently and wins
4. Player wins, then plays differently and loses
5. Player loses, then plays the same and wins
6. Player loses, then plays the same and wins
7. Player loses, then plays differently and wins
8. Player loses, then plays differently and loses

We will look at these events, then record whether ...

1. They played the same or different after the scenario
2. Whether the behaviour in the first point was a repeat in the preceding situation
