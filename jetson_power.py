
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


def print_echo(string, file_echo=None, **kwargs):
    print(string, **kwargs)
    if file_echo is not None:
        print(string, file=file_echo, **kwargs)


def loop(file_echo=None):
    for rail, file in rail_names.items():
        with open(file, "r") as fobj:
            milliwatts = int(fobj.readline())
            print_echo(milliwatts, end='\t', file_echo=file_echo)
    print_echo("", file_echo=file_echo)


def print_titles(file_echo=None):
    for rail, file in rail_names.items():
        print_echo(rail, end='\t', file_echo=file_echo)
    print_echo("", file_echo=file_echo)


if __name__ == '__main__':
    with open(output_file, 'w') as file_echo:
        print_echo("Time", file_echo=file_echo)
        print_titles(file_echo=file_echo)
        tstart = time.time()
        while True:
            time.sleep(1.0)
            this_time = time.time() - tstart
            print_echo(this_time, end='\t', file_echo=file_echo)
            loop(file_echo=file_echo)
