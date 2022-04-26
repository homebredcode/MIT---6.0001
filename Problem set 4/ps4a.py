# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        first_character = sequence[0]
        subsequent_characters = sequence[1:]
        permutations_without_first_character = get_permutations(subsequent_characters)

        for sequence in permutations_without_first_character:
            for index in range(len(sequence)+1):
                new_perm = sequence[0:index] + first_character + sequence[index:len(sequence)+1]
                permutations.append(new_perm)
        return permutations


        
print(get_permutations('abc'))

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


