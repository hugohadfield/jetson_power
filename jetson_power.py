
import time

output_file = 'power.txt'

rail_names = {
"VDD_IN": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power0_input",
"VDD_SYS_GPU": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power0_input",
"VDD_SYS_CPU": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power1_input",
"VDD_SYS_SOC": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power1_input",
"VDD_SYS_DDR": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power2_input",
"VDD_4V0_WIFI": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power2_input"
}

def loop(file_echo=None):
    for rail, file in rail_names.items():
        with open(file, "r") as fobj:
            milliwatts = int(fobj.readline())
            print(milliwatts, end='\t')
            if file_echo is not None:
                print(milliwatts, end='\t', file=file_echo)
    print()


def print_titles(file_echo=None):
    for rail, file in rail_names.items():
        print(rail, end='\t')
        if file_echo is not None:
            print(rail, end='\t', file=file_echo)
    print()


if __name__ == '__main__':
    with open(output_file, 'w') as ofobj:
        print('Time', end='\t')
        print('Time', end='\t', file=ofobj)
        print_titles(file_echo=ofobj)
        tstart = time.time()
        while True:
            time.sleep(1.0)
            this_time = time.time() - tstart
            print(this_time, end='\t')
            print(this_time, end='\t', file=ofobj)
            loop(file_echo=ofobj)
