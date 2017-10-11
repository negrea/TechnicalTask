# Performance engineering

In order to understand the script's performance in terms of overall 'wall' time taken the cProfile and pStats python library were used. After analyzing data gathered from the profiler, it was discovered that the performance bottleneck resides in the sort_csv function.

### Sample from profiler output

	Ordered by: cumulative time

	   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
		1    0.125    0.125    8.996    8.996 validate_postcodes.py:39(bulk_import)
		1    0.786    0.786    6.883    6.883 validate_postcodes.py:64(sort_csv)
	  2147855    2.055    0.000    2.539    0.000 validate_postcodes.py:109(get_rows)
		2    1.674    0.837    2.163    1.081 {method 'sort' of 'list' objects}
		2    1.830    0.915    1.830    0.915 {method 'writerows' of '_csv.writer' objects}
	  2147854    0.364    0.000    1.295    0.000 validate_postcodes.py:127(validate_postcode)

In analyzing the performance of the bulk_import python solution, we can see that there are a limited number of major operations that need to process the data and thus must go through every row in the file at least once. As such their minimal complexity is O(n). These are:

 - Reading
 - Decompressing
 - Validation
 - Sorting
 - Writing

Out of these reading, decompressing, validation and writing ensure the complexity is exactly O(n) through their implementation. For example, the get_rows_from_disk generator makes sure that each row of the file only gets read once and is processed immediately afterwards for validation. This results in a complexity of O(n) for reading the entire content of the file.

However, when it comes to sorting the industry leading algorithms have a worst case complexity of O(nlogn). One such algorithm is timsort which is used by Python's built in sorted() function. Timsort is an adaptive algorithm meaning it has a best-case complexity of 0(n) if list is already sorted, and also takes advantage of natural runs, sequences of already sorted elements. It is also fined tuned for speed and memory efficiency when operating on real life data. For these reasons and considering the exact specification of the file given (small in terms of contemporary RAM capacity) I have decided to use it for the sorting step.

As a small step in improving performance, attribute lookups were eliminated from the inner loop. The success_rows.append() and fail_rows.append() methods were placed into local variables success_rows_append and fail_rows_append and reused in the loop.

If there were any doubts that the file size could be larger (more than 200MB) an external sort algorithm such as mergesort would have been used. This would have broken the file into smaller chunks, sorted them in memory then merge them back together.

