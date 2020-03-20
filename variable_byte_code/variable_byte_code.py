from struct import pack, unpack

def vb_encode(number):
    """VariableByteCode Encode for number
    Usage:
        import variable_byte_code as vb
        vb.encode(123)
    """
    bytes = []
    while True:
        bytes.insert(0, number % 128)
        if number < 128:
            break
        number //= 128
    bytes[-1] += 128
    return pack('%dB' % len(bytes), *bytes)

def vb_decode(bytestream):
    """VariableByteCode Decode
    Usage:
        import variable_byte_code as vb
        vb.decode(bytestream)
            => [1, 4, 123]
    """
    numbers = []
    n = 0
    bytestream = unpack('%dB' % len(bytestream), bytestream)
    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            numbers.append(128 * n + (byte - 128))
            n = 0
    return numbers