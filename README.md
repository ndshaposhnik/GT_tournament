# Usage

To run the tournament, simply write

```
python3 tournament.py
```

In order to add your strategy to the tournament, you need to write a corresponding function and add it to the list of strategies in the `main` function.

Every strategy has to have 2 arguments:
  
  - `your_history: list[str]` is a list of the moves of your strategy;
  - `opponent_history: list[str]` is a list of the moves of you opponent's strategy.

Each move is either `'C'` or `'D'`.

Output example:

```
--------------------  -------------------  -------------------  --------------------  ------------  -----------  -------------  ----------  ----------  ----
                      period_punishment_5  period_punishment_2  period_punishment_10  grim_trigger  tit_for_tat  all_cooperate  all_defect  random      SUM
period_punishment_5   [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [99, 104]   [309, 59]   2208
period_punishment_2   [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [99, 104]   [284, 159]  2183
period_punishment_10  [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [99, 104]   [265, 65]   2164
grim_trigger          [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [99, 104]   [263, 68]   2162
tit_for_tat           [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [99, 104]   [223, 223]  2122
all_cooperate         [300, 300]           [300, 300]           [300, 300]            [300, 300]    [300, 300]   [300, 300]     [0, 500]    [144, 404]  1944
all_defect            [104, 99]            [104, 99]            [104, 99]             [104, 99]     [104, 99]    [500, 0]       [100, 100]  [284, 54]   1404
random                [59, 309]            [159, 284]           [65, 265]             [68, 263]     [223, 223]   [404, 144]     [54, 284]   [207, 237]  1239
--------------------  -------------------  -------------------  --------------------  ------------  -----------  -------------  ----------  ----------  ----

```
