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
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) <= 1:
        word_list = [sequence]
    else:
        word_list = []
        for letter in sequence:
            previous_list = get_permutations(sequence.replace(letter,'',1))
            for word_from_list in previous_list:
                for i in range(len(word_from_list)):
                    word_temp = word_from_list[0:i]+letter+word_from_list[i:len(word_from_list)]
                    if word_temp not in word_list: word_list.append(word_temp)
    return word_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #test: single character
    single_char_input = 'a'
    print('Input:', single_char_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(single_char_input))
    
    #test: standart
    standart_input = 'abc'
    print('Input:', standart_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(standart_input))
    
    #test: double letter
    double_input = 'abba'
    print('Input:', double_input)
    print('Expected Output:', ['abba', 'baba', 'bbaa', 'abab', 'baab', 'aabb'])
    print('Actual Output:', get_permutations(double_input))
    

