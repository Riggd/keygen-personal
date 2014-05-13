'''
Basic Secret Key Generator
Stores in external file which can then be read an inserted into application.
'''
import os
import random
import sys

length = int(raw_input('Please enter a length for your secret key: '))
filename = raw_input('Please enter a name for the file: ')
filename = filename + '.txt'

def generate_secret_key(length, filename):

    while (length < 500):
        length = int(raw_input('Please enter a larger integer: '))
        
    secret_key = ''
    for i in range(length):
        secret_key += chr(random.SystemRandom().randint(33,126))    
    
    file = open(filename, 'w')
    file.write(secret_key)
    file.close()
 
def print_file(filename):
    file = open(filename, 'r')
    print 'Your secret key is: '
    print file.read().strip()
    file.close()

def write_to_environment(filename):
    file = open(filename, 'r')
    key = file.read().strip()
    os.environ['SECRET_KEY'] = key
    file.close()

if __name__ == '__main__':
    generate_secret_key(length,filename)
    print_file(filename)
    #write_to_environment(filename)