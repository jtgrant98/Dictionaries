
def main():


    outfile = open('philosophers.txt','w')

    outfile.write('John Locke' + '\n')
    outfile.write('David Hum\n')
    outfile.write('Edmund Burke')

    outfile.close()



    outfile = open('philosophers.txt', 'a')
    outfile.write('\nJosh Grant')

    outfile.close()

main()
