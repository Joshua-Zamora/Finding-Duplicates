# CS2302 DATA STRUCTURES
# Author: Joshua Zamora
# OPTION A (Inspecting Files)
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Last Updated 9 / 24 / 2019
# The purpose of this program is to store ID numbers in a linked-list and
# find duplicates using 4 solutions

from time import perf_counter


class Node(object):
    item = -1
    next_node = None

    def __init__(self, item):
        self.item = item


class SinglyLinkedList(object):
    head = None

    def __init__(self, head=None):
        self.head = head

    def add_at_end(self, node):
        if not self.head:  # if list is empty add head node
            self.head = node
        else:
            temp = self.head
            while temp.next_node:  # adds nodes at end
                temp = temp.next_node
            temp.next_node = node

    def get_length(self):
        length = 1
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
            length = length + 1  # counts up the nodes in the list

        return length

    def get_at_index(self, index):
        temp = self.head
        if index < 0 or index > (self.get_length() - 1):  # checks if index is in range
            print('LList index out of bounds!')
            return temp
        i = 0
        while i < index:  # increases index till desired node is next
            temp = temp.next_node
            i = i + 1

        return temp

    def find_duplicates(self):
        temp = self.head
        num_duplicates = 0

        # traverses list in order to find duplicates
        while True:
            if temp.item == temp.next_node.item:
                num_duplicates = num_duplicates + 1  # increases counter if node items are equal
            if not temp.next_node.next_node:
                break
            else:
                temp = temp.next_node

        return num_duplicates


def solution_1(id_linked_list, length):
    num_duplicates = 0
    temp_one = id_linked_list.head

    for i in range(length):
        temp_two = id_linked_list.head

        for j in range(length):  # if duplicate or same element continue to next iteration
            if temp_two.item == -1 or temp_one.item == -1 or temp_one == temp_two:
                if temp_two.next_node:
                    temp_two = temp_two.next_node  # gets next node to compare
                else:
                    break
                continue
            if temp_one.item == temp_two.item:
                temp_two.item = -1  # marks duplicates as -1
                num_duplicates = num_duplicates + 1  # increases duplicate counter

            if temp_two.next_node:
                temp_two = temp_two.next_node  # gets next node to compare
            else:
                break  # else break out of loop

        if temp_one.next_node:
            temp_one = temp_one.next_node  # gets next node to compare
        else:
            return num_duplicates


def solution_2(id_linked_list):
    left_node = id_linked_list.head
    right_node = left_node.next_node
    num_comparisons = 0

    while True:
        while True:
            if right_node.item < left_node.item:
                temp_node_item = right_node.item
                right_node.item = left_node.item  # swaps the item data between adjacent nodes
                left_node.item = temp_node_item
                num_comparisons = num_comparisons + 1

            if not right_node.next_node:  # checks if we've reached the end of the list
                break  # breaks out of loop
            else:
                right_node = right_node.next_node

            left_node = left_node.next_node  # moves over one node

        if num_comparisons is 0:  # checks if the list is sorted
            break
        else:
            left_node = id_linked_list.head
            right_node = left_node.next_node
            num_comparisons = 0

    return id_linked_list


def solution_3_part_2(numbers, i, j, k):
    merged_size = k - i + 1  # size of merged partition
    merged_numbers = SinglyLinkedList(Node(0))  # temporary linked list for merged numbers

    for l in range(merged_size):
        merged_numbers.add_at_end(Node(0))

    merge_pos = 0  # position to insert merged number

    left_pos = i  # initialize left partition position
    right_pos = j + 1  # initialize right partition position

    while left_pos <= j and right_pos <= k:  # adds smallest element from left or right partition to merged numbers
        if numbers.get_at_index(left_pos).item < numbers.get_at_index(right_pos).item:
            merged_numbers.get_at_index(merge_pos).item = numbers.get_at_index(left_pos).item
            left_pos = left_pos + 1
        else:
            merged_numbers.get_at_index(merge_pos).item = numbers.get_at_index(right_pos).item
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    while left_pos <= j:  # if left partition is not empty, adds remaining elements to merged numbers
        merged_numbers.get_at_index(merge_pos).item = numbers.get_at_index(left_pos).item
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    while right_pos <= k:  # if right partition is not empty, adds remaining elements to merged numbers
        merged_numbers.get_at_index(merge_pos).item = numbers.get_at_index(right_pos).item
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    merge_pos = 0
    while merge_pos < merged_size:  # copies the merge numbers back to numbers
        numbers.get_at_index(i + merge_pos).item = merged_numbers.get_at_index(merge_pos).item
        merge_pos = merge_pos + 1


def solution_3(numbers, i, k):
    if i < k:
        j = (i + k) // 2  # find the midpoint in the partition

        solution_3(numbers, i, j)
        solution_3(numbers, j + 1, k)  # recursively sort left and right partitions

        solution_3_part_2(numbers, i, j, k)  # merge left and right partitions in sorted order

    return numbers


def solution_4(id_linked_list, length):
    boolean_list = [False] * (length + 1)  # creates and fills a list with False values
    num_duplicates = 0
    current_node = id_linked_list.head

    while True:
        if not boolean_list[current_node.item]:  # marks id duplicates as True
            boolean_list[current_node.item] = True
        else:
            num_duplicates = num_duplicates + 1  # if element is True, marks it as a duplicate

        if current_node.next_node:  # checks if the end of the list has been reached
            current_node = current_node.next_node
        else:
            break

    return num_duplicates


def list_copy():
    file_object = open('activision.txt')
    file_to_list = file_object.readlines()  # reads each line to an element in a list

    file_object = open('vivendi.txt')
    file_to_list_two = file_object.readlines()  # reads each line to an element in a list

    file_to_list.extend(file_to_list_two)
    return file_to_list


def list_to_linked_list(id_list):
    new_linked_list = SinglyLinkedList(Node(int(id_list.pop(0))))  # creates linked list with first id stored

    while len(id_list) > 0:
        temp_node = Node(int(id_list.pop(0)))  # adds id numbers to the front of the list
        temp_node.next_node = new_linked_list.head
        new_linked_list.head = temp_node

    return new_linked_list


id_linked_list_one = list_to_linked_list(list_copy())
id_linked_list_two = list_to_linked_list(list_copy())
id_linked_list_three = list_to_linked_list(list_copy())  # creates linked-lists based on given files
id_linked_list_four = list_to_linked_list(list_copy())

linked_list_length = id_linked_list_one.get_length()  # gets linked-lists length

start = perf_counter()  # timer
print('\nSOLUTION 1: ', solution_1(id_linked_list_one, linked_list_length), ' DUPLICATES')
stop = perf_counter()
print('\tTime elapsed: ', round(stop - start, 2), ' seconds')

start = perf_counter()
print('\nSOLUTION 2: ', solution_2(id_linked_list_two).find_duplicates(), ' DUPLICATES ')
stop = perf_counter()
print('\tTime elapsed: ', round(stop - start, 2), ' seconds')

start = perf_counter()
print('\nSOLUTION 3: ', solution_3(id_linked_list_three, 0, linked_list_length - 1).find_duplicates(), ' DUPLICATES ')
stop = perf_counter()
print('\tTime elapsed: ', round(stop - start, 2), ' seconds')

start = perf_counter()
print('\nSOLUTION 4: ', solution_4(id_linked_list_four, linked_list_length), ' DUPLICATES ')
stop = perf_counter()
print('\tTime elapsed: ', round(stop - start, 2), ' seconds')
