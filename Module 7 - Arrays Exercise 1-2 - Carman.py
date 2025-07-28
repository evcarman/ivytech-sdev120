START
    # DECLARATIONS
    num SIZE = 20
    num ARRAY_LIMIT = SIZE - 1
    num userNumbers[SIZE]
    num index = 0
    string END_PROGRAM = “N”
    string sentinel = “Y”
    string PROMPT = “Select Y or N to enter another value: “

    housekeeping()
    do while index < size AND sentinel <> END_PROGRAM
        output “Please enter a number for index “ + index + “: “
        input userNumbers(index)
        index = index + 1
    endwhile
    endofjob()

END

housekeeping()
    output PROMPT
    input sentinel
return

endofjob()
    for y = index to 0 step - 1
        output userNumbers(y)
    endfor
return
