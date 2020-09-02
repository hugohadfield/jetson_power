import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages


def process_line(line):
    if len(line) < 5:
        return None
    else:
        return [s.rstrip() for s in line.split()]


if __name__ == '__main__':
    with open('power.txt', 'r') as fobj:
        nmeasurements = 0
        output_list = []
        titles = []
        lines = fobj.readlines()
        for line_number, line in enumerate(lines):
            if line_number == 0:
                titles = process_line(line)
                nmeasurements = len(titles)
            else:
                strings = process_line(line)
                output_list.append([float(s) for s in strings])
        np_output = np.array(output_list)

        pdf_name = 'power.pdf'
        pp = PdfPages(pdf_name)
        time = np_output[:, 0]
        for i in range(1, nmeasurements):
            v = plt.figure()
            plt.plot(time, np_output[:, i])
            plt.title(titles[i])
            plt.xlabel('time (s)')
            plt.ylabel('power (mw)')
            pp.savefig(v)
        pp.close()