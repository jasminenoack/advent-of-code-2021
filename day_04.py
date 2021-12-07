from collections import defaultdict
from dataclasses import dataclass

from typing import List, Tuple, Dict

instructions = """
85,84,30,15,46,71,64,45,13,90,63,89,62,25,87,68,73,47,65,78,2,27,67,95,88,99,96,17,42,31,91,98,57,28,38,93,43,0,55,49,22,24,82,54,59,52,3,26,9,32,4,48,39,50,80,21,5,1,23,10,58,34,12,35,74,8,6,79,40,76,86,69,81,61,14,92,97,19,7,51,33,11,77,75,20,70,29,36,60,18,56,37,72,41,94,44,83,66,16,53

78 13  8 62 67
42 89 97 16 65
 5 12 73 50 56
45 10 63 41 64
49  1 95 71 17

60 25 66 82 22
94 45 68  5 12
46 44 48 31 34
10 56 37 96 81
99 39 84 32  6

11 86 77 36  2
57 68 27 74  4
81 92 49 37 51
78 43 94 46 63
13 52 72 17 44

88 13 81 21 20
80 99 23 37 53
44 68 15 38 55
84 48 82 97  6
 4 43 52 72 31

39 62 45 86 44
12 17 16  7  6
84 42 82 34 85
19 77  9 48 98
21 99 67 26 69

 1 75 50  5 44
 3 28 62 17 43
14 52 64 77 81
32 89  7 11 70
38 36 71 45 58

53 32 35 69 63
 6 21 75 64 96
10 89 15 48 26
23 20 43 57 33
18 49 51 47 74

20 79  9 74 13
52 28 77 26 43
57 83  4 25 70
90  1 30 53 38
56 66 82 35 51

12  3 31 93  8
20 27 51 78  9
29 46 82 85 75
15 76 91 70 63
59 39 13 43 79

46 35 15 13  2
65 69 97 77 87
64 59 94 88 40
34 79 92 93 58
47 28 74 82 29

32 38 24 68 12
 8 78 79 89 43
67 54  6 98 48
 1 14 83 15 37
44 10 97 74 33

 9 95  2 99  1
 8 42 60 56 40
32 11 71 14 80
77  6 68 46 48
98 70 39 44 62

43 94 41 13 15
96 99 35 27  8
22 75 73 17 90
62 23  5 88  3
10 52 61 60 57

31 62 74  3 79
15 49 60 28 71
66  2 11 36 41
34 80 33 94 75
64 56 84 70 16

98 94 68 32 26
61  7 52 66 18
40 20 82 81 74
28 36 89 14 35
71 11 44 13 72

81 30  6 86 37
46 45 64 83 62
 7 70 38 51 15
91 41 26 40  4
87  0 82 74 60

83 99 26 69  1
 6 98 53 31 43
82 64 42 90 34
87 62 11 40 39
77 51  2 30 97

96  5 24 44 32
48 92 78 74 76
99 33 93 97 49
45  8 88 66 59
52 64 29 60 82

69 23 59 96 71
14 93 21 44 62
65 84  2 39  1
 0 68 38 81  4
48 31 26 60 34

24 46 44 52 98
65 23 31 89  5
34 79 75 96 41
76 28 90 12 11
68 29 38 70 50

51  0 45 23 20
44 49 12 31  7
41 26 46 75 92
90 30 72 95 55
87 57 10 99 40

25 67 80 74 44
 3 82 27 81 11
33 42 97 57 70
19 94  0  2 49
 6 90 60 29 58

79 59 96 68 14
38 70 65 66 69
36 75 20 18 29
64 88 35 61 43
57 76 62 23 25

60  9 81 94 62
73 20 87 72 14
95 63 42 51 13
75 83 32 30 66
97  6 80 82 17

 3 88 31 43 68
20 78 47 10 91
14 42 40 74 39
 5 32 16 97  1
 9 33 49 70 36

77 31 65 27 52
49 74 57 25 66
24  4 39 33  1
23 14 19  2 21
80 71 29 81 91

32 68 47  3 88
 1 97 99 28 80
 2 25 18 31 51
26 10 73 34 40
 8 55 45 36 37

79 81 33 94 51
84  4 91  0 69
49 80 35 67 20
98 48 64 38 30
25 83 45 97 42

18  5 84 94 50
36 47  2 52 65
39 77 83 37 80
51 88 15 12 31
87 17 68 48 67

39 95 30  8 86
45 57 40 51 60
85 88 33 93 25
76 52 37 68  6
11 80 69 19 71

 6 71 25 66 54
33 17 98 63 20
27 14 44 43 18
68 10 50 35 65
61  3 83 12 13

46 21 43 15 19
99 82  8 95 80
 1 10 45 58 53
23 94 50 66 52
57 98 26 77 90

11 50 55 28 79
 4  3 26 57 56
68 86 10 87 69
32 35 89 63 29
66 27 33  8 30

23 34 94 93 47
 7 71  9 52 50
45 79 13 43 86
 0 51 17  6 26
 4 82 44 38 37

49 24 16 64 32
46 84  3 29 51
71 82 33 61 26
15  5 94 86 41
63 36 10 67 43

94 17  3 71 91
93 50 88 36 27
54 68  7  8 34
 9 92 37 45 52
47 29 70 10 69

79 27 30  0 12
51 70 19 89 20
 2 42 64 21 49
48 39  1  3 56
98 35 95 82 72

91 71 65 95 44
26 72 92 59 43
61 93  6  4 90
76 31  8  1 29
82 64 89 22 45

55  4  1 42 87
88 34 67 83 45
22 23 98 24 12
74 72 49 32 25
73  7 19 26  3

 0 43 50 57 80
68 21 87  1 91
60  6 81 78 99
35 98 72 49 16
36 25 13 48 22

59  1 26  3 71
43 55 50  7 16
 5 64 29 38 84
41 23 60 19 24
85 58 49 98 33

80 48  3 65 38
30 97 96 45  7
 6 85  8 90 40
37 78 84 16 24
69 11 43 64 63

28 14 19  1 97
37 39 86 23 64
20 67 85 65 90
54 51 59 91 43
17 30 11 24  7

22 88 27 43 10
35  3 72 52 57
61 54 28 69 37
71 78 96 82 81
33 39 32 40  7

50 60 69 33 57
84 22 95 74  6
90 94 71 45 68
72 86 77  9 24
73 12 89 13  1

66 35 36 87 73
77 96 52 47 68
63  4 83 20 95
17 70  9 18 50
98 40 25 60 26

31 37 81 34 56
 3 15 43 51 35
67 70  1 20 12
80 54 69 17 88
65 91 60  8 53

76 23 87 41 18
49 58 92 98 25
77 53 44 17 27
67 28 37 66 95
59 39 33  4 34

 0 25  2  5 22
26 85 90 51 21
31 79 10 41 45
69 56  1 67 40
59 98 99 89  6

95 67 72 52 78
88 61 96 11 43
34 73 53 54  8
71  3 70 42 58
12 82 97 68 98

20 10 13 74 89
82 25 45 92 61
58 62  0 22 57
68 90 36 18 75
48 39 69  4 52

40  3 86 33 98
30 67 39  7 69
80 64 77 54 51
24 49  6 68 61
62 94  1 26 50

89 88  7 21 87
83 10 78 27 97
35 62 86 13 38
28 80 19 36 75
98 93 47 33 57

22 88 35 79 85
98 96 89 69 17
37 62 57 39  1
99 10 55 50 71
65 94 67  4 63

 7 83 51 95 98
56 93 62 85  9
72 14 44 70 67
42  4 65 37 54
47 82  1 60 55

 0 73 60 25 64
90 11 93 85 89
80 97 86 76 96
43 92 88 72 44
62 87 81 34 49

47 27 89 98 68
86 76 14 96 17
21  4 41 74 29
18 82 33 34 20
30 62 95 42 51

45  4 70 20 53
66 39 43 82  1
54 30 68 77 42
61 41 65 94 35
25 78 22 26 46

70 73 44 48 61
69  7 85 47 89
91 22 12 98 11
25 60 58 46 54
 5 37 83 62 65

47 62 30 70 40
86  9 64 61  0
27 63 90 88 17
18 71 42 33 93
91 14 81  4 31

81  7 22 94 55
99 90 60  9 46
65  2 47  1 73
78 76 75 19 88
63 51 86 56 49

25 27 12 22 30
87 75 16  4 32
19 73  5 20 52
18  6 34 94 31
23 96 84 26 66

23 69 51 35  5
13 76 99 89 82
88  3 50 54 33
19 59 92 84 34
64 80 42 40 60

15 91 92 60 36
46 40 53 34 27
13 35 96 16 42
 4 61 81 56 24
85 21  7 99 20

32 37 19 21 28
66  7 96 46 88
23 52 25 50 22
53 62 34 81 27
98 31 14 40 49

23 43 71 61 12
 8 94 91 74  7
67  2 59 77  4
39 18 97 41 21
55 15 31  9 38

29 69 52 16 75
71 15 34 79 86
62 57 48 44 54
11 32 96 13 60
56 77 26 68 82

93 57 21 94 31
29  4 59 24 40
13 99 34 96 91
70 55 47 62 51
33 32 19 69 71

76 80  1 57 20
13 28 72 27 79
40 21 71 37 85
26 12 67 33 99
11 41 62 18 64

23 22 92 69 86
38 79 47 56 83
74 46  1 95 24
93 71 28 54 52
94 51 33 57 73

17 96  4 81 76
67 20 24 21 70
28 77  3 74 10
45 78 18  7 15
 8 48 27 58 13

51 58 59 73 35
13  7 92 15 98
75 26  1 49 24
91 85 44 34 74
64  2 20 72 90

46 89 50 54 79
 9 60 98 36 78
91 16 80 92 20
77 69 13 76 75
95 41 45  3 40

86  7 67 20 99
14 18 97 70  0
81 27 89 30  3
39 37 56 42 32
35 71 49  8 73

60 67 61  6 86
25 41 24 29 88
98  3 90 56 87
45 22 84 70 99
53 59 27 26 57

17  4 11 41 66
28 39 27 54 89
 3 78 37 93 29
95 23 86 51 40
75 67 71 57 92

60 41 91 89 52
68 46 83 62  1
18 21 72 19 35
55 34 11 16 75
32 71 61 78 50

27 38 70 48 93
16  2 80 17 63
97 89 55 86 85
54  5 41 33 60
51 95 12 67 37

72 17 74  6 41
53 19  8 12 92
39 84 82 63 48
22 21 87 13 32
40 34 64 15 31

75  2 46 64 99
26 72 79 90 76
85 68 10 28 67
20 34 81 12 83
92  1 65 43 71

49 80 85 54  9
31 40 22 94 51
12 73 43 68 98
78 91 70  3 28
47 59 69 99 62

46 56 28 73 20
 5 29 69 68 22
64 12  8 52 92
36 44 90 72  0
76 48 33 86 66

99 61 97 17 74
32 52 44 42  9
57 67 36 41 31
68  1 50 22 11
73 12 21 48 62

44 53 77 88 87
27 99 59 98 74
33 66 51 14 34
29 30 60 49 80
47 84 36 12 71

29 89 54 59 70
87 65 77 38 25
40 17 41  9 30
45 27  0  5 24
52  8 35 68 10

16 41 66 87 76
94 70 51 48 96
90 73 98 89 91
 4 46 30 28 63
68 45 37 80 57

19 11 46 41 14
94 48 66 86  9
42 90 56 70 21
95 54 74 30 87
81 89 49 60 34

18 90 79 64 98
27 74 59 53 11
96 45 17 14 23
 9 60 30 42 12
97 21 31  5 41

98 63 51 92 64
55 30 46 22 91
 8 73 61 57 67
37 60 49 31 10
80 99 77 11 82

52 69 77 41  8
94 11 78 62 28
91 39 96 79  3
44 88 37  0 47
 6 80 49 98 48

93  2 70 26  4
47  8 94 12  3
10  7 24 40 23
49 84 50 56 44
41 53 96  1 85

76 78 70 24 75
71 19 85 77 25
21 44 58 45 64
40 38  9 50 61
79 42 86 37  6

34 39 94 84  0
90 80 78 54 49
13 81 87 60 56
74 59 75 41 28
29 67 66 44 20

50 66 43 39 16
88 94 60 70 64
63 80 56 69 36
53 48 32 22 79
59 77 20 30 67

70 56 80 12 11
35 55 40 71 87
84 27 96 46 85
20 23 26 29 14
58 37 21 75 68

78 23 13 37 94
65 44 54 43 38
29 60 83  1 57
98  2 75 12 14
92 25 48  9 52

64 37 93 48 34
22 81 58  5 13
63 80  2 67 53
62 52 79 41 44
83 75 96 91 88

 1 54 88 45 90
81 78 19  8 40
17 74 69 87 33
 9 64 85 50 71
92 38 65 82 41

 2 62 96 60 81
51  1 34 48 25
78 13 74 65 42
46 64 57 19 72
85 88 53 68 76

57 95 40 92 27
65 37 42 90  9
17 72 78 43 45
87 28 48 81 79
 7  4 24 67 70
"""

