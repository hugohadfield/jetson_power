
rail_names = {
"VDD_IN": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power0_input",
"VDD_SYS_GPU": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power0_input",
"VDD_SYS_CPU": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power1_input",
"VDD_SYS_SOC": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power1_input",
"VDD_SYS_DDR": "/sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_power2_input",
"VDD_4V0_WIFI": "/sys/bus/i2c/drivers/ina3221x/0-0040/iio:device0/in_power2_input"
}

def loop():
    for rail, file in rail_names.items():
        with open(file, "r") as fobj:
            milliwatts = int(fobj.readline())
            print(milliwatts, end='\t')
        print()


def print_titles():
    for rail, file in rail_names.items():
        print(rail, end='\t')
    print()


if __name__ == '__main__':
    print_titles()
    loop()
