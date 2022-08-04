#short code
import re
print( sum( [ int(a) for a in re.findall('[0-9]+', open('REact.txt').read()) ] ) )