"""
Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. 
(Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, 
that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. 
It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). 
For example:
"""

test_instructions = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

@dataclass
class Space:
    value: int
    marked: bool = False


@dataclass
class Board:
    board: List[List[Space]]
    map_value_to_cell: Dict[int, Tuple[int, int]]

    @classmethod
    def factory(cls, board):
        value_map = {}
        for row_index, line in enumerate(board):
            for column_index, spot in enumerate(line):
                value_map[spot.value] = (row_index, column_index)
        return cls(board, value_map)

    def has_cell(self, value):
        return self.map_value_to_cell.get(value)

    def find_cell(self, value):
        return self.map_value_to_cell[value]

    def check_column(self, index):
        return all(line[index].marked for line in self.board)

    def check_row(self, index):
        return all(x.marked for x in self.board[index])

    def respond_to_call(self, value):
        if not self.has_cell(value):
            return False
        row, column = self.find_cell(value)
        self.board[row][column].marked = True
        return self.check_column(column) or self.check_row(row)

    def score(self):
        total = 0
        for line in self.board:
            for space in line:
                if not space.marked:
                    total += space.value
        return total


def build_calls(calls_data):
    return [int(x) for x in calls_data.split(',')]


def build_board(board_data):
    board = []
    lines = board_data.split('\n')
    for line in lines:
        line_values = []
        for spot in line.split():
            line_values.append(Space(value=int(spot)))
        board.append(line_values)
    return Board.factory(board=board)


