# Create a program to read a PGM and then also write an output PGM file
# with higher contrast, displaying grey level histograms 

import sys, re

if len(sys.argv) == 1:   # check for command line path arg
        print("Missing file argument. Add file argument. (try '/users/abrick/resources/maquinna.pgm')")
        exit()


with open(sys.argv[1]) as content:

        parts = re.split(r'\s+',re.sub(r'#.*',r'\n',content.read()))   # splits out

        magicnum, x_dimensions, y_dimensions, maxgrayvalue = parts[0],int(parts[1]), int(parts[2]), int(parts[3])

        bucketnum = 1  # bucket counter
        x = 4  #start at 4th since the first three parts are reserved for magic number, x dimensions, y dimensions, and max value
        y = 19 # 15 unit increments

        if magicnum == "P2":
                print("Valid PGM File.")


                while bucketnum < 17:  # sixteen buckets
                        pixels = [int(n) for n in parts[x:y] if n]   # creates list from slice
                        pixels = sum(pixels) # counts the values in the 15 unit slice 

                        print(round(pixels/50) * '-', "Bucket", bucketnum, "has the following levels of gray ", pixels, sep='\t') # prints out count of each bucket
                        bucketnum += 1 # increments bucket count
                        x += 15 # increments to next bucket slice
                        y += 15 # increments to next bucket slice
        
                upscale_contrast()


        else: 
                print("Not a valid greyscale ASCII PGM File try ('/users/abrick/resources/maquinna.pgm')")
                exit()

def upscale_contrast():
        upscaleval = 2

        # PGM image upscaler continuing last week's code.
        FACTOR = 3
        # A dict of dicts indexes the pixel data by Cartesian dimensions.
        two_d = collections.defaultdict(dict)
        for y in range(y_dim):
        for x in range(x_dim):
        two_d[x][y] = pixels[x+x_dim*y]
        # Create a simple upscaling using nearest-neighbor sampling.
        header = 'P2\n{} {}\n{}\n'.format(x_dim*FACTOR,y_dim*FACTOR,depth)
        with open('larger.pgm','w') as larger:
        larger.write(header)
        for y in range(y_dim*FACTOR):
        for x in range(x_dim*FACTOR):
        larger.write((str(two_d[x//FACTOR][y//FACTOR])+' '))

dimension, depth = x_dimensions, y_dimensions
greys = range(depth)

with open('output.pgm','w') as target:
        header, pixels = 'P2\n{0} {0}\n{1}\n'.format(dimension,depth), ''
        for row in range(dimension):
                for column in range(dimension):
                pixels += str(random.choice(greys)) + ' '
                pixels += '\n'
                target.write(header+pixels)
