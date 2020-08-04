# Algorithms - Iterative Sorting

## How do we measure how “good” an algorithm is?

When given a choice between different algorithms, we want to choose the most efficient algorithm (considering both time and space efficiency depending on our needs).

Note: It is common for your first solution to work with a few items or users, but break as you add more. Making sure solutions scale is something that all developers must remain vigilant about.

## Selection Sort

Time Complexity: `O(n^2)`
Required Space: `O(1)`

Example:

```python
def selection_sort(array):

	# the mininum index value starts at 0 and increases by 1 with each repitition
	for min_index in range(len(array)):

		# keep track of the index for the mininum value
		min_value_index = min_index

		# find the mininum value in the remaining unsorted array and store it's index
		for current_index in range(min_index + 1, len(array)):
			if array[current_index] < array[min_value_index]:
				min_value_index = current_index

		# swap the values for min_index and min_value_index
		array[min_index], array[min_value_index] = array[min_value_index], array[min_index]

array = [3,11,19,2,7,17,1,5,13,23]
print('sorted array: ', selection_sort(array))
# sorted array: [1,2,3,5,7,11,13,17,19,23]
```

## Insertion Sort

Time Complexity: `O(n^2)`
Required Space: `O(1)`

```python
def insertion_sort(array):
	# start at the second element, assume the first is a sorted array with 1 element
	for current_index in range(1, len(array)):
		current_value = array[i]

		# start at the element to the immediate left of current_index
		checking_index = current_index - 1
		checking_value = array[checking_index]

		#  move elements that are greater than the array one position ahead of their current position
		while checking_index >= 0 and current_value < checking_value:
			array[checking_index + 1] = array[checking_index]
			checking_index = checking_index - 1

		# insert current_value where it belongs
		array[checking_index + 1] = current_value

array = [3,11,19,2,7,17,1,5,13,23]
print('sorted array: ', insertion_sort(array))
# sorted array: [1,2,3,5,7,11,13,17,19,23]
```

## Bubble Sort

Time Complexity: `O(n^n)`
Required Space: `O(1)`

```python
def bubble_sort(array):
	for index in range(len(array) - 1):
		#  set/reset swap_flag
		swap_flag = False

		# the last index values are already sorted
		for current_index in range(0, len(array) - index - 1):

			# if the current value is bigger than the next value; swap them and trigger swap flag
			if array[current_index] > array[current_index + 1]:
				array[current_index], array[current_index + 1] = array[current_index + 1], array[current_index]
				swap_flag = True

		# if swap flag hasn't been trigger, break out of the loop
		if not swap_flag:
			break

array = [3,11,19,2,7,17,1,5,13,23]
print('sorted array: ', bubble_sort(array))
# sorted array: [1,2,3,5,7,11,13,17,19,23]
```
