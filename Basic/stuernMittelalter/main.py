from Einwohner import *
from Bauer import *
from Adel import *
from Koenig import *
from Leibeigener import *

def main():
    koenig = Koenig()
    koenig.setEinkommen(4000)
    print(koenig.steuer())

if __name__ == '__main__':
    main()
