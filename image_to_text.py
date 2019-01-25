from PIL import Image
import ansiwrap
from data.textures import *
import colorama
colorama.init(strip=True)

ASCII_CHARS = [' ',',',':',';','+','*','?','%','S','@','#']
ASCII_CHARS = ASCII_CHARS[::-1]
CHARS = {
    'player': PLAYER_CHAR,
    'floor': FLOOR_CHAR,
    'empty': ' ',
    'door': DOOR_CHAR,
    'monster': MONSTER_CHAR,
    'wall': WALL_CHAR_UP_DOWN
    }

'''
method resize():
    - takes as parameters the image, and the final width
    - resizes the image into the final width while maintaining aspect ratio
'''
def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
'''
method grayscalify():
    - takes an image as a parameter
    - returns the grayscale version of image
'''
def grayscalify(image):
    return image.convert('L')

'''
method modify():
    - replaces every pixel with a character whose intensity is similar
'''
def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [char_picker(pixel_value) for pixel_value in initial_pixels]
    # return ''.join(new_pixels)
    return new_pixels

'''
My own for deciding character :)
'''
def char_picker(pixel):
    # pink == player
    if pixel[0] > 150 and pixel[1] < 150 and pixel[2] > 150:
        return 'player'
    # white == empty space
    if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
        return 'empty'
    # black == wall
    if pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
        return 'wall'
    # red == door
    if pixel[0] > 150 and pixel[1] < 150 and pixel[2] < 150:
        return 'door'
    # green == floor
    if pixel[0] < 50 and pixel[1] > 120 and pixel[2] < 50:
        return 'monster'
    # leftover colors == floor
    else:
        return 'floor'

'''
method do():
    - does all the work by calling all the above functions
'''
def do(image, new_width=40):
    # image = resize(image, 40)
    # image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+image.size[0]] for index in range(0, len_pixels, image.size[0])]
    image = ""
    for i, line in enumerate(new_image):
        for j, word in enumerate(line):
            if word in CHARS:
                new_image[i][j] = CHARS[word]
                image += CHARS[word]
                if word == 'wall' or word == 'door':
                    try:
                        if new_image[i][j+1] == 'wall' or new_image[i][j+1] == 'empty' or new_image[i][j+1] == 'door':
                            image += CHARS['wall']
                        else:
                            image += ' '

                    except:
                        pass
                else:
                    image += ' '
        image += '\n'

    sliced = []
    coord = (10,15)
    cut = 10//2

    for i in range(-cut, cut):
        row =[]
        check = i+coord[0]
        if check >= 0:
            try:
                for part in new_image[check]:

                        try:
                            row.append(part)
                            # sliced.append(' \n')
                            # print(part)
                            # print("".join(part[coord[1]-cut:coord[1]+cut]))
                        except:
                            row.append(' ')
                            # sliced.append(' \n')
                # sliced.append('\n')
            except:
                # sliced.append(' \n')
                pass
            if row:
                sliced.append(row)

    # print("\n".join(''.join(row) for row in sliced))
        # image += " ".join(line) + "\n"


    return image

'''
method runner():
    - takes as parameter the image path and runs the above code
    - handles exceptions as well
    - provides alternative output options
'''
def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        #print(e)
        return
    image = do(image)

    # To print on console
    print(image)

    # Else, to write into a file
    # Note: This text file will be created by default under
    #       the same directory as this python file,
    #       NOT in the directory from where the image is pulled.
    # f = open('img.txt','w')
    # f.write(image)
    # f.close()

'''
method main():
    - reads input from console
    - profit
'''
if __name__ == '__main__':
    # import sys
    # import urllib.request
    # if sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://'):
    #     urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
    #     path = "asciify.jpg"
    # else:
    #     path = sys.argv[1]
    runner('test2.png')
