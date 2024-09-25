from sys import argv


from for_task60_module.task61_module import func

min_, max_, count = map(int, argv[1:])
print(func(min_, max_, count))
