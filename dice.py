# 
#   Copyright 2019 Maarten de Goede
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from random import *


def experiment(run_count, trial):
    prob = 0
    for _ in range(run_count):
        if trial(): prob += 1
    return prob / run_count


def dice_builder(values=range(6), weights=None, dice_count=1):
    return lambda: sum(choices(values, weights=weights, k=dice_count))


if __name__ == '__main__':
    run_count = 100000
    check = lambda: s1() < s2()
    text = "Probability of S1 beating S2:"

    # Case 1:
    # S1 = (9, {1,2,3,4}, lambda x: 1/4)
    # S2 = (6, {1,2,3,4,5,6}, lambda x: 1/6)
    # Probability of S1 beating S2: 0.57315
    s1 = dice_builder(range(4), dice_count=9)
    s2 = dice_builder(dice_count=6)
    print("Case 1:", text, experiment(run_count, check))

    # Case 2:
    # S1 = (1, set(range(1,36+1)), lambda x: 1/36)
    # S2 = (36, {0,1}, lambda x: 1/2)
    s1 = dice_builder(range(1, 37), dice_count=1)
    s2 = dice_builder([0, 1], dice_count=36)
    print("Case 2:", text, experiment(run_count, check))

    # Case 3:
    # S1 = (6, {1,2,3,4}, lambda x: 1/4)
    # S2 = (4, {1,2,3,4,5,6}, lambda x: 1/6)
    s1 = dice_builder(range(4), dice_count=6)
    s2 = dice_builder(dice_count=4)
    print("Case 3:", text, experiment(run_count, check))

    # Case 4:
    # S1 = (6, {1,2,3,4}, {1: 1/3, 2: 1/5, 3: 1/7, 4:1-1/3-1/5-1/7})
    # S2 = (4, {1,2,3,4,5,6}, lambda x: 1/6)
    s1 = dice_builder(range(4), [1 / 3, 1 / 5, 1 / 7, 1 - 1 / 3 - 1 / 5 - 1 / 7], 6)
    s2 = dice_builder(dice_count=4)
    print("Case 4:", text, experiment(run_count, check))

    # Case 5:
    # S1 = (55, {1,3}, lambda x: 1/2)
    # S2 = (20 , set(range(1,11)), lambda x: 1/10)
    s1 = dice_builder([1, 3], dice_count=55)
    s2 = dice_builder(range(1, 11), dice_count=20)
    print("Case 5:", text, experiment(run_count, check))

    # Case 6:
    # S1 = (10, {1,3}, lambda x: 1/2)
    # S2 = (20 , {0,2}, lambda x: 1/2)
    s1 = dice_builder([1, 3], dice_count=10)
    s2 = dice_builder([0, 2], dice_count=20)
    print("Case 6:", text, experiment(run_count, check))
