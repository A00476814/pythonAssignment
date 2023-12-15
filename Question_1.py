def stack(our_list, operation, new_element=None):
    if operation.lower() == 'add' and new_element is not None:
        our_list.insert(0, new_element)
    elif operation.lower() == 'remove':
        if len(our_list) != 0:
            our_list.pop(0)
        else:
            return "Invalid operation: No element is present in the stack"
    return our_list

def queue(our_list, operation, new_element=None):
    if operation.lower() == 'add' and new_element is not None:
        our_list.append(new_element)
    elif operation.lower() == 'remove':
        if len(our_list) != 0:
            our_list.pop(0)
        else:
            return "Invalid operation: No element is present in the queue"
    return our_list
