packet_marker_length = 4
message_marker_length = 14


def characters_to_first_marker(marker_length):
    signal = read_signal()
    i = marker_length
    while not marker_found(i, signal, marker_length):
        i += 1
    return i


def read_signal():
    with open('../resources/signal.txt') as signal:
        signal = signal.readline()
        return signal


def marker_found(end, signal, marker_length):
    start = end - marker_length
    return len(set(signal[start:end])) == marker_length


if __name__ == '__main__':
    print(characters_to_first_marker(packet_marker_length))
    print(characters_to_first_marker(message_marker_length))
