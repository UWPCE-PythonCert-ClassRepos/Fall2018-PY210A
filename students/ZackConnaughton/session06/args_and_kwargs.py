#!/usr/bin/env python

def colors(fore_color='red',
           back_color='blue',
           link_color='green',
           visited_color='lavender'
           ):
    return fore_color, back_color, link_color, visited_color


def colors2(*args,
            **kwargs,
            ):
    """
    Takes in an abrituary number of arguments and keywork arguments based on the
    text color definitions. Returns the color definitions as a tuple in order.
    """
    #print(args)
    #print(kwargs)
    output = ['red', 'blue', 'green', 'lavender']
    kwargs_dict = {'fore_color': 0,
                   'back_color': 1,
                   'link_color': 2,
                   'visited_color': 3}
    x = 0
    if args:
        for arg_item in args:
            output[x] = arg_item
            x += 1
    if kwargs:
        for kwarg_key, kwarg_value in kwargs.items():
            #I really like pytest for this, I would have completely ignored
            #previously getting a TypeError here, maybe this is an improved method
            #and now that change is obvious and will make it into the documentation
            if kwargs_dict[kwarg_key] < len(args):
                raise TypeError('Reassigned an argument with a key value')
            output[kwargs_dict[kwarg_key]] = kwarg_value
    return tuple(output)
