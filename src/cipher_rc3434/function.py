def cipher(text, shift, encrypt=True):

    """
    Cesar shift cipher.  Tool to decrypt/encrypt text that uses the substitution of a letter by another one further in the alphabet.

    Parameters
    ----------

    text : str: The message to encrypt or decrypt.

    shift : integer input: number of characters that message will move to encrypt. Can be a positive or a negative integer, depending in the desired direction . 

    encrypt : boolean: if True the message is encrypted; otherwise, it is decrypted.

    Returns
    -------
	A new str that has been encypted or decrypted according to the desired shift. 

    Examples
    --------
    >>> cipher ('text', shift, encrypt=True)

        >>> text = str([‘what a nice day’])

        >>> shift = int([4])

        >>> encrypt = True

    [‘Alex e rmgi heC’]

    >>> Cipher ('text', shift, encrypt=False)

        >>> text = str([‘Alex e rmgi heC’])

        >>> shift = int([4])

        >>> encrypt = False

    [‘what a nice day’]

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text