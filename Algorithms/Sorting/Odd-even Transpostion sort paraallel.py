"""
Write a Python program to sort unsorted numbers using Odd Even Transposition Parallel sort.
Odd Even Transposition Parallel sort:
This is an implementation of odd-even transposition sort.
It works by performing a series of parallel swaps between odd and even pairs of variables in the list.
This implementation represents each variable in the list with a process and each process communicates with 
its neighbouring processes in the list to perform comparisons.
They are synchronized with locks and message passing but other forms of synchronization could be used.
"""