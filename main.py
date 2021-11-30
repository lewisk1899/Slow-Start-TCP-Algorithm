# Lewis Koplon
# Professor Lazos
# ECE 578
# Slow Start Simulation Given Network Parameters

def slowStartAlg():
    bandwidth = 1 * 10 ^ 9  # bits per second
    one_way_latency = .1  # second
    file_size = 10 * 1024  # File Size in Kilobytes
    receive_window_size = 1024  # in Kilobytes
    # How many RTTs does it take until slow start opens the send window to 1 MB?
    sender_window_size = 1  # in Kilobytes
    number_of_rtts = 0
    while file_size >= 0:
        if sender_window_size <= receive_window_size: # SLOW START
            file_size -= sender_window_size  # remove the amount of the file that is sent by the sender
            print("#####################################")
            print("Number of RTTs:", number_of_rtts)
            print("File size remaining in Kilobytes:", file_size)
            print("Sender Window Size in Kilobytes:", sender_window_size)
            number_of_rtts += 1  # assume ack is received after the data is sent
            sender_window_size *= 2  # increase the sender window size by two times itself
        else:
            sender_window_size /= 2


slowStartAlg()
