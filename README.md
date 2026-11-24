[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Adnanhasim8/makefun-irvan-haiku-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Adnanhasim8/makefun-irvan-haiku-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

# Seventeen Syllables of Debugging

One haiku about debugging, in the 5-7-5 shape, for the make.fun competition
[u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605):

> the debugger halts
> on the line I swore was safe
> nothing ever was

The debugger stops on the one line the author trusted — and the last line
takes that trust away. Seventeen syllables, 65 characters including the
trailing newline, one concrete image, no explanation of the turn.

## How to run

Python 3.13 standard library only, no network needed:

```sh
python3 main.py
```

It writes the haiku to `/output/entry.txt` (UTF-8). The program asserts its
own gate before writing: exactly 3 non-empty lines, at most 200 characters
total, and the hand-counted syllables 5-7-5.
