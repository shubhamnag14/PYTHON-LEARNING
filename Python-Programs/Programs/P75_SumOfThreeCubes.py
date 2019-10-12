# This program tries to solve unsolved sum of three cubes problems,
# see https://en.wikipedia.org/wiki/Sums_of_three_cubes

max_cube_magnitude = 10000000000000000000
cube_magnitude_range = range(0, max_cube_magnitude)


# TODO: parallelise the program to run on multiple cores/computers at once
# TODO: add persistent store of cube ranges that have and have not been tried


def try_cubes(num, x_scalar, y_scalar, z_scalar):
    for x in [x_scalar, x_scalar * -1]:
        for y in [y_scalar, y_scalar * -1]:
            for z in [z_scalar, z_scalar * -1]:
                if (x ** 3) + (y ** 3) + (z ** 3) == num:
                    return [x, y, z]
    return None


def gen_cubes(num):
    for x in cube_magnitude_range:
        for y in cube_magnitude_range:
            for z in cube_magnitude_range:
                res = try_cubes(num, x, y, z)
                if res is not None:
                    return res


def print_cubes():
    print("Trying to find unsolved three cube sums")
    for num in [114, 390, 579, 627, 633, 732, 921, 975]:
        print("Trying to find the 3 cubes for " + str(num) + ".")
        cubes = gen_cubes(num)
        print("The cubes " + str(cubes[0]) + ", " + str(cubes[1]) +
              ", and " + str(cubes[2]) + " make " + str(num) + ".")


if __name__ == '__main__':
    print_cubes()
