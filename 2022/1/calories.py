#!/usr/bin/env python

from typing import List, Tuple


class Elf:
    def __init__(self, calories: int) -> None:
        self.calories = calories
        self.next = None
        self.prev = None


class ElfList:
    def __init__(self) -> None:
        self.head = None

    def add_elf(self, elf: Elf) -> None:
        if self.head is None:
            # Adding first elf to list
            self.head = elf
        elif self.head.calories < elf.calories:
            # Replacing head of list with current elf
            elf.next = self.head
            self.head.prev = elf
            self.head = elf
        else:
            curr_elf = self.head
            while curr_elf.next is not None and curr_elf.calories > elf.calories:
                curr_elf = curr_elf.next
            if curr_elf.calories > elf.calories:
                # Adding elf to end of list
                curr_elf.next = elf
                elf.prev = curr_elf
            else:
                # Adding elf to middle of list
                elf.next = curr_elf
                elf.prev = curr_elf.prev
                curr_elf.prev.next = elf
                curr_elf.prev = elf

    # Returns the nodes going forward and backward
    def __repr__(self) -> str:
        node = self.head
        temp_node = self.head
        nodes = []
        prev_nodes = []
        while node is not None:
            nodes.append(str(node.calories))
            temp_node = node
            node = node.next
        while temp_node.prev is not None:
            prev_nodes.append(str(temp_node.calories))
            temp_node = temp_node.prev
        nodes.append("None")
        prev_nodes.append("None")
        return " -> ".join(nodes) + "\n" + " -> ".join(prev_nodes)

    # Returns list of top elves and their calorie total
    def get_top_elves(self, count: int = 1) -> Tuple[List[int], int]:
        output = []
        curr_elf = self.head
        total = 0
        for i in range(0, count):
            total += curr_elf.calories
            output.append(curr_elf.calories)
            curr_elf = curr_elf.next
        return output, total


elf_list = ElfList()
with open('./input.txt') as file:
    current_calories = 0
    for line in file:
        if line.rstrip():
            current_calories += int(line.rstrip('\n'))
        else:
            elf_list.add_elf(Elf(current_calories))
            current_calories = 0

top_elves, total_calories = elf_list.get_top_elves(3)
print("1st most calories:", top_elves[0])
print("2nd most calories:", top_elves[1])
print("3rd most calories:", top_elves[2])
print("Total calories:", total_calories)
