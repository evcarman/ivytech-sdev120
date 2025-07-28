num SIZE = 20
num ARRAY_LIMIT = size - 1
num userNumbers[SIZE]

for x = 0 to ARRAY_LIMIT step 1
    output “Please enter a number for index “ + x + “: “
    input userNumbers(x)
endfor

for y = arrayLimit to 0 step -1
    output userNumbers(y)
end for
