#include <stdio.h>

#include "aoc_print.h"
#include "aoc_days.h"

void print_days(void) {
    printf("Hello and welcome to AoC 2022!\n\n");

    printf("Day 1:\n");
    printf("  Part 1: %d\n", day01_pt1("../inputs/01.txt"));
    printf("  Part 1: %d\n", day01_pt2("../inputs/01.txt"));

    return;
}