def build_boards(boards):
    return [
        build_board(board)
        for board in boards
    ]


def set_up_data(input):
    values = input.strip().split('\n\n')
    calls = build_calls(values[0])
    boards = build_boards(values[1:])
    return calls, boards


def call_a_number(call, boards):
    winners = []
    for index, board in enumerate(boards):
        if board.respond_to_call(call):
            winners.append(index)
    return winners


"""
The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on 
that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when 
the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. 
What will your final score be if you choose that board?
"""
def score_board(board, last_call):
    score = board.score()
    return score * last_call


def win_bingo(input):
    calls, boards = set_up_data(input)
    for call in calls:
        winners = call_a_number(call, boards)
        if winners:
            return score_board(boards[winners[0]], call)
    return


def lose_bingo(input):
    calls, boards = set_up_data(input)
    board_ids = set(range(len(boards)))
    calls, boards = set_up_data(input)
    last_score = None
    for call in calls:
        winners = call_a_number(call, boards)
        if winners:
            for winner in winners:
                if winner in board_ids:
                    board_ids.remove(winner)
                    last_score = score_board(boards[winner], call)
    return last_score


print("part 1 test", win_bingo(test_instructions))
print("part 1 real", win_bingo(instructions))

print("part 2 test", lose_bingo(test_instructions))
print("part 2 real", lose_bingo(instructions))
