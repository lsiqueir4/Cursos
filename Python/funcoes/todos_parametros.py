def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    
if __name__ == '__main':
    todos_params(1,2,3, legal=True)
