START
    # DECLARATIONS
    num sum = 0
    string PROMPT = “Enter another value or 0 to end: “
    num userEntry = 0

    housekeeping()
    do while userEntry <> 0
            sum = sum + userEntry
            output PROMPT
            input userEntry
    endwhile
    endofjob()
END

housekeeping()
    output PROMPT
    input userEntry
return

endofjob()
    output sum
return
