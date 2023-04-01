from task1 import frequency_bitwise_test
from task2 import identical_consecutive_bits_test


def writeToRes(dst, nameOfTest, resOfTest):
    with open(dst, 'a') as f:
        f.write(f"{nameOfTest}: {resOfTest}")
        if (resOfTest >= 0.01):
            f.write(" It means, that sequence is random\n")
        else:
            f.write(" It means, that sequence is NOT random\n")


if __name__ == '__main__':
    with open('sequence.txt', 'r') as f:
        data = f.read()
    tmp = data.split(" ")
    tmp.remove("")
    sequence = list(map(int, tmp))
    sequence1 = list(map(lambda x: -1 if not x else 1, sequence))

    writeToRes("res.txt", "frequency_bitwise_test",
               frequency_bitwise_test(sequence1))
    writeToRes("res.txt", "identical_consecutive_bits_test",
               identical_consecutive_bits_test(sequence))
