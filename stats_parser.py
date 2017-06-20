import re
import glob
import csv


def read_file_asstrem(file_name):
    str = open(file_name, 'r').read()
    return str
    # print(str)


def tokenizer(str, file_name):
    # Need to find how to print all the matches in python, eg: regex ''^.*[i|d]cache.overall_accesses::total.*([0-9]+)''
    regex_list = ['^.*[i]cache.overall_accesses::total.* ([0-9]+)', '^.*[i]cache.overall_misses::total.* ([0-9]+)',
                  '^.*[d]cache.overall_accesses::total.* ([0-9]+)', '^.*[d]cache.overall_misses::total.* ([0-9]+)',
                  'sim_seconds.* ([0-9]+.*[0-9])']

    total_misses = 0
    total_access = 0
    sim_time = 0
    for each in regex_list:
        m = re.search(each, str, re.M)
        if m.group(0).find('misses') >= 0:
            total_misses += int(m.group(1))
        elif m.group(0).find('accesses') >= 0:
            total_access += int(m.group(1))
        else:
            sim_time = float(m.group(1))

    return [file_name.strip('txt'), float(total_misses / total_access), sim_time]


def main():

    f = open('output_stats.txt', 'wt')
    writer = csv.writer(f)
    writer.writerow(('file_name', 'average rate', 'simulation time'))
    #writer = csv.writer(f)
    for filename in glob.iglob('./results/*'):
        str = read_file_asstrem(filename)
        list = (tokenizer(str, filename))
        writer.writerow((list[0], list[1], list[2]))


# Here's our payoff idiom!
if __name__ == '__main__':
    main()
