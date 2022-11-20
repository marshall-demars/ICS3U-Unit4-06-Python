#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program uses nested loops to print RGB values


def main():
    # This program uses nested loops to print RGB values

    rgb1 = 0
    rgb2 = 0
    rgb3 = 0

    # input,process,output
    for rgb1 in range(256):
        for rgb2 in range(256):
            for rgb3 in range(256):
                print("\nRGB({0},{1},{2})".format(rgb1, rgb2, rgb3))

    print("\nDone.")


if __name__ == "__main__":
    main()